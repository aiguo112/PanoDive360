import os

import torch
import torch.nn.functional as F
from tqdm import tqdm
import numpy as np
from torch.utils.tensorboard import SummaryWriter
import torch.optim as optim
from losses import combined_loss
from dataset import train_loader, valid_loader
from model import CustomDeepLabV3Plus
from config import num_classes

def calculate_iou(pred, mask, num_classes):
    ious = []
    pred = pred.view(-1)
    mask = mask.view(-1)

    for cls in range(num_classes):
        pred_inds = (pred == cls)
        target_inds = (mask == cls)
        intersection = (pred_inds[target_inds]).long().sum().item()
        union = pred_inds.long().sum().item() + target_inds.long().sum().item() - intersection
        if union == 0:
            ious.append(float('nan'))  # If there is no ground truth, do not include in evaluation
        else:
            ious.append(float(intersection) / max(union, 1))
    return np.array(ious)

def save_checkpoint(epoch, model, optimizer, path):
    state = {
        'epoch': epoch,
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }
    torch.save(state, path)
    print(f'Model and optimizer saved at {path}')

def train_model(model, train_loader, valid_loader, criterion, optimizer, num_epochs, patience, model_name):
    best_loss = float('inf')
    epochs_no_improve = 0
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=patience, verbose=True)

    log_dir = os.path.join(r'/home/arbi/PycharmProjects/Data_Prep_Pano/runs', model_name)
    writer = SummaryWriter(log_dir=log_dir)

    for epoch in range(num_epochs):
        model.train()
        train_loss = 0
        train_correct = 0
        train_total = 0
        train_ious = []

        for images, masks in tqdm(train_loader, desc=f'Epoch {epoch + 1}/{num_epochs}'):
            images = images.cuda()
            masks = masks.cuda()
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks.argmax(dim=1))
            loss.backward()
            optimizer.step()
            train_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            predicted = F.interpolate(predicted.unsqueeze(1).float(), size=masks.shape[2:], mode='nearest').squeeze(1)
            train_total += masks.numel() // masks.shape[1]
            train_correct += (predicted == masks.argmax(dim=1)).sum().item()
            train_ious.append(calculate_iou(predicted, masks.argmax(dim=1), num_classes))

        train_accuracy = train_correct / train_total
        train_iou = np.nanmean(np.array(train_ious), axis=0)

        valid_loss = 0
        valid_correct = 0
        valid_total = 0
        valid_ious = []
        model.eval()
        with torch.no_grad():
            for images, masks in valid_loader:
                images = images.cuda()
                masks = masks.cuda()
                outputs = model(images)
                loss = criterion(outputs, masks.argmax(dim=1))
                valid_loss += loss.item()

                _, predicted = torch.max(outputs.data, 1)
                predicted = F.interpolate(predicted.unsqueeze(1).float(), size=masks.shape[2:], mode='nearest').squeeze(1)
                valid_total += masks.numel() // masks.shape[1]
                valid_correct += (predicted == masks.argmax(dim=1)).sum().item()
                valid_ious.append(calculate_iou(predicted, masks.argmax(dim=1), num_classes))

        valid_accuracy = valid_correct / valid_total
        valid_iou = np.nanmean(np.array(valid_ious), axis=0)

        writer.add_scalar('Loss/Train', train_loss / len(train_loader), epoch)
        writer.add_scalar('Loss/Valid', valid_loss / len(valid_loader), epoch)
        writer.add_scalar('Accuracy/Train', train_accuracy, epoch)
        writer.add_scalar('Accuracy/Valid', valid_accuracy, epoch)
        writer.add_scalar('IoU/Train', train_iou.mean(), epoch)
        writer.add_scalar('IoU/Valid', valid_iou.mean(), epoch)

        checkpoint_path = os.path.join(log_dir, f'{model_name}_epoch_{epoch+1}.pth')
        save_checkpoint(epoch+1, model, optimizer, checkpoint_path)

        print(f'Epoch {epoch + 1}/{num_epochs} - Train loss: {train_loss / len(train_loader):.4f} - Train accuracy: {train_accuracy:.4f} - Train IoU: {train_iou.mean():.4f}')
        print(f'Epoch {epoch + 1}/{num_epochs} - Valid loss: {valid_loss / len(valid_loader):.4f} - Valid accuracy: {valid_accuracy:.4f} - Valid IoU: {valid_iou.mean():.4f}')

        scheduler.step(valid_loss / len(valid_loader))
        if valid_loss < best_loss:
            best_loss = valid_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= patience:
                print(f'Early stopping at epoch {epoch + 1}')
                break

    writer.close()

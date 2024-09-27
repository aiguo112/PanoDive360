import torch
import torch.optim as optim
from csutom_model import CustomDeepLabV3Plus
from train import train_model
from losses import combined_loss
from dataset import train_loader, valid_loader
from config import num_classes

# Train CustomDeepLabV3Plus model
model_name = 'CustomDeepLabV3Plus'
model = CustomDeepLabV3Plus(encoder_name="resnet34", encoder_weights="imagenet", in_channels=3, classes=num_classes)
model = torch.nn.DataParallel(model).cuda()

optimizer = optim.Adam(model.parameters(), lr=1e-4)
criterion = combined_loss

train_model(model, train_loader, valid_loader, criterion, optimizer, num_epochs=25, patience=5, model_name=model_name)
print(f'Training completed for {model_name}. Ready to evaluate and compare the results.')

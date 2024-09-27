import os
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import torch
from torchvision import transforms
import numpy as np
from config import color_map, input_size, train_images_dir, valid_images_dir, train_masks_dir, valid_masks_dir
from utils import rgb_to_onehot


class SegmentationDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.image_filenames = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
        self.transform = transform

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        image_filename = self.image_filenames[idx]
        image_path = os.path.join(self.image_dir, image_filename)
        mask_filename = image_filename.replace('image_', 'mask_').replace('.jpg', '.png')
        mask_path = os.path.join(self.mask_dir, mask_filename)

        if not os.path.exists(mask_path):
            raise FileNotFoundError(f"Mask file not found for {image_path} corresponding to {mask_path}")

        image = Image.open(image_path).convert('RGB')
        mask = Image.open(mask_path).convert('RGB')
        mask = np.array(mask, dtype=np.float32)
        mask = rgb_to_onehot(mask, color_map)
        mask = np.transpose(mask, (2, 0, 1))  # Channels first for PyTorch

        if self.transform:
            image = self.transform(image)

        return image, torch.tensor(mask, dtype=torch.float32)


# Transformations
transform = transforms.Compose([
    transforms.Resize(input_size),
    transforms.ToTensor(),
])

# Datasets and DataLoaders
train_dataset = SegmentationDataset(train_images_dir, train_masks_dir, transform)
valid_dataset = SegmentationDataset(valid_images_dir, valid_masks_dir, transform)
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=4, shuffle=False)

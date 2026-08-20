import os
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import torch
from torchvision import transforms
import numpy as np

from panodive360.config import (
    color_map,
    input_size,
    train_images_dir,
    valid_images_dir,
    train_masks_dir,
    valid_masks_dir,
    batch_size,
)
from panodive360.data.mask_utils import rgb_to_onehot

IMAGE_EXTS = ('.png', '.jpg', '.jpeg', '.JPG', '.JPEG', '.PNG')


def _mask_path(mask_dir, image_filename):
    stem, _ = os.path.splitext(image_filename)
    candidates = [
        image_filename.replace('image_', 'mask_').replace('.jpg', '.png').replace('.jpeg', '.png'),
        stem + '.png',
        image_filename,
    ]
    for name in candidates:
        path = os.path.join(mask_dir, name)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(
        f'No mask for {image_filename} in {mask_dir}. Tried: {candidates}'
    )


class SegmentationDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.image_filenames = sorted(
            f for f in os.listdir(image_dir)
            if os.path.isfile(os.path.join(image_dir, f)) and f.endswith(IMAGE_EXTS)
        )
        self.transform = transform

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        image_filename = self.image_filenames[idx]
        image_path = os.path.join(self.image_dir, image_filename)
        mask_path = _mask_path(self.mask_dir, image_filename)

        image = Image.open(image_path).convert('RGB')
        mask = Image.open(mask_path).convert('RGB')
        mask = np.array(mask, dtype=np.float32)
        mask = rgb_to_onehot(mask, color_map)
        mask = np.transpose(mask, (2, 0, 1))

        if self.transform:
            image = self.transform(image)

        return image, torch.tensor(mask, dtype=torch.float32)


def get_dataloaders(train_batch_size=None, valid_batch_size=None):
    transform = transforms.Compose([
        transforms.Resize(input_size),
        transforms.ToTensor(),
    ])
    train_bs = batch_size if train_batch_size is None else train_batch_size
    valid_bs = batch_size if valid_batch_size is None else valid_batch_size

    for path, label in (
        (train_images_dir, 'train images'),
        (train_masks_dir, 'train masks'),
        (valid_images_dir, 'valid images'),
        (valid_masks_dir, 'valid masks'),
    ):
        if not os.path.isdir(path):
            raise FileNotFoundError(
                f'Missing {label} directory: {path}. Put the split under data/splits/ or set PANODIVE360_DATA.'
            )

    train_dataset = SegmentationDataset(train_images_dir, train_masks_dir, transform)
    valid_dataset = SegmentationDataset(valid_images_dir, valid_masks_dir, transform)
    train_loader = DataLoader(train_dataset, batch_size=train_bs, shuffle=True)
    valid_loader = DataLoader(valid_dataset, batch_size=valid_bs, shuffle=False)
    return train_loader, valid_loader

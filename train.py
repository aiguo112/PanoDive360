"""Train the ERP-CBAM DeepLabv3+ baseline.

Run from the repository root:

    python train.py
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import torch
import torch.optim as optim

from panodive360.config import learning_rate, num_classes, num_epochs, patience
from panodive360.data import get_dataloaders
from panodive360.losses import combined_loss
from panodive360.models import DeepLabV3PlusERPCBAM
from panodive360.trainer import train_model


def main():
    model_name = 'DeepLabV3PlusERPCBAM'
    model = DeepLabV3PlusERPCBAM(
        encoder_name='resnet34',
        encoder_weights='imagenet',
        in_channels=3,
        classes=num_classes,
    )
    model = torch.nn.DataParallel(model).cuda()

    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    train_loader, valid_loader = get_dataloaders()

    train_model(
        model,
        train_loader,
        valid_loader,
        combined_loss,
        optimizer,
        num_epochs=num_epochs,
        patience=patience,
        model_name=model_name,
    )
    print(f'Training completed for {model_name}.')


if __name__ == '__main__':
    main()

"""Optional drop-in training entry that matches the paper seed protocol.

Copy to the PanoDive360 repo root as train_seeded.py, then:

    python train_seeded.py --seed 42
    python train_seeded.py --seed 123
    python train_seeded.py --seed 777

Keep input resolution at 1440x720 (2:1 ERP). Do not use the square
1024x1024 resize currently in panodive360/config.py if you want paper numbers.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE
for candidate in (HERE, HERE.parent, HERE.parent.parent):
    if (candidate / "panodive360").is_dir():
        ROOT = candidate
        break
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import torch
import torch.optim as optim

from panodive360.config import learning_rate, num_classes, num_epochs, patience
from panodive360.data import get_dataloaders
from panodive360.losses import combined_loss
from panodive360.models import DeepLabV3PlusERPCBAM
from panodive360.trainer import train_model

try:
    from panodive360.seed import set_seed
except ImportError:
    from seed import set_seed  # same folder fallback


def parse_args():
    p = argparse.ArgumentParser(description="Train ERP-CBAM with a paper seed.")
    p.add_argument("--seed", type=int, default=42, choices=[42, 123, 777],
                   help="Random seed. Paper robustness set: 42, 123, 777.")
    return p.parse_args()


def main():
    args = parse_args()
    set_seed(args.seed)

    model_name = f"DeepLabV3PlusERPCBAM_seed{args.seed}"
    model = DeepLabV3PlusERPCBAM(
        encoder_name="resnet34",
        encoder_weights="imagenet",
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
    print(f"Training completed for {model_name} (seed={args.seed}).")


if __name__ == "__main__":
    main()

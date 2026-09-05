"""Deterministic seeding used for the three-seed ERP-CBAM study.

Drop this file into the PanoDive360 repository as panodive360/seed.py
and call set_seed(args.seed) at the start of train.py.

Seeds reported in the ACM supplementary material: 42, 123, 777.
"""
from __future__ import annotations

import os
import random

import numpy as np
import torch


PAPER_SEEDS = (42, 123, 777)
MAIN_TABLE_SEED = 42


def set_seed(seed: int, cudnn_deterministic: bool = True) -> None:
    """Seed Python, NumPy, and PyTorch (CPU + CUDA) consistently.

    The three-seed study in the paper/supplement used this protocol and
    evaluated the epoch-25 checkpoint on the same 211-image test split.
    """
    seed = int(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    if cudnn_deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def seed_worker(worker_id: int) -> None:
    """Pass to DataLoader(worker_init_fn=seed_worker) for full reproducibility."""
    worker_seed = torch.initial_seed() % 2**32
    np.random.seed(worker_seed)
    random.seed(worker_seed)

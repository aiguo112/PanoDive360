## Supplementary material

Extra protocol, random-seed runs, and graphs for the ACM Multimedia Asia 2026 paper are in [`supplementary/`](supplementary/).

| Item | Detail |
| --- | --- |
| PDF | [`supplementary/PanoDive360_supplementary.pdf`](supplementary/PanoDive360_supplementary.pdf) |
| Seeds | 42 (main table), 123, 777 (robustness) |
| Three-seed test mIoU | 0.6503 ± 0.0183 |
| Paper resolution | 1440×720 ERP (not the 1024×1024 default in `config.py`) |

Reproduce the three seeds after copying `supplementary/scripts/seed.py` into `panodive360/` and `supplementary/scripts/train_seeded.py` to the repo root:

```bash
python train_seeded.py --seed 42
python train_seeded.py --seed 123
python train_seeded.py --seed 777
```

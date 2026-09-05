# ACM MMAsia supplementary material for PanoDive360

This folder is ready to copy into [https://github.com/aiguo112/PanoDive360](https://github.com/aiguo112/PanoDive360) as `supplementary/`. Nothing has been uploaded for you.

## What you upload

| Destination | File | Notes |
| --- | --- | --- |
| **GitHub repo** | this whole folder → `supplementary/` | public code release |
| **CMT (optional)** | `PanoDive360_supplementary.pdf` only | strip authors if review is still double-blind |

Recommended GitHub layout after you copy:

```text
PanoDive360/
├── supplementary/
│   ├── PanoDive360_supplementary.pdf   ← upload this PDF
│   ├── PanoDive360_supplementary.tex   ← Overleaf source if you want ACM LaTeX
│   ├── protocol.yaml                   ← exact paper settings + seeds
│   ├── README.md
│   ├── figures/                        ← chapter graphs (S1–S8)
│   ├── tables/                         ← CSV + JSON of every number
│   └── scripts/
│       ├── seed.py                     ← copy to panodive360/seed.py
│       ├── train_seeded.py             ← copy to repo root
│       └── build_pdf.py
```

## Random seeds (the extra chapter experiment)

| Seed | Test mIoU | Pixel accuracy |
| ---: | ---: | ---: |
| 42 | 0.6702 | 0.9597 |
| 123 | 0.6342 | 0.9592 |
| 777 | 0.6465 | 0.9578 |
| **Mean ± std** | **0.6503 ± 0.0183** | **0.9589 ± 0.0010** |

- Main comparison table in the paper: seed **42**, ERP-CBAM mIoU **0.662**.
- Three-seed study: epoch-25 checkpoint, same 211-image test split.
- Seed 42 at epoch 25 (0.6702) is ordinary run-to-run variation around 0.662.
- Lowest seed (123 → 0.6342) is still 18.3% above DeepLabv3+ (0.536).
- These runs share one split. They are seed robustness, not $k$-fold split variance.

Python / NumPy / PyTorch CPU+CUDA were all seeded; cuDNN deterministic.

```bash
python train_seeded.py --seed 42
python train_seeded.py --seed 123
python train_seeded.py --seed 777
```

After copying `scripts/seed.py` → `panodive360/seed.py` and `scripts/train_seeded.py` → repo root.

## Graphs included (from the PanoDive360 chapter)

| Figure | File | In main chapter? |
| --- | --- | --- |
| S1 Three-seed test mIoU bar | `figures/figS1_multiseed_test_miou_bar.pdf` | yes (`ch3_multiseed_test_miou_bar`) |
| S2 Three-seed val mIoU curves | `figures/figS2_multiseed_val_miou.pdf` | yes |
| S3 Train+val mIoU (three seeds) | `figures/figS3_multiseed_train_val_miou.pdf` | extra (folder only) |
| S4 Val loss (three seeds) | `figures/figS4_multiseed_val_loss.pdf` | extra (folder only) |
| S5 Compute / memory | `figures/figS5_compute_efficiency.pdf` | yes |
| S6 Radar metrics | `figures/figS6_radar_metrics.png` | yes |
| S7 Grouped bars | `figures/figS7_grouped_bar_metrics.png` | yes |
| S8 Class histogram | `figures/figS8_class_distribution.png` | yes |

## Important mismatch in the public code

`panodive360/config.py` currently has `input_size = (1024, 1024)`. The paper uses **1440×720** (2:1 ERP, no crop). Video FPS used **1440×736** (pad to a multiple of 32). If you leave 1024×1024 you will not match these tables.

## How to copy (you do this)

From PowerShell, after `cd` into a clone of PanoDive360:

```powershell
Copy-Item -Recurse "G:\PPTS\ustc_thesis_skeleton (2)\PanoDive360_ACM_supplementary" .\supplementary
git add supplementary
git commit -m "Add ACM MMAsia supplementary material (seeds, compute, extra graphs)."
git push
```

Then paste the block in `README_GITHUB_SNIPPET.md` into the root `README.md` if you want a visible link.

## Rebuild the PDF

```powershell
python supplementary/scripts/build_pdf.py
```

Or compile `PanoDive360_supplementary.tex` on Overleaf (`pdflatex` once is enough).

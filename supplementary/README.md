# Supplementary material (anonymous)

This folder is the extra protocol and figures for the ACM Multimedia Asia 2026 paper on PanoDive360. It contains no author names and no code-repository URLs.

## Contents

- `PanoDive360_supplementary.pdf` — upload this PDF to CMT
- `PanoDive360_supplementary.tex` — LaTeX source
- `protocol.yaml` — paper hyperparameters and seeds
- `figures/` — graphs S1–S8
- `tables/` — CSV/JSON of every reported number
- `scripts/seed.py` and `scripts/train_seeded.py` — seed protocol

## Random seeds

| Seed | Test mIoU | Pixel accuracy |
| ---: | ---: | ---: |
| 42 | 0.6702 | 0.9597 |
| 123 | 0.6342 | 0.9592 |
| 777 | 0.6465 | 0.9578 |
| **Mean ± std** | **0.6503 ± 0.0183** | **0.9589 ± 0.0010** |

- Main comparison table: seed 42, ERP-CBAM mIoU 0.662.
- Three-seed study: epoch-25 checkpoint, same 211-image test split.
- These runs share one split (seed robustness, not split variance).

```bash
python train_seeded.py --seed 42
python train_seeded.py --seed 123
python train_seeded.py --seed 777
```

## Figures

| Figure | File |
| --- | --- |
| S1 Three-seed test mIoU bar | `figures/figS1_multiseed_test_miou_bar.pdf` |
| S2 Three-seed val mIoU curves | `figures/figS2_multiseed_val_miou.pdf` |
| S3 Train+val mIoU (three seeds) | `figures/figS3_multiseed_train_val_miou.pdf` |
| S4 Val loss (three seeds) | `figures/figS4_multiseed_val_loss.pdf` |
| S5 Compute / memory | `figures/figS5_compute_efficiency.pdf` |
| S6 Radar metrics | `figures/figS6_radar_metrics.png` |
| S7 Grouped bars | `figures/figS7_grouped_bar_metrics.png` |
| S8 Class histogram | `figures/figS8_class_distribution.png` |

## Resolution note

The paper uses **1440×720** (2:1 ERP, no crop). Video FPS used **1440×736**. A square 1024×1024 resize will not match these tables.

## Rebuild the PDF

```bash
python scripts/build_pdf.py
```

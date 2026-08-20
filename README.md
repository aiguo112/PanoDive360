# PanoDive360

![PanoDive360 teaser: RGB equirectangular frame, ground-truth mask, and overlay](assets/teaser.jpg)

*Example ERP still (frame 417) with pixel labels for diver and shipwreck. The dataset has 11 classes in total.*

Equirectangular (ERP) dataset and CNN benchmark for **underwater 360-degree multiclass semantic segmentation**.

Almost all marine segmentation datasets assume a narrow-field pinhole camera. ERP 360-degree imagery removes blind spots, but it stretches objects near the poles, wraps instances across the image seam, and mixes low-visibility water with cluttered fauna. PanoDive360 is a pixel-annotated underwater ERP set and a first CNN baseline on that set.

This repository is the **code release** (preprocessing helpers + training scripts). The image/mask archive is not stored here.

## Dataset (main contribution)

| Item | Value |
| --- | --- |
| Frames | 1,052 stills from 30 publicly shared 4K 360-degree videos |
| Projection | Monoscopic ERP, 2:1 aspect, pixel labels on the ERP image |
| Classes | 11 (10 foreground + background water) |
| Source | Publicly shared platforms such as YouTube (not public-domain by default) |
| Prep | Audio stripped; side-by-side / over-under converted to mono ERP; stills extracted with FFmpeg |

Foreground classes, frame counts, and mask RGB colors:

| Class | Frames | % of 1,052 | RGB |
| --- | ---: | ---: | --- |
| Diver | 1010 | 96.0 | (167, 242, 82) |
| Shark | 310 | 29.5 | (166, 3, 3) |
| Fish | 267 | 25.4 | (255, 237, 29) |
| Sea turtle | 41 | 3.9 | (255, 0, 243) |
| Dolphin | 27 | 2.6 | (30, 95, 170) |
| Sea lion | 68 | 6.5 | (169, 205, 248) |
| Coral | 96 | 9.1 | (106, 37, 163) |
| Shipwreck | 275 | 26.1 | (115, 76, 20) |
| Seaweed | 323 | 30.7 | (233, 180, 245) |
| Rock | 272 | 25.9 | (245, 94, 94) |
| Background | 1052 | 100 | (0, 0, 0) |

Diver is present in almost every frame; dolphin and sea turtle are rare. The set is strongly imbalanced. Source URLs, platform terms of use, and a labeling codebook are intended to ship with the public image package.

## CNN benchmark (diagnostic, not a SOTA claim)

Shared-protocol CNNs in the paper: U-Net, U-Net++, PSPNet, DeepLabv3+, and ERP-CBAM (DeepLabv3+ / ResNet-34 with a latitude-weighted spatial attention block).

Relative to DeepLabv3+, ERP-CBAM raises mean IoU (0.536 → 0.606), recall (0.680 → 0.758), F1, Dice, and balanced accuracy. It is **not** best among these five CNNs on accuracy, precision, or MCC. Treat ERP-CBAM as a diagnostic baseline rather than a generally superior architecture.

Ablation in the paper: removing the latitude term can raise mIoU while the full ERP-CBAM setting is stronger on recall / balanced accuracy. That is a trade-off, not a uniform win.

## Layout expected by the training script

```text
data_split/
  train/
    images/     # e.g. image_001.jpg
    masks/      # e.g. mask_001.png (RGB labels, same stem)
  valid/
    images/
    masks/
```

Set the data root with `PANODIVE360_DATA` or edit `config.py`. Checkpoints and TensorBoard logs go to `runs/` (or `PANODIVE360_RUNS`).

## Setup

```bash
pip install -r requirements.txt
```

Install a CUDA build of PyTorch that matches your GPU from the [PyTorch install page](https://pytorch.org/get-started/locally/). Then:

```bash
python main.py
```

`main.py` trains the ERP-CBAM DeepLabv3+ variant (`csutom_model.py`). Vanilla CBAM DeepLabv3+ is in `model.py`.

Helpers:

- `stereo_to_mono_converter.py` — dual-channel 360 layouts to monoscopic ERP
- `VideoFrameExtractor.py` — FFmpeg still extraction
- `ImageResizer.py` — optional 2:1 resize (default example 1664×832)

## Files

| File | Role |
| --- | --- |
| `config.py` | Paths, 11-class RGB map, input size |
| `dataset.py` | `SegmentationDataset` and loaders |
| `utils.py` | RGB mask ↔ one-hot |
| `losses.py` | Dice + cross-entropy |
| `cbam.py` | Standard CBAM |
| `erp_cbam.py` | Latitude-weighted spatial attention |
| `model.py` | DeepLabv3+ + CBAM |
| `csutom_model.py` | DeepLabv3+ + ERP-CBAM (used by `main.py`) |
| `train.py` | Train / val loop, checkpoints, TensorBoard |
| `main.py` | Entry point |

## License

Code: MIT (see `LICENSE`). Dataset media remain under their original platform terms; this repo does not redistribute the videos.

# Dataset layout

PanoDive360 labels 1,052 monoscopic ERP stills into 11 classes (10 foreground + background water). **Images and masks are not stored in this git repo.** Place your local copy here, or set `PANODIVE360_DATA` to another root with the same layout.

```text
data/
  raw/                         # optional: source 360 videos
  splits/
    train/
      images/                  # RGB stills, e.g. image_001.jpg or initial_360-ERP_417.jpg
      masks/                   # RGB label PNGs, same stem, e.g. mask_001.png
    valid/
      images/
      masks/
    test/
      images/
      masks/
```

Mask files can share the image stem (`initial_360-ERP_417.jpg` ↔ `initial_360-ERP_417.png`) or use the older `image_*` / `mask_*` naming.

## Classes and RGB colors

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

Source videos come from publicly shared platforms such as YouTube. They are not public-domain by default. Do not commit raw video or full image dumps to git.

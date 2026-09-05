"""Build PanoDive360_supplementary.pdf (ACM MMAsia extra material).

Run from this folder:
    python scripts/build_pdf.py
"""
from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures"
OUT = ROOT / "PanoDive360_supplementary.pdf"

NAVY = colors.HexColor("#1f4e79")
HEADER_BG = colors.HexColor("#1f4e79")
ROW_ALT = colors.HexColor("#f2f6fa")
LINE = colors.HexColor("#8aa0b8")


def styles():
    base = getSampleStyleSheet()
    s = {
        "title": ParagraphStyle(
            "TitleS",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=14,
            leading=18,
            alignment=TA_CENTER,
            spaceAfter=4,
            textColor=NAVY,
        ),
        "subtitle": ParagraphStyle(
            "SubS",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "meta": ParagraphStyle(
            "MetaS",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=10,
            leading=13,
            alignment=TA_CENTER,
            spaceAfter=10,
        ),
        "h1": ParagraphStyle(
            "H1S",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=12,
            leading=16,
            spaceBefore=12,
            spaceAfter=6,
            textColor=NAVY,
        ),
        "h2": ParagraphStyle(
            "H2S",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=8,
            spaceAfter=4,
            textColor=NAVY,
        ),
        "body": ParagraphStyle(
            "BodyS",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "caption": ParagraphStyle(
            "CapS",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            spaceBefore=3,
            spaceAfter=10,
        ),
        "code": ParagraphStyle(
            "CodeS",
            parent=base["Normal"],
            fontName="Courier",
            fontSize=8.5,
            leading=11,
            leftIndent=12,
            spaceAfter=6,
        ),
        "cell": ParagraphStyle(
            "CellS",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
        ),
        "cellL": ParagraphStyle(
            "CellLS",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=8,
            leading=10,
            alignment=TA_LEFT,
        ),
        "cellB": ParagraphStyle(
            "CellBS",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
        ),
        "th": ParagraphStyle(
            "THS",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=colors.white,
        ),
        "foot": ParagraphStyle(
            "FootS",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#555555"),
        ),
    }
    return s


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 12, A4[0], 12, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(
        18 * mm,
        A4[1] - 9,
        "Supplementary Material  |  PanoDive360  |  ACM Multimedia Asia 2026",
    )
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, A4[0], 14, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawCentredString(A4[0] / 2, 5, f"{doc.page}")
    canvas.restoreState()


def make_table(headers, rows, col_widths, s, bold_last=False):
    th = [Paragraph(h, s["th"]) for h in headers]
    data = [th]
    for i, row in enumerate(rows):
        styled = []
        use_bold = bold_last and i == len(rows) - 1
        for j, val in enumerate(row):
            st = s["cellB"] if use_bold else (s["cellL"] if j == 0 else s["cell"])
            styled.append(Paragraph(str(val), st))
        data.append(styled)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    if bold_last:
        cmds.append(("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#dce8f5")))
    t.setStyle(TableStyle(cmds))
    return t


def fig(path: Path, width, s, caption: str):
    if not path.exists():
        return [Paragraph(f"[missing {path.name}]", s["body"])]
    img = Image(str(path), width=width, height=width * 0.55, kind="proportional")
    # restore true aspect
    from PIL import Image as PILImage

    with PILImage.open(path) as im:
        w, h = im.size
    img.drawWidth = width
    img.drawHeight = width * (h / w)
    img.hAlign = "CENTER"
    return KeepTogether([img, Paragraph(caption, s["caption"])])


def build():
    s = styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=22 * mm,
        bottomMargin=18 * mm,
        title="Supplementary Material: PanoDive360",
        author="Ghulam Arbi, Lu Zhang, Yanyong Zhang",
    )
    story = []
    usable = A4[0] - 36 * mm

    story.append(Paragraph("Supplementary Material", s["title"]))
    story.append(
        Paragraph(
            "PanoDive360: A Novel Equirectangular Projection Dataset and Enhanced "
            "Attention Mechanism for Underwater 360-Degree Multiclass Semantic Segmentation",
            s["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "Ghulam Arbi, Lu Zhang, and Yanyong Zhang<br/>"
            "University of Science and Technology of China<br/>"
            "ACM Multimedia Asia 2026",
            s["meta"],
        )
    )
    story.append(
        Paragraph(
            "This supplement records the reproducibility protocol and the extra "
            "experiments that do not fit in the 6-page ACM main paper: random-seed "
            "robustness (seeds 42, 123, 777), training/validation curves, and ERP "
            "video-inference cost. All numbers and graphs match the PanoDive360 "
            "chapter. Upload this folder to "
            "<font color='blue'><u>https://github.com/aiguo112/PanoDive360</u></font> "
            "as <font face='Courier'>supplementary/</font>. "
            "For CMT double-blind review, strip the author block before uploading the PDF.",
            s["body"],
        )
    )

    story.append(Paragraph("1. Reproducibility protocol", s["h1"]))
    story.append(Paragraph("1.1 Software and hardware", s["h2"]))
    story.append(
        Paragraph(
            "All models were implemented in Python 3.8.19 with PyTorch 1.8.0, "
            "CUDA 11.1 and cuDNN 8902. Training used dual NVIDIA GeForce RTX 3060 "
            "GPUs (12 GB each) with data parallelism. Latency and FPS were measured "
            "on an RTX 5070 Ti: batch size = 1, 20 warm-up iterations, 100 timed "
            "iterations, CUDA synchronised, input padded to 1440×736.",
            s["body"],
        )
    )

    story.append(Paragraph("1.2 Training hyperparameters", s["h2"]))
    story.append(
        Paragraph(
            "The protocol below was applied identically to U-Net, U-Net++, PSPNet, "
            "DeepLabv3+ and ERP-CBAM. The paper resolution is 1440×720 (2:1 ERP, no crop). "
            "The public <font face='Courier'>panodive360/config.py</font> currently "
            "defaults to a square 1024×1024 resize; that setting does not reproduce "
            "the paper tables. Override it to (1440, 720) before rerunning.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Hyperparameter", "Value"],
            [
                ["Classes", "11"],
                ["Batch size", "4"],
                ["Optimizer", "Adam (β1=0.9, β2=0.999)"],
                ["Learning rate", "1×10⁻⁴"],
                ["Loss", "CE + Dice"],
                ["Epochs / early-stop patience", "25 / 5"],
                ["LR scheduler", "ReduceLROnPlateau (factor 0.5, patience 3)"],
                ["Input (train/test)", "1440×720 (2:1 ERP)"],
                ["Video inference (padded)", "1440×736"],
                ["Train / val / test", "1,472 / 421 / 211"],
                ["Backbone", "ResNet-34 (ImageNet)"],
            ],
            [usable * 0.45, usable * 0.55],
            s,
        )
    )
    story.append(Paragraph("Table S1. Training hyperparameters on PanoDive360.", s["caption"]))

    story.append(Paragraph("1.3 Random seeds", s["h2"]))
    story.append(
        Paragraph(
            "The nine-metric comparison against the four baselines uses a single run "
            "so that the ranking is exactly reproducible (main seed 42). ERP-CBAM was "
            "then retrained twice more under identical hyper-parameters, data splits, "
            "and the 25-epoch protocol, using seeds 123 and 777. Python, NumPy and "
            "PyTorch (CPU and CUDA) generators were seeded consistently; cuDNN was set "
            "deterministic. The epoch-25 checkpoint was evaluated on the same "
            "211-image test set. These runs share one train/val/test split: they probe "
            "seed robustness, not split variance.",
            s["body"],
        )
    )
    story.append(Paragraph("Helper in scripts/seed.py:", s["body"]))
    story.append(Paragraph("set_seed(42)    # or 123, 777", s["code"]))
    story.append(
        Paragraph(
            "Then: python train_seeded.py --seed 42  (repeat for 123 and 777).",
            s["code"],
        )
    )

    story.append(Paragraph("2. Three-seed robustness", s["h1"]))
    story.append(
        Paragraph(
            "Table S2 reports test mIoU and pixel accuracy for the three seeds. "
            "The seed-42 mIoU of 0.6702 lies within ordinary run-to-run variation of "
            "the main-table value 0.662. The lowest seed (123, mIoU 0.6342) still "
            "exceeds DeepLabv3+ (0.536) by 18.3% relative.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Seed", "Test mIoU", "Pixel accuracy"],
            [
                ["42", "0.6702", "0.9597"],
                ["123", "0.6342", "0.9592"],
                ["777", "0.6465", "0.9578"],
                ["Mean ± Std", "0.6503 ± 0.0183", "0.9589 ± 0.0010"],
            ],
            [usable / 3] * 3,
            s,
            bold_last=True,
        )
    )
    story.append(
        Paragraph(
            "Table S2. ERP-CBAM (DeepLabv3+, ResNet-34) on the same 211-image test split.",
            s["caption"],
        )
    )

    story.append(
        fig(
            FIG / "figS1_multiseed_test_miou_bar.png",
            usable * 0.82,
            s,
            "Figure S1. Test mIoU of ERP-CBAM for seeds 42, 123 and 777. "
            "Dashed line: mean (0.6503). Band: ±1 standard deviation (0.0183).",
        )
    )
    story.append(
        fig(
            FIG / "figS2_multiseed_val_miou.png",
            usable * 0.82,
            s,
            "Figure S2. Validation mIoU over 25 training epochs for the three seeded "
            "ERP-CBAM runs. The trajectories remain closely aligned.",
        )
    )
    story.append(
        fig(
            FIG / "figS3_multiseed_train_val_miou.png",
            usable * 0.82,
            s,
            "Figure S3. Training and validation mIoU for the three seeds "
            "(solid: validation; dashed: training). Extra curve not shown in the main paper.",
        )
    )
    story.append(
        fig(
            FIG / "figS4_multiseed_val_loss.png",
            usable * 0.82,
            s,
            "Figure S4. Validation loss over 25 epochs for seeds 42, 123 and 777. "
            "Extra curve not shown in the main paper.",
        )
    )

    story.append(Paragraph("3. Computational cost of ERP video inference", s["h1"]))
    story.append(
        Paragraph(
            "ERP-CBAM is DeepLabv3+ with latitude-weighted spatial attention. It cannot "
            "be substantially faster than its host. Table S3 shows +0.012 M parameters "
            "(+0.05%) and +0.017 GFLOPs (+0.007%) at 1440×736. On the RTX 5070 Ti, "
            "ERP-CBAM measures 79.1 FPS (12.64 ms) against 86.8 FPS for DeepLabv3+ "
            "(11.53 ms), about 9% slower. The claim that stands is that the mIoU gain "
            "is obtained inside the DeepLabv3+ compute envelope, not that ERP-CBAM is "
            "the fastest model.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Model", "Params (M)", "GFLOPs", "Peak mem. (MB)", "Latency (ms)", "FPS"],
            [
                ["U-Net", "24.44", "255.8", "623", "16.57", "60.3"],
                ["U-Net++", "26.08", "597.6", "1536", "38.46", "26.0"],
                ["PSPNet", "21.48", "77.2", "460", "4.83", "206.9"],
                ["DeepLabv3+", "22.44", "255.3", "774", "11.53", "86.8"],
                ["ERP-CBAM", "22.45", "255.4", "861", "12.64", "79.1"],
            ],
            [usable * 0.22, usable * 0.156, usable * 0.156, usable * 0.176, usable * 0.156, usable * 0.136],
            s,
            bold_last=True,
        )
    )
    story.append(
        Paragraph(
            "Table S3. ERP video inference (1440×736, batch = 1, 11 classes). "
            "Params/GFLOPs are hardware-independent. Latency/FPS: RTX 5070 Ti.",
            s["caption"],
        )
    )
    story.append(
        fig(
            FIG / "figS5_compute_efficiency.png",
            usable,
            s,
            "Figure S5. Left: GFLOPs per ERP frame (parameter count in parentheses). "
            "Right: peak GPU memory. ERP-CBAM is indistinguishable from DeepLabv3+ on "
            "FLOPs and stays below 1 GB of inference memory.",
        )
    )

    story.append(Paragraph("4. Full metric comparison", s["h1"]))
    story.append(
        Paragraph(
            "Table S4 repeats the nine-metric test-set comparison. Mean IoU and "
            "Balanced Accuracy are the primary ranking metrics because PanoDive360 is "
            "strongly imbalanced (diver in 1,010 of 1,052 frames; dolphin in 27). "
            "ERP-CBAM is not best on accuracy, precision, or MCC; treat it as a "
            "diagnostic ERP baseline rather than a generally superior architecture.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Model", "Acc.", "mIoU", "Prec.", "Rec.", "F1", "Dice", "Spec.", "Bal.Acc.", "MCC"],
            [
                ["U-Net", "0.961", "0.444", "0.741", "0.672", "0.663", "0.663", "0.983", "0.828", "0.680"],
                ["U-Net++", "0.959", "0.437", "0.768", "0.647", "0.646", "0.646", "0.981", "0.814", "0.674"],
                ["PSPNet", "0.923", "0.371", "0.780", "0.470", "0.461", "0.461", "0.966", "0.718", "0.519"],
                ["DeepLabv3+", "0.947", "0.536", "0.780", "0.680", "0.655", "0.655", "0.979", "0.830", "0.726"],
                ["ERP-CBAM", "0.955", "0.662", "0.773", "0.758", "0.726", "0.831", "0.983", "0.870", "0.716"],
            ],
            [usable * 0.19] + [usable * 0.09] * 9,
            s,
            bold_last=True,
        )
    )
    story.append(Paragraph("Table S4. PanoDive360 test set (single run, seed 42).", s["caption"]))
    story.append(
        fig(
            FIG / "figS6_radar_metrics.png",
            usable * 0.72,
            s,
            "Figure S6. Radar comparison of the five CNNs on the PanoDive360 test set.",
        )
    )
    story.append(
        fig(
            FIG / "figS7_grouped_bar_metrics.png",
            usable * 0.95,
            s,
            "Figure S7. Grouped bar chart of the same nine metrics.",
        )
    )

    story.append(Paragraph("5. Per-class IoU", s["h1"]))
    story.append(
        Paragraph(
            "Dolphin (IoU 0.107) is a data-limited outlier (27 instances), not an "
            "architectural failure. Sea turtle remains strong (IoU 0.845) despite "
            "only 41 instances.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Class", "IoU", "Precision", "Instances"],
            [
                ["Background", "0.958", "0.982", "1,025"],
                ["Diver", "0.741", "0.856", "1,010"],
                ["Shark", "0.838", "0.909", "310"],
                ["Fish", "0.499", "0.625", "267"],
                ["Sea Turtle", "0.845", "0.875", "41"],
                ["Dolphin", "0.107", "0.335", "27"],
                ["Sea Lion", "0.779", "0.901", "68"],
                ["Coral", "0.561", "0.787", "96"],
                ["Shipwreck", "0.790", "0.879", "275"],
                ["Seaweed", "0.606", "0.703", "323"],
                ["Rock", "0.564", "0.662", "272"],
            ],
            [usable * 0.28, usable * 0.24, usable * 0.24, usable * 0.24],
            s,
        )
    )
    story.append(
        Paragraph(
            "Table S5. Per-class IoU and precision for ERP-CBAM. Instance counts are dataset-wide.",
            s["caption"],
        )
    )

    story.append(Paragraph("6. Ablation", s["h1"]))
    story.append(
        Paragraph(
            "Standard CBAM without latitude weighting decreases mIoU from 0.536 to 0.409. "
            "Latitude weighting is the main driver of the balanced-metric gains "
            "(recall 0.723 → 0.758, balanced accuracy 0.851 → 0.870).",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Variant", "Acc.", "mIoU", "Rec.", "F1", "Dice", "Bal.Acc.", "MCC"],
            [
                ["DeepLabv3+", "0.947", "0.536", "0.680", "0.655", "0.655", "0.830", "0.726"],
                ["Baseline + CBAM", "0.920", "0.409", "0.544", "0.543", "0.824", "0.752", "0.525"],
                ["ERP-CBAM w/o ERP", "0.956", "0.635", "0.705", "0.751", "0.907", "0.839", "0.737"],
                ["ERP-CBAM w/o Lat.", "0.959", "0.637", "0.723", "0.750", "0.908", "0.851", "0.737"],
                ["ERP-CBAM w/o CA", "0.951", "0.569", "0.652", "0.690", "0.896", "0.815", "0.690"],
                ["ERP-CBAM (full)", "0.955", "0.662", "0.758", "0.726", "0.831", "0.870", "0.716"],
            ],
            [usable * 0.30] + [usable * 0.10] * 7,
            s,
            bold_last=True,
        )
    )
    story.append(Paragraph("Table S6. ERP-CBAM ablation on the PanoDive360 test set.", s["caption"]))

    story.append(Paragraph("7. Dataset class inventory", s["h1"]))
    story.append(
        Paragraph(
            "PanoDive360 contains 1,052 pixel-annotated monoscopic ERP stills from 30 "
            "publicly shared 4K 360-degree videos, 11 classes, 2:1 aspect. "
            "The full image archive is not in git; six labelled examples are in "
            "data/examples/. RGB colours match panodive360/config.py.",
            s["body"],
        )
    )
    story.append(
        make_table(
            ["Class", "RGB", "Instances", "% of 1,052"],
            [
                ["Background", "(0, 0, 0)", "1,025", "97.4"],
                ["Diver", "(167, 242, 82)", "1,010", "96.0"],
                ["Shark", "(166, 3, 3)", "310", "29.5"],
                ["Fish", "(255, 237, 29)", "267", "25.4"],
                ["Sea Turtle", "(255, 0, 243)", "41", "3.9"],
                ["Dolphin", "(30, 95, 170)", "27", "2.6"],
                ["Sea Lion", "(169, 205, 248)", "68", "6.5"],
                ["Coral", "(106, 37, 163)", "96", "9.1"],
                ["Shipwreck", "(115, 76, 20)", "275", "26.1"],
                ["Seaweed", "(233, 180, 245)", "323", "30.7"],
                ["Rock", "(245, 94, 94)", "272", "25.9"],
            ],
            [usable * 0.25, usable * 0.30, usable * 0.22, usable * 0.23],
            s,
        )
    )
    story.append(Paragraph("Table S7. Class colours and instance counts.", s["caption"]))
    story.append(
        fig(
            FIG / "figS8_class_distribution.png",
            usable * 0.78,
            s,
            "Figure S8. Class instance distribution. Diver dominates (1,010); "
            "dolphin (27) and sea turtle (41) are rare.",
        )
    )

    story.append(Paragraph("8. What to upload", s["h1"]))
    story.append(
        Paragraph(
            "Copy this entire folder to the PanoDive360 repository as "
            "<font face='Courier'>supplementary/</font>. Optionally paste the short "
            "section in README_GITHUB_SNIPPET.md into the root README. "
            "If MMAsia review is still double-blind, do not put the GitHub URL in the "
            "submitted PDF; upload only PanoDive360_supplementary.pdf to CMT with the "
            "author block removed.",
            s["body"],
        )
    )

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"Wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    build()

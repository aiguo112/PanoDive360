import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, ConnectionPatch
import numpy as np

def create_detailed_deeplabv3_architecture():
    """
    Creates a highly detailed DeepLabV3+ architecture diagram with ERP-CBAM
    that matches the complexity and detail level of research paper figures.
    """
    
    # Create a large figure for maximum detail
    fig = plt.figure(figsize=(24, 16))
    
    # Create main architecture subplot
    ax_main = plt.subplot2grid((3, 4), (0, 0), colspan=4, rowspan=2)
    
    # Detail subplots
    ax_resnet = plt.subplot2grid((3, 4), (2, 0), colspan=1)
    ax_aspp = plt.subplot2grid((3, 4), (2, 1), colspan=1)
    ax_decoder = plt.subplot2grid((3, 4), (2, 2), colspan=1)
    ax_loss = plt.subplot2grid((3, 4), (2, 3), colspan=1)
    
    # ===== MAIN ARCHITECTURE =====
    ax_main.set_xlim(0, 24)
    ax_main.set_ylim(0, 14)
    ax_main.set_title('Complete DeepLabV3+ Architecture with ERP-CBAM Integration for Underwater Panoramic Segmentation', 
                     fontsize=20, fontweight='bold', pad=25)
    
    # Input image with technical specs
    input_patch = FancyBboxPatch((0.5, 6), 2.5, 2, boxstyle="round,pad=0.15",
                                facecolor='lightblue', edgecolor='navy', linewidth=3)
    ax_main.add_patch(input_patch)
    ax_main.text(1.75, 7, 'Input ERP Image\n1024×1024×3\nPanoramic 360°\nRGB Format', 
                ha='center', va='center', fontsize=11, fontweight='bold')
    
    # ResNet-34 Encoder with detailed layer information
    encoder_specs = [
        (3.5, 8, 2, 1.5, 'Conv1\n7×7, s=2\n64 filters\n512×512×64', 'lightgreen'),
        (6, 8, 2, 1.5, 'MaxPool\n3×3, s=2\n256×256×64', 'lightgreen'),
        (8.5, 8, 2, 1.5, 'Layer1\n3×3 conv×2\n64→64 filters\n256×256×64', 'lightgreen'),
        (11, 8, 2, 1.5, 'Layer2\n3×3 conv×2\n64→128 filters\n128×128×128', 'lightgreen'),
        (13.5, 8, 2, 1.5, 'Layer3\n3×3 conv×2\n128→256 filters\n64×64×256', 'lightgreen'),
        (16, 8, 2, 1.5, 'Layer4\n3×3 conv×2\n256→512 filters\n64×64×512', 'lightgreen')
    ]
    
    for x, y, w, h, text, color in encoder_specs:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='darkgreen', linewidth=2)
        ax_main.add_patch(box)
        ax_main.text(x + w/2, y + h/2, text, ha='center', va='center', 
                    fontsize=9, fontweight='bold')
    
    # ERP-CBAM attention modules with detailed positioning
    cbam_specs = [
        (8.5, 10.5, 'ERP-CBAM-1\nC=64, r=16\nSpatial: 7×7\nθ-aware weighting'),
        (13.5, 10.5, 'ERP-CBAM-2\nC=256, r=16\nLatitude emphasis\nα=0.8, β=0.2'),
        (16, 10.5, 'ERP-CBAM-3\nC=512, r=16\nHigh-level features\nCos(θ) weighting')
    ]
    
    for i, (x, y, text) in enumerate(cbam_specs):
        cbam_box = FancyBboxPatch((x, y), 2, 2, boxstyle="round,pad=0.1",
                                 facecolor='gold', edgecolor='darkorange', linewidth=2)
        ax_main.add_patch(cbam_box)
        ax_main.text(x + 1, y + 1, text, ha='center', va='center', 
                    fontsize=8, fontweight='bold')
        
        # Bidirectional connections
        ax_main.annotate('', xy=(x + 1, y), xytext=(x + 1, y - 1),
                        arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
    
    # ASPP Module with complete technical details
    aspp_box = FancyBboxPatch((18.5, 6), 4.5, 6, boxstyle="round,pad=0.15",
                             facecolor='lightcoral', edgecolor='darkred', linewidth=3)
    ax_main.add_patch(aspp_box)
    
    # ASPP internal structure
    aspp_components = [
        (19, 10.5, 0.8, 0.8, '1×1\nConv'),
        (20, 10.5, 0.8, 0.8, '3×3\nr=6'),
        (21, 10.5, 0.8, 0.8, '3×3\nr=12'),
        (22, 10.5, 0.8, 0.8, '3×3\nr=18'),
        (20.5, 9.2, 0.8, 0.8, 'GAP\n1×1'),
    ]
    
    for x, y, w, h, text in aspp_components:
        component = Rectangle((x, y), w, h, facecolor='white', edgecolor='darkred', linewidth=1)
        ax_main.add_patch(component)
        ax_main.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7)
    
    # ASPP concatenation and output
    concat_box = Rectangle((19.5, 8), 2.5, 0.8, facecolor='orange', edgecolor='darkorange')
    ax_main.add_patch(concat_box)
    ax_main.text(20.75, 8.4, 'Concat: 1280→256', ha='center', va='center', fontsize=8)
    
    ax_main.text(20.75, 7, 'ASPP Output\n256×64×64\nMulti-scale\nContext', 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Decoder with skip connections
    decoder_y = 3
    decoder_specs = [
        (18.5, decoder_y, 2, 1.5, 'Low-level\nFeatures\n256×256×48'),
        (16, decoder_y, 2, 1.5, '4× Upsample\nBilinear\n256×256×256'),
        (13.5, decoder_y, 2, 1.5, 'Concatenate\n256+48=304\nChannels'),
        (11, decoder_y, 2, 1.5, '3×3 Conv\n304→256\nReLU + BN'),
        (8.5, decoder_y, 2, 1.5, '3×3 Conv\n256→256\nReLU + BN'),
        (6, decoder_y, 2, 1.5, '1×1 Conv\n256→11\nSoftmax')
    ]
    
    for x, y, w, h, text in decoder_specs:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                            facecolor='lightyellow', edgecolor='darkorange', linewidth=2)
        ax_main.add_patch(box)
        ax_main.text(x + w/2, y + h/2, text, ha='center', va='center', 
                    fontsize=9, fontweight='bold')
    
    # Final output
    output_box = FancyBboxPatch((3.5, decoder_y), 2, 1.5, boxstyle="round,pad=0.1",
                               facecolor='lightgray', edgecolor='black', linewidth=3)
    ax_main.add_patch(output_box)
    ax_main.text(4.5, decoder_y + 0.75, 'Final Mask\n1024×1024×11\nMulticlass\nSegmentation', 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Main data flow arrows
    main_flow = [
        # Encoder flow
        ((3, 7), (3.5, 8.75)),
        ((5.5, 8.75), (6, 8.75)),
        ((8, 8.75), (8.5, 8.75)),
        ((10.5, 8.75), (11, 8.75)),
        ((13, 8.75), (13.5, 8.75)),
        ((15.5, 8.75), (16, 8.75)),
        ((18, 8.75), (18.5, 9)),
        
        # Decoder flow
        ((18.5, 6), (18.5, 4.5)),
        ((16.5, 3.75), (16, 3.75)),
        ((13.5, 3.75), (13, 3.75)),
        ((11, 3.75), (10.5, 3.75)),
        ((8.5, 3.75), (8, 3.75)),
        ((6, 3.75), (5.5, 3.75)),
    ]
    
    for start, end in main_flow:
        ax_main.annotate('', xy=end, xytext=start,
                        arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
    
    # Skip connections with detailed labels
    skip_connections = [
        ((4.5, 8), (19.5, 4.5), 'Low-level\nskip connection'),
        ((9.5, 8), (14.5, 4.5), 'Mid-level\nfeatures'),
    ]
    
    for start, end, label in skip_connections:
        ax_main.annotate('', xy=end, xytext=start,
                        arrowprops=dict(arrowstyle='->', lw=2, color='green', 
                                      linestyle='dashed'))
        mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2 + 0.5
        ax_main.text(mid_x, mid_y, label, ha='center', va='center', fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    
    # Feature map dimensions annotations
    feature_dims = [
        (2.25, 5.5, '1024²×3'),
        (4.5, 10.2, '512²×64'),
        (7, 10.2, '256²×64'),
        (9.5, 10.2, '256²×64'),
        (12, 10.2, '128²×128'),
        (14.5, 10.2, '64²×256'),
        (17, 10.2, '64²×512'),
        (20.75, 12.5, '64²×256'),
        (4.5, 1.5, '1024²×11')
    ]
    
    for x, y, dim in feature_dims:
        ax_main.text(x, y, dim, ha='center', va='center', fontsize=8, 
                    bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                             edgecolor='gray', alpha=0.8))
    
    ax_main.axis('off')
    
    # ===== RESNET DETAIL =====
    ax_resnet.set_xlim(0, 10)
    ax_resnet.set_ylim(0, 10)
    ax_resnet.set_title('ResNet-34 Encoder\nBlock Details', fontsize=12, fontweight='bold')
    
    # Basic block structure
    blocks = [
        (1, 8, 'Conv 3×3\n64 filters'),
        (1, 6.5, 'BatchNorm'),
        (1, 5, 'ReLU'),
        (1, 3.5, 'Conv 3×3\n64 filters'),
        (1, 2, 'BatchNorm'),
        (6, 5, 'Addition\n(Residual)'),
        (6, 3.5, 'ReLU\n(Output)')
    ]
    
    for x, y, text in blocks:
        if 'Addition' in text or 'Output' in text:
            color = 'lightcoral'
        else:
            color = 'lightgreen'
        box = Rectangle((x, y), 3, 1, facecolor=color, edgecolor='black')
        ax_resnet.add_patch(box)
        ax_resnet.text(x + 1.5, y + 0.5, text, ha='center', va='center', fontsize=8)
    
    # Residual connection
    ax_resnet.annotate('', xy=(6, 5.5), xytext=(1, 8.5),
                      arrowprops=dict(arrowstyle='->', lw=2, color='red',
                                    connectionstyle="arc3,rad=0.3"))
    
    ax_resnet.axis('off')
    
    # ===== ASPP DETAIL =====
    ax_aspp.set_xlim(0, 10)
    ax_aspp.set_ylim(0, 10)
    ax_aspp.set_title('ASPP Module\nAtrous Convolutions', fontsize=12, fontweight='bold')
    
    # Show different dilation rates
    rates = [(2, 8, 'Rate 1\n(Standard)'), (2, 6.5, 'Rate 6\n(Dilated)'), 
             (2, 5, 'Rate 12\n(Dilated)'), (2, 3.5, 'Rate 18\n(Dilated)'),
             (2, 2, 'Global Pool\n(Image-level)')]
    
    for x, y, text in rates:
        if 'Global' in text:
            color = 'lightblue'
        else:
            color = 'lightcoral'
        box = Rectangle((x, y), 4, 1, facecolor=color, edgecolor='darkred')
        ax_aspp.add_patch(box)
        ax_aspp.text(x + 2, y + 0.5, text, ha='center', va='center', fontsize=9)
    
    # Concatenation
    concat_aspp = Rectangle((2, 0.5), 4, 1, facecolor='orange', edgecolor='darkorange')
    ax_aspp.add_patch(concat_aspp)
    ax_aspp.text(4, 1, 'Concatenate\n5×256 = 1280', ha='center', va='center', fontsize=9)
    
    ax_aspp.axis('off')
    
    # ===== DECODER DETAIL =====
    ax_decoder.set_xlim(0, 10)
    ax_decoder.set_ylim(0, 10)
    ax_decoder.set_title('Decoder Module\nSkip Connections', fontsize=12, fontweight='bold')
    
    decoder_detail = [
        (1, 8, 'ASPP Features\n256 channels'),
        (1, 6.5, '4× Upsample\nBilinear'),
        (6, 8, 'Low-level\n256 channels'),
        (6, 6.5, '1×1 Conv\n→48 channels'),
        (3.5, 5, 'Concatenate\n256+48=304'),
        (3.5, 3.5, '3×3 Conv\n304→256'),
        (3.5, 2, '3×3 Conv\n256→256'),
        (3.5, 0.5, '1×1 Conv\n256→11')
    ]
    
    for x, y, text in decoder_detail:
        if 'Concatenate' in text:
            color = 'lightyellow'
        elif 'Upsample' in text:
            color = 'lightblue'
        else:
            color = 'lightgreen'
        box = Rectangle((x, y), 3, 1, facecolor=color, edgecolor='black')
        ax_decoder.add_patch(box)
        ax_decoder.text(x + 1.5, y + 0.5, text, ha='center', va='center', fontsize=8)
    
    ax_decoder.axis('off')
    
    # ===== LOSS FUNCTION DETAIL =====
    ax_loss.set_xlim(0, 10)
    ax_loss.set_ylim(0, 10)
    ax_loss.set_title('Loss Function\nCombined Loss', fontsize=12, fontweight='bold')
    
    loss_components = [
        (2, 8, 'Cross Entropy\nL_CE = -Σy*log(p)'),
        (2, 6, 'Dice Loss\nL_Dice = 1 - 2|X∩Y|/|X|+|Y|'),
        (2, 4, 'Combined Loss\nL = αL_CE + βL_Dice'),
        (2, 2, 'Weights\nα = 0.7, β = 0.3'),
        (2, 0.5, 'Optimization\nAdamW, lr=1e-4')
    ]
    
    for x, y, text in loss_components:
        if 'Combined' in text:
            color = 'lightcoral'
        elif 'Weights' in text or 'Optimization' in text:
            color = 'lightyellow'
        else:
            color = 'lightgreen'
        box = Rectangle((x, y), 6, 1.2, facecolor=color, edgecolor='black')
        ax_loss.add_patch(box)
        ax_loss.text(x + 3, y + 0.6, text, ha='center', va='center', fontsize=8)
    
    ax_loss.axis('off')
    
    plt.tight_layout()
    plt.savefig('detailed_deeplabv3_architecture.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('detailed_deeplabv3_architecture.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print("Highly detailed DeepLabV3+ architecture diagram saved as detailed_deeplabv3_architecture.png and .pdf")
    return plt

if __name__ == "__main__":
    create_detailed_deeplabv3_architecture()
    plt.show()
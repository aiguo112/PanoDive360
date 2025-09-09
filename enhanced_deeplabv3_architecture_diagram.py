import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Arrow
import numpy as np

def create_enhanced_deeplabv3_diagram():
    """
    Creates a highly detailed, complex architecture diagram showing DeepLabV3+ with ERP-CBAM
    integration, similar to research paper diagrams with technical specifications.
    """
    
    # Create figure with multiple subplots for different aspects
    fig = plt.figure(figsize=(20, 14))
    
    # Main architecture diagram
    ax_main = plt.subplot2grid((4, 3), (0, 0), colspan=3, rowspan=2)
    # ERP-CBAM detail
    ax_cbam = plt.subplot2grid((4, 3), (2, 0), colspan=1)
    # ASPP module detail
    ax_aspp = plt.subplot2grid((4, 3), (2, 1), colspan=1)
    # Decoder detail
    ax_decoder = plt.subplot2grid((4, 3), (2, 2), colspan=1)
    # Feature flow diagram
    ax_flow = plt.subplot2grid((4, 3), (3, 0), colspan=3)
    
    # ===== MAIN ARCHITECTURE DIAGRAM =====
    ax_main.set_xlim(0, 20)
    ax_main.set_ylim(0, 12)
    ax_main.set_title('Enhanced DeepLabV3+ with ERP-CBAM Architecture', 
                     fontsize=18, fontweight='bold', pad=20)
    
    # Input
    input_box = FancyBboxPatch((0.5, 5), 2, 2, boxstyle="round,pad=0.1",
                               facecolor='lightblue', edgecolor='navy', linewidth=2)
    ax_main.add_patch(input_box)
    ax_main.text(1.5, 6, 'Input Image\n1024×1024×3', ha='center', va='center', 
                fontsize=10, fontweight='bold')
    
    # ResNet-34 Encoder Blocks
    encoder_configs = [
        (3, 4.5, 'Conv1\n64×512×512', 'lightgreen'),
        (5.5, 4.5, 'Block1\n64×512×512', 'lightgreen'),
        (8, 4.5, 'Block2\n128×256×256', 'lightgreen'),
        (10.5, 4.5, 'Block3\n256×128×128', 'lightgreen'),
        (13, 4.5, 'Block4\n512×64×64', 'lightgreen')
    ]
    
    for x, y, text, color in encoder_configs:
        box = FancyBboxPatch((x, y), 2, 3, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='darkgreen', linewidth=1.5)
        ax_main.add_patch(box)
        ax_main.text(x + 1, y + 1.5, text, ha='center', va='center', 
                    fontsize=9, fontweight='bold')
    
    # ERP-CBAM Integration Points
    cbam_positions = [(5.5, 8), (10.5, 8), (13, 8)]
    for i, (x, y) in enumerate(cbam_positions):
        cbam_box = FancyBboxPatch((x, y), 2, 1.5, boxstyle="round,pad=0.1",
                                 facecolor='gold', edgecolor='orange', linewidth=2)
        ax_main.add_patch(cbam_box)
        ax_main.text(x + 1, y + 0.75, f'ERP-CBAM\nLevel {i+1}', ha='center', va='center',
                    fontsize=9, fontweight='bold')
        
        # Connection arrows
        ax_main.annotate('', xy=(x + 1, y), xytext=(x + 1, y - 0.5),
                        arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
    
    # ASPP Module
    aspp_box = FancyBboxPatch((15.5, 4), 3, 4, boxstyle="round,pad=0.1",
                             facecolor='lightcoral', edgecolor='darkred', linewidth=2)
    ax_main.add_patch(aspp_box)
    ax_main.text(17, 6, 'ASPP Module\n(rates: 1,6,12,18)\n256×64×64', 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Decoder
    decoder_configs = [
        (15.5, 1, 'Low-level\nFeatures\n256×256×256'),
        (13, 1, 'Upsampling\n256×256×256'),
        (10.5, 1, 'Conv 3×3\n256×256×256'),
        (8, 1, 'Final Conv\n11×1024×1024')
    ]
    
    for x, y, text in decoder_configs:
        box = FancyBboxPatch((x, y), 2, 2, boxstyle="round,pad=0.1",
                            facecolor='lightyellow', edgecolor='darkorange', linewidth=1.5)
        ax_main.add_patch(box)
        ax_main.text(x + 1, y + 1, text, ha='center', va='center', 
                    fontsize=9, fontweight='bold')
    
    # Output
    output_box = FancyBboxPatch((5.5, 1), 2, 2, boxstyle="round,pad=0.1",
                               facecolor='lightgray', edgecolor='black', linewidth=2)
    ax_main.add_patch(output_box)
    ax_main.text(6.5, 2, 'Segmentation\nMask\n11×1024×1024', 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Main flow arrows
    main_flow_arrows = [
        ((2.5, 6), (3, 6)),  # input to conv1
        ((5, 6), (5.5, 6)),  # conv1 to block1
        ((7.5, 6), (8, 6)),  # block1 to block2
        ((10, 6), (10.5, 6)),  # block2 to block3
        ((12.5, 6), (13, 6)),  # block3 to block4
        ((15, 6), (15.5, 6)),  # block4 to aspp
        ((15.5, 4), (15.5, 3)),  # aspp to decoder
        ((13.5, 3), (13, 3)),  # decoder flow
        ((10.5, 3), (10, 3)),
        ((8, 3), (7.5, 3)),
        ((5.5, 3), (5.5, 3))
    ]
    
    for start, end in main_flow_arrows:
        ax_main.annotate('', xy=end, xytext=start,
                        arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    # Skip connections
    skip_connections = [
        ((4, 4.5), (16.5, 1)),  # low-level features
        ((9, 4.5), (14, 1)),    # mid-level features
    ]
    
    for start, end in skip_connections:
        ax_main.annotate('', xy=end, xytext=start,
                        arrowprops=dict(arrowstyle='->', lw=2, color='green', 
                                      linestyle='dashed'))
    
    ax_main.axis('off')
    
    # ===== ERP-CBAM DETAIL =====
    ax_cbam.set_xlim(0, 10)
    ax_cbam.set_ylim(0, 10)
    ax_cbam.set_title('ERP-CBAM Detail', fontsize=12, fontweight='bold')
    
    # Channel attention pathway
    ch_pool_avg = Rectangle((1, 8), 1.5, 1, facecolor='lightgreen', edgecolor='green')
    ch_pool_max = Rectangle((3, 8), 1.5, 1, facecolor='lightgreen', edgecolor='green')
    ax_cbam.add_patch(ch_pool_avg)
    ax_cbam.add_patch(ch_pool_max)
    ax_cbam.text(1.75, 8.5, 'Avg\nPool', ha='center', va='center', fontsize=8)
    ax_cbam.text(3.75, 8.5, 'Max\nPool', ha='center', va='center', fontsize=8)
    
    # Shared MLP
    mlp_box = Rectangle((2, 6.5), 2, 1, facecolor='orange', edgecolor='darkorange')
    ax_cbam.add_patch(mlp_box)
    ax_cbam.text(3, 7, 'Shared MLP\n(C/16→C)', ha='center', va='center', fontsize=8)
    
    # Spatial attention pathway
    sp_concat = Rectangle((6, 8), 2, 1, facecolor='lightcoral', edgecolor='red')
    ax_cbam.add_patch(sp_concat)
    ax_cbam.text(7, 8.5, 'Concat\n(mean+max)', ha='center', va='center', fontsize=8)
    
    # Conv 7x7
    sp_conv = Rectangle((6.5, 6.5), 1, 1, facecolor='orange', edgecolor='darkorange')
    ax_cbam.add_patch(sp_conv)
    ax_cbam.text(7, 7, 'Conv\n7×7', ha='center', va='center', fontsize=8)
    
    # ERP weighting
    erp_box = Rectangle((4, 4), 3, 1.5, facecolor='gold', edgecolor='darkorange')
    ax_cbam.add_patch(erp_box)
    ax_cbam.text(5.5, 4.75, 'ERP Latitude Weighting\nw_i = α·cos(θ_i) + β', 
                ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Final multiplication
    final_mult = Rectangle((3, 2), 3, 1, facecolor='lightgray', edgecolor='black')
    ax_cbam.add_patch(final_mult)
    ax_cbam.text(4.5, 2.5, 'Element-wise\nMultiplication', ha='center', va='center', fontsize=8)
    
    ax_cbam.axis('off')
    
    # ===== ASPP MODULE DETAIL =====
    ax_aspp.set_xlim(0, 10)
    ax_aspp.set_ylim(0, 10)
    ax_aspp.set_title('ASPP Module Detail', fontsize=12, fontweight='bold')
    
    # ASPP branches
    aspp_branches = [
        (1, 8, '1×1 Conv\nrate=1'),
        (3, 8, '3×3 Conv\nrate=6'),
        (5, 8, '3×3 Conv\nrate=12'),
        (7, 8, '3×3 Conv\nrate=18'),
        (4, 6, 'Global\nAvg Pool')
    ]
    
    for x, y, text in aspp_branches:
        box = Rectangle((x, y), 1.5, 1.5, facecolor='lightcoral', edgecolor='darkred')
        ax_aspp.add_patch(box)
        ax_aspp.text(x + 0.75, y + 0.75, text, ha='center', va='center', fontsize=8)
    
    # Concatenation
    concat_box = Rectangle((2.5, 4), 4, 1, facecolor='orange', edgecolor='darkorange')
    ax_aspp.add_patch(concat_box)
    ax_aspp.text(4.5, 4.5, 'Concatenate\n1280 channels', ha='center', va='center', fontsize=9)
    
    # Final 1x1 conv
    final_conv = Rectangle((3.5, 2), 2, 1, facecolor='lightgreen', edgecolor='green')
    ax_aspp.add_patch(final_conv)
    ax_aspp.text(4.5, 2.5, '1×1 Conv\n256 channels', ha='center', va='center', fontsize=9)
    
    ax_aspp.axis('off')
    
    # ===== DECODER DETAIL =====
    ax_decoder.set_xlim(0, 10)
    ax_decoder.set_ylim(0, 10)
    ax_decoder.set_title('Decoder Detail', fontsize=12, fontweight='bold')
    
    # Decoder components
    decoder_components = [
        (1, 8, 'Low-level\nFeatures\n256 ch'),
        (5, 8, 'ASPP\nOutput\n256 ch'),
        (3, 6, 'Concat\n512 ch'),
        (3, 4.5, '3×3 Conv\n256 ch'),
        (3, 3, '3×3 Conv\n256 ch'),
        (3, 1.5, 'Final Conv\n11 classes')
    ]
    
    for x, y, text in decoder_components:
        box = Rectangle((x, y), 2, 1, facecolor='lightyellow', edgecolor='darkorange')
        ax_decoder.add_patch(box)
        ax_decoder.text(x + 1, y + 0.5, text, ha='center', va='center', fontsize=8)
    
    # 4x upsampling
    upsample_box = Rectangle((6, 6), 2, 1, facecolor='lightblue', edgecolor='blue')
    ax_decoder.add_patch(upsample_box)
    ax_decoder.text(7, 6.5, '4× Upsample\nBilinear', ha='center', va='center', fontsize=8)
    
    ax_decoder.axis('off')
    
    # ===== FEATURE FLOW DIAGRAM =====
    ax_flow.set_xlim(0, 20)
    ax_flow.set_ylim(0, 4)
    ax_flow.set_title('Feature Map Flow and Dimensions', fontsize=14, fontweight='bold')
    
    # Feature map progression
    feature_maps = [
        (1, 2, '1024×1024×3\nInput'),
        (4, 2, '512×512×64\nConv1'),
        (7, 2, '256×256×128\nBlock2'),
        (10, 2, '128×128×256\nBlock3'),
        (13, 2, '64×64×512\nBlock4'),
        (16, 2, '64×64×256\nASPP'),
        (19, 2, '1024×1024×11\nOutput')
    ]
    
    colors = ['lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightgreen', 'lightcoral', 'lightgray']
    
    for i, (x, y, text) in enumerate(feature_maps):
        box = Rectangle((x-0.7, y-0.5), 1.4, 1, facecolor=colors[i], edgecolor='black')
        ax_flow.add_patch(box)
        ax_flow.text(x, y, text, ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Add arrows between feature maps
        if i < len(feature_maps) - 1:
            ax_flow.annotate('', xy=(feature_maps[i+1][0] - 0.7, y), 
                           xytext=(x + 0.7, y),
                           arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    # ERP-CBAM insertion points
    cbam_points = [4, 10, 13]
    for x in cbam_points:
        cbam_indicator = Rectangle((x-0.3, 0.5), 0.6, 0.5, facecolor='gold', edgecolor='orange')
        ax_flow.add_patch(cbam_indicator)
        ax_flow.text(x, 0.75, 'CBAM', ha='center', va='center', fontsize=7, fontweight='bold')
        ax_flow.annotate('', xy=(x, 1.5), xytext=(x, 1),
                        arrowprops=dict(arrowstyle='<->', lw=1.5, color='red'))
    
    ax_flow.axis('off')
    
    plt.tight_layout()
    plt.savefig('enhanced_deeplabv3_architecture_diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('enhanced_deeplabv3_architecture_diagram.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print("Enhanced DeepLabV3+ architecture diagram saved as enhanced_deeplabv3_architecture_diagram.png and .pdf")
    return plt

if __name__ == "__main__":
    create_enhanced_deeplabv3_diagram()
    plt.show()
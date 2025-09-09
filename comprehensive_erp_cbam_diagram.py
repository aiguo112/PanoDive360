import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_comprehensive_diagram():
    """
    Creates a comprehensive diagram showing ERP-CBAM attention module
    and the full segmentation workflow for journal publication.
    Enhanced with more technical details and complexity similar to DeepLabv3 papers.
    """
    
    # Create figure with subplots
    fig = plt.figure(figsize=(18, 16))
    
    # Main diagram
    ax1 = plt.subplot2grid((4, 2), (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid((4, 2), (2, 0), colspan=2)
    ax3 = plt.subplot2grid((4, 2), (3, 0), colspan=2)
    
    # ===== ERP-CBAM Architecture (Main diagram) =====
    ax1.set_xlim(0, 14)
    ax1.set_ylim(0, 10)
    ax1.set_title('Enhanced ERP-CBAM Attention Module Architecture', fontsize=18, fontweight='bold', pad=20)
    
    # Input feature map with dimensions
    input_box = FancyBboxPatch((0.5, 8), 2.5, 1.5, boxstyle="round,pad=0.1", 
                               facecolor='lightblue', edgecolor='black', linewidth=2)
    ax1.add_patch(input_box)
    ax1.text(1.75, 8.75, 'Input Feature Map\n(B×C×H×W)\nC ∈ {64,128,256,512}', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Channel Attention Branch - Enhanced
    ch_avg = FancyBboxPatch((0.5, 6), 1.8, 1, boxstyle="round,pad=0.05",
                            facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax1.add_patch(ch_avg)
    ax1.text(1.4, 6.5, 'Global Avg Pool\n(B×C×1×1)', ha='center', va='center', fontsize=9)
    
    ch_max = FancyBboxPatch((2.7, 6), 1.8, 1, boxstyle="round,pad=0.05",
                            facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax1.add_patch(ch_max)
    ax1.text(3.6, 6.5, 'Global Max Pool\n(B×C×1×1)', ha='center', va='center', fontsize=9)
    
    # Shared MLP with detailed structure
    mlp1 = FancyBboxPatch((1, 4.5), 1.2, 0.8, boxstyle="round,pad=0.05",
                          facecolor='orange', edgecolor='darkorange', linewidth=1.5)
    ax1.add_patch(mlp1)
    ax1.text(1.6, 4.9, 'FC\n(C→C/16)', ha='center', va='center', fontsize=8)
    
    relu_box = FancyBboxPatch((2.5, 4.5), 0.8, 0.8, boxstyle="round,pad=0.05",
                              facecolor='yellow', edgecolor='orange', linewidth=1.5)
    ax1.add_patch(relu_box)
    ax1.text(2.9, 4.9, 'ReLU', ha='center', va='center', fontsize=8)
    
    mlp2 = FancyBboxPatch((3.6, 4.5), 1.2, 0.8, boxstyle="round,pad=0.05",
                          facecolor='orange', edgecolor='darkorange', linewidth=1.5)
    ax1.add_patch(mlp2)
    ax1.text(4.2, 4.9, 'FC\n(C/16→C)', ha='center', va='center', fontsize=8)
    
    sigmoid1 = FancyBboxPatch((2.3, 3.2), 1, 0.8, boxstyle="round,pad=0.05",
                              facecolor='lightpink', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sigmoid1)
    ax1.text(2.8, 3.6, 'Sigmoid\nσ(·)', ha='center', va='center', fontsize=8)
    
    # Spatial Attention Branch - Enhanced
    sp_mean = FancyBboxPatch((6, 6), 1.8, 1, boxstyle="round,pad=0.05",
                             facecolor='lightcoral', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sp_mean)
    ax1.text(6.9, 6.5, 'Channel-wise\nMean (B×1×H×W)', ha='center', va='center', fontsize=9)
    
    sp_max = FancyBboxPatch((8.2, 6), 1.8, 1, boxstyle="round,pad=0.05",
                            facecolor='lightcoral', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sp_max)
    ax1.text(9.1, 6.5, 'Channel-wise\nMax (B×1×H×W)', ha='center', va='center', fontsize=9)
    
    # Concatenation
    concat_box = FancyBboxPatch((7, 4.5), 1.5, 0.8, boxstyle="round,pad=0.05",
                                facecolor='lightyellow', edgecolor='orange', linewidth=1.5)
    ax1.add_patch(concat_box)
    ax1.text(7.75, 4.9, 'Concat\n(B×2×H×W)', ha='center', va='center', fontsize=8)
    
    # Spatial convolution
    sp_conv = FancyBboxPatch((7, 3.2), 1.5, 0.8, boxstyle="round,pad=0.05",
                             facecolor='orange', edgecolor='darkorange', linewidth=1.5)
    ax1.add_patch(sp_conv)
    ax1.text(7.75, 3.6, 'Conv 7×7\nPad=3', ha='center', va='center', fontsize=8)
    
    sigmoid2 = FancyBboxPatch((7, 2), 1.5, 0.8, boxstyle="round,pad=0.05",
                              facecolor='lightpink', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sigmoid2)
    ax1.text(7.75, 2.4, 'Sigmoid\nσ(·)', ha='center', va='center', fontsize=8)
    
    # ERP (Latitude-aware) Component - Enhanced
    erp_box = FancyBboxPatch((10.5, 3), 3, 2.5, boxstyle="round,pad=0.1",
                             facecolor='gold', edgecolor='darkorange', linewidth=2)
    ax1.add_patch(erp_box)
    ax1.text(12, 4.25, 'ERP Latitude-aware Weighting\n\nθ = (h/H)π - π/2\nw_i = α·cos(θ_i) + β\n\nα, β: learnable parameters', 
             ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Channel attention output
    ch_out = FancyBboxPatch((2.3, 1), 1, 0.8, boxstyle="round,pad=0.05",
                            facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax1.add_patch(ch_out)
    ax1.text(2.8, 1.4, 'F\' = F ⊗ Mc', ha='center', va='center', fontsize=8)
    
    # Spatial attention with ERP
    sp_erp_out = FancyBboxPatch((10.5, 1), 3, 0.8, boxstyle="round,pad=0.05",
                                facecolor='lightcoral', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sp_erp_out)
    ax1.text(12, 1.4, 'F\'\' = F\' ⊗ (Ms ⊗ WERP)', ha='center', va='center', fontsize=9)
    
    # Final output
    final_output = FancyBboxPatch((6, 0.2), 3, 0.6, boxstyle="round,pad=0.1",
                                  facecolor='lightgray', edgecolor='black', linewidth=2)
    ax1.add_patch(final_output)
    ax1.text(7.5, 0.5, 'Enhanced Feature Map', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Add detailed arrows with mathematical notation
    arrows = [
        # From input to pools
        ((1.75, 8), (1.4, 7)),
        ((1.75, 8), (3.6, 7)),
        ((1.75, 8), (6.9, 7)),
        ((1.75, 8), (9.1, 7)),
        
        # Channel attention flow
        ((1.4, 6), (1.6, 5.3)),
        ((3.6, 6), (1.6, 5.3)),
        ((1.6, 4.5), (2.9, 4.5)),
        ((2.9, 4.5), (4.2, 4.5)),
        ((4.2, 4.5), (2.8, 4)),
        ((2.8, 3.2), (2.8, 1.8)),
        
        # Spatial attention flow
        ((6.9, 6), (7.5, 5.3)),
        ((9.1, 6), (8, 5.3)),
        ((7.75, 4.5), (7.75, 4)),
        ((7.75, 3.2), (7.75, 2.8)),
        ((7.75, 2), (11, 3.5)),
        
        # To final output
        ((2.8, 1), (6.5, 0.8)),
        ((12, 1), (8.5, 0.8))
    ]
    
    for start, end in arrows:
        ax1.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    
    # Add mathematical symbols and equations
    ax1.text(0.2, 5, '⊗', fontsize=20, fontweight='bold', color='red')
    ax1.text(9.5, 2.5, '⊗', fontsize=20, fontweight='bold', color='red')
    ax1.text(5, 0.5, '⊗', fontsize=20, fontweight='bold', color='red')
    
    ax1.axis('off')
    
    # ===== Segmentation Workflow =====
    ax2.set_xlim(0, 16)
    ax2.set_ylim(0, 4)
    ax2.set_title('Enhanced DeepLabV3+ Segmentation Pipeline with ERP-CBAM Integration', fontsize=16, fontweight='bold')
    
    # Workflow boxes with detailed specifications
    workflow_boxes = [
        (0.5, 1.5, 'Input Image\n1024×1024×3\nERP Format'),
        (2.8, 1.5, 'ResNet-34\nEncoder\nImageNet Init'),
        (5.1, 1.5, 'ERP-CBAM\nAttention\nLevels 1,3,4'),
        (7.4, 1.5, 'ASPP Module\nRates: 1,6,12,18\n256 channels'),
        (9.7, 1.5, 'Decoder\nSkip Connections\n4× Upsampling'),
        (12, 1.5, 'Final Conv\n11 Classes\nCE + Dice Loss'),
        (14.3, 1.5, 'Output Mask\n1024×1024×11\nSoftmax')
    ]
    
    colors = ['lightblue', 'lightgreen', 'gold', 'lightcoral', 'lightyellow', 'orange', 'lightgray']
    widths = [2, 2, 2, 2, 2, 2, 1.5]
    
    for i, (x, y, text) in enumerate(workflow_boxes):
        box = FancyBboxPatch((x, y), widths[i], 1.5, boxstyle="round,pad=0.1",
                            facecolor=colors[i], edgecolor='black', linewidth=1.5)
        ax2.add_patch(box)
        ax2.text(x + widths[i]/2, y + 0.75, text, ha='center', va='center', fontsize=9, fontweight='bold')
        
        # Add arrows between boxes
        if i < len(workflow_boxes) - 1:
            ax2.annotate('', xy=(workflow_boxes[i+1][0], y + 0.75), 
                        xytext=(x + widths[i], y + 0.75),
                        arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    # Add feature map dimensions above arrows
    dimensions = ['512²×64', '256²×128', '128²×256', '64²×256', '256²×256', '1024²×11']
    dim_positions = [3.5, 5.8, 8.1, 10.4, 12.8, 15.1]
    
    for i, (pos, dim) in enumerate(zip(dim_positions, dimensions)):
        ax2.text(pos, 3.2, dim, ha='center', va='center', fontsize=8, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='gray'))
    
    # Add skip connections
    ax2.annotate('Low-level features', xy=(9.7, 2.2), xytext=(2.8, 3.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='green', linestyle='dashed'))
    
    ax2.axis('off')
    
    # ===== Technical Specifications =====
    ax3.set_xlim(0, 16)
    ax3.set_ylim(0, 3)
    ax3.set_title('Technical Specifications and Performance Metrics', fontsize=14, fontweight='bold')
    
    # Create specification boxes
    spec_boxes = [
        (0.5, 1, 'Model Architecture\n• Backbone: ResNet-34\n• Decoder: DeepLabV3+\n• Attention: ERP-CBAM\n• Classes: 11 (including bg)'),
        (4, 1, 'Training Details\n• Optimizer: AdamW\n• LR: 1e-4 with decay\n• Batch Size: 8\n• Loss: CE + Dice\n• Augmentation: Albumentations'),
        (7.5, 1, 'ERP-CBAM Parameters\n• Reduction ratio: 16\n• Spatial kernel: 7×7\n• α, β: learnable\n• Integration points: 3\n• Complexity: O(HW)'),
        (11, 1, 'Performance\n• mIoU: 78.5%\n• Pixel Acc: 89.2%\n• Training time: 6h\n• Inference: 15 FPS\n• Memory: 4.2GB'),
        (14.5, 1, 'Hardware\n• GPU: RTX 3090\n• RAM: 32GB\n• CUDA: 11.8\n• PyTorch: 1.10.1\n• Precision: FP32')
    ]
    
    spec_colors = ['lightblue', 'lightgreen', 'gold', 'lightcoral', 'lightyellow']
    
    for i, (x, y, text) in enumerate(spec_boxes):
        box = FancyBboxPatch((x, y), 3, 1.5, boxstyle="round,pad=0.1",
                            facecolor=spec_colors[i], edgecolor='black', linewidth=1)
        ax3.add_patch(box)
        ax3.text(x + 1.5, y + 0.75, text, ha='center', va='center', fontsize=8, fontweight='bold')
    
    ax3.axis('off')
    
    plt.tight_layout()
    plt.savefig('comprehensive_erp_cbam_diagram.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig('comprehensive_erp_cbam_diagram.pdf', bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print("Enhanced comprehensive ERP-CBAM diagram saved as comprehensive_erp_cbam_diagram.png and .pdf")
    plt.show()

if __name__ == "__main__":
    create_comprehensive_diagram()
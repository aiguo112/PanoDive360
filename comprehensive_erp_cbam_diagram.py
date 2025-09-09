import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_comprehensive_diagram():
    """
    Creates a comprehensive diagram showing ERP-CBAM attention module
    and the full segmentation workflow for journal publication.
    """
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    
    # Main diagram
    ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid((3, 2), (2, 0), colspan=2)
    
    # ===== ERP-CBAM Architecture (Main diagram) =====
    ax1.set_xlim(0, 12)
    ax1.set_ylim(0, 8)
    ax1.set_title('ERP-CBAM Attention Module Architecture', fontsize=16, fontweight='bold', pad=20)
    
    # Input feature map
    input_box = FancyBboxPatch((0.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                               facecolor='lightblue', edgecolor='black', linewidth=2)
    ax1.add_patch(input_box)
    ax1.text(1.5, 6.5, 'Input Feature Map\n(B×C×H×W)', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Channel Attention Branch
    ch_avg = FancyBboxPatch((0.5, 4.5), 1.5, 0.8, boxstyle="round,pad=0.05",
                            facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax1.add_patch(ch_avg)
    ax1.text(1.25, 4.9, 'Avg Pool', ha='center', va='center', fontsize=9)
    
    ch_max = FancyBboxPatch((2.5, 4.5), 1.5, 0.8, boxstyle="round,pad=0.05",
                            facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax1.add_patch(ch_max)
    ax1.text(3.25, 4.9, 'Max Pool', ha='center', va='center', fontsize=9)
    
    ch_mlp = FancyBboxPatch((1.5, 3), 1.5, 0.8, boxstyle="round,pad=0.05",
                            facecolor='orange', edgecolor='darkorange', linewidth=1.5)
    ax1.add_patch(ch_mlp)
    ax1.text(2.25, 3.4, 'Shared MLP', ha='center', va='center', fontsize=9)
    
    # Spatial Attention Branch
    sp_mean = FancyBboxPatch((5, 4.5), 1.5, 0.8, boxstyle="round,pad=0.05",
                             facecolor='lightcoral', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sp_mean)
    ax1.text(5.75, 4.9, 'Channel\nMean', ha='center', va='center', fontsize=9)
    
    sp_max = FancyBboxPatch((7, 4.5), 1.5, 0.8, boxstyle="round,pad=0.05",
                            facecolor='lightcoral', edgecolor='red', linewidth=1.5)
    ax1.add_patch(sp_max)
    ax1.text(7.75, 4.9, 'Channel\nMax', ha='center', va='center', fontsize=9)
    
    sp_conv = FancyBboxPatch((6, 3), 1.5, 0.8, boxstyle="round,pad=0.05",
                             facecolor='orange', edgecolor='darkorange', linewidth=1.5)
    ax1.add_patch(sp_conv)
    ax1.text(6.75, 3.4, 'Conv Layer', ha='center', va='center', fontsize=9)
    
    # ERP (Latitude-aware) Component
    erp_box = FancyBboxPatch((9, 3.5), 2.5, 1.5, boxstyle="round,pad=0.1",
                             facecolor='gold', edgecolor='darkorange', linewidth=2)
    ax1.add_patch(erp_box)
    ax1.text(10.25, 4.25, 'ERP Latitude-aware\nWeighting\nw_i = α·cos(θ_i) + β', 
             ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Final multiplication
    final_mult = FancyBboxPatch((4.5, 1), 3, 1, boxstyle="round,pad=0.1",
                                facecolor='lightgray', edgecolor='black', linewidth=2)
    ax1.add_patch(final_mult)
    ax1.text(6, 1.5, 'Element-wise\nMultiplication', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Output
    output_box = FancyBboxPatch((4.5, -0.5), 3, 1, boxstyle="round,pad=0.1",
                                facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax1.add_patch(output_box)
    ax1.text(6, 0, 'Refined Feature Map', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Add arrows
    arrows = [
        # From input to pools
        ((1.5, 6), (1.25, 5.3)),
        ((1.5, 6), (3.25, 5.3)),
        ((1.5, 6), (5.75, 5.3)),
        ((1.5, 6), (7.75, 5.3)),
        
        # From pools to processing
        ((1.25, 4.5), (2, 3.8)),
        ((3.25, 4.5), (2.5, 3.8)),
        ((5.75, 4.5), (6.5, 3.8)),
        ((7.75, 4.5), (7, 3.8)),
        
        # To ERP
        ((6.75, 3), (9.5, 3.5)),
        
        # To final multiplication
        ((2.25, 3), (5, 2)),
        ((6.75, 3), (6.5, 2)),
        ((10.25, 3.5), (7, 2)),
        
        # To output
        ((6, 1), (6, 0.5))
    ]
    
    for start, end in arrows:
        ax1.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    
    ax1.axis('off')
    
    # ===== Segmentation Workflow =====
    ax2.set_xlim(0, 12)
    ax2.set_ylim(0, 3)
    ax2.set_title('Full Segmentation Workflow with ERP-CBAM Integration', fontsize=14, fontweight='bold')
    
    # Workflow boxes
    workflow_boxes = [
        (0.5, 1, 'Input\nImage'),
        (2.5, 1, 'Encoder\n(ResNet)'),
        (4.5, 1, 'ERP-CBAM\nAttention'),
        (6.5, 1, 'ASPP\nModule'),
        (8.5, 1, 'Decoder'),
        (10.5, 1, 'Segmentation\nMask')
    ]
    
    colors = ['lightblue', 'lightgreen', 'gold', 'lightcoral', 'lightyellow', 'lightgray']
    
    for i, (x, y, text) in enumerate(workflow_boxes):
        box = FancyBboxPatch((x, y), 1.5, 1, boxstyle="round,pad=0.1",
                            facecolor=colors[i], edgecolor='black', linewidth=1.5)
        ax2.add_patch(box)
        ax2.text(x + 0.75, y + 0.5, text, ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Add arrows between boxes
        if i < len(workflow_boxes) - 1:
            ax2.annotate('', xy=(workflow_boxes[i+1][0], y + 0.5), 
                        xytext=(x + 1.5, y + 0.5),
                        arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('comprehensive_erp_cbam_diagram.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig('comprehensive_erp_cbam_diagram.pdf', bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print("Diagram saved as comprehensive_erp_cbam_diagram.png and .pdf")
    plt.show()

if __name__ == "__main__":
    create_comprehensive_diagram()
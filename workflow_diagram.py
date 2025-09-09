import matplotlib.pyplot as plt
import numpy as np

def draw_diagram():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))

    # ERP-CBAM Module Architecture
    ax.text(0.5, 0.9, 'ERP-CBAM Module', fontsize=14, ha='center')
    ax.text(0.3, 0.85, 'Channel Attention', fontsize=12, ha='center')
    ax.text(0.5, 0.85, 'Spatial Attention', fontsize=12, ha='center')
    ax.text(0.7, 0.85, 'Latitude-aware Weighting', fontsize=12, ha='center')

    # Full Segmentation Pipeline
    ax.text(0.5, 0.6, 'Segmentation Pipeline', fontsize=14, ha='center')
    ax.arrow(0.5, 0.75, 0, -0.1, head_width=0.03, head_length=0.05, fc='k', ec='k')
    ax.text(0.5, 0.5, 'Input Image -> Feature Extraction -> ERP-CBAM -> DeepLabV3+ -> Final Mask', fontsize=12, ha='center')

    # Model Integration
    ax.text(0.5, 0.3, 'DeepLabV3+ Architecture', fontsize=14, ha='center')
    ax.text(0.3, 0.25, 'ERP-CBAM Applied Here', fontsize=12, ha='center')
    ax.arrow(0.5, 0.45, 0, -0.1, head_width=0.03, head_length=0.05, fc='k', ec='k')

    # Finalization
    ax.axis('off')  # Turn off the axis
    plt.title('ERP-CBAM Attention Module and Segmentation Workflow', fontsize=16)
    plt.savefig('erp_cbam_segmentation_workflow.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    draw_diagram()
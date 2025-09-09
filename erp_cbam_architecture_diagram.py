import matplotlib.pyplot as plt
import numpy as np

def draw_attention_module(ax):
    # Draw ERP-CBAM attention module architecture
    ax.text(0.5, 0.9, 'ERP-CBAM Attention Module', fontsize=12, ha='center', weight='bold')
    ax.annotate('Channel Attention', xy=(0.3, 0.7), xytext=(0.1, 0.8),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('Spatial Attention', xy=(0.5, 0.7), xytext=(0.6, 0.8),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('Latitude-aware Weighting', xy=(0.7, 0.7), xytext=(0.8, 0.8),
                arrowprops=dict(facecolor='black', shrink=0.05))

def draw_segmentation_workflow(ax):
    # Draw segmentation workflow with DeepLabV3+
    ax.text(0.5, 0.4, 'Segmentation Workflow', fontsize=12, ha='center', weight='bold')
    ax.annotate('Input Image', xy=(0.5, 0.3), xytext=(0.5, 0.25),
                arrowprops=dict(facecolor='blue', shrink=0.05))
    ax.annotate('DeepLabV3+', xy=(0.5, 0.2), xytext=(0.5, 0.1),
                arrowprops=dict(facecolor='green', shrink=0.05))
    ax.annotate('Output Segmentation Map', xy=(0.5, 0.1), xytext=(0.5, 0.05),
                arrowprops=dict(facecolor='red', shrink=0.05))

def draw_multi_scale(ax):
    # Draw multi-scale feature processing
    ax.text(0.5, 0.6, 'Multi-scale Feature Processing', fontsize=12, ha='center', weight='bold')
    ax.annotate('Scale 1', xy=(0.2, 0.5), xytext=(0.1, 0.6),
                arrowprops=dict(facecolor='purple', shrink=0.05))
    ax.annotate('Scale 2', xy=(0.5, 0.5), xytext=(0.5, 0.6),
                arrowprops=dict(facecolor='purple', shrink=0.05))
    ax.annotate('Scale 3', xy=(0.8, 0.5), xytext=(0.9, 0.6),
                arrowprops=dict(facecolor='purple', shrink=0.05))

def main():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')

    draw_attention_module(ax)
    draw_segmentation_workflow(ax)
    draw_multi_scale(ax)

    plt.title('ERP-CBAM Architecture Diagram', fontsize=14)
    plt.savefig('erp_cbam_architecture_diagram.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
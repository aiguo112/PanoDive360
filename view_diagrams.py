import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def display_architecture_diagrams():
    """
    Display all the generated architecture diagrams to show the enhanced complexity
    """
    
    # List of generated diagrams
    diagrams = [
        ('comprehensive_erp_cbam_diagram.png', 'Enhanced Comprehensive ERP-CBAM Diagram'),
        ('enhanced_deeplabv3_architecture_diagram.png', 'Enhanced DeepLabV3+ Multi-panel Architecture'),
        ('detailed_deeplabv3_architecture.png', 'Highly Detailed DeepLabV3+ Research-level Diagram')
    ]
    
    # Create figure to display all diagrams
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))
    fig.suptitle('Evolution of Architecture Diagrams: From Basic to Research-Paper Complexity', 
                 fontsize=16, fontweight='bold')
    
    for i, (filename, title) in enumerate(diagrams):
        if os.path.exists(filename):
            img = mpimg.imread(filename)
            axes[i].imshow(img)
            axes[i].set_title(title, fontsize=12, fontweight='bold')
            axes[i].axis('off')
        else:
            axes[i].text(0.5, 0.5, f'File not found:\n{filename}', 
                        ha='center', va='center', transform=axes[i].transAxes)
            axes[i].set_title(title, fontsize=12, fontweight='bold')
            axes[i].axis('off')
    
    plt.tight_layout()
    plt.savefig('architecture_comparison.png', dpi=150, bbox_inches='tight')
    plt.savefig('architecture_comparison.pdf', bbox_inches='tight')
    
    print("Architecture comparison saved as architecture_comparison.png")
    print("\nGenerated diagrams summary:")
    print("1. Enhanced Comprehensive ERP-CBAM Diagram - Technical details and mathematical notation")
    print("2. Enhanced DeepLabV3+ Multi-panel - Multiple detailed views of architecture components")
    print("3. Highly Detailed Research-level - Complete technical specifications like research papers")
    
    return plt

if __name__ == "__main__":
    display_architecture_diagrams()
    plt.show()
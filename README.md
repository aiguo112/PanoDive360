
# Custom DeepLabV3+ with CBAM for Semantic Segmentation

This repository contains an implementation of a custom semantic segmentation model based on **DeepLabV3+** with **Convolutional Block Attention Module (CBAM)**. The model is built using PyTorch and uses CBAM blocks to improve feature representation in the segmentation process. The dataset used is expected to have RGB images and corresponding labeled masks with multiple classes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Dataset Structure](#dataset-structure)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Evaluating the Model](#evaluating-the-model)
- [Model Architecture](#model-architecture)
- [Files Overview](#files-overview)
- [License](#license)

## Features

- **Custom DeepLabV3+ Model**: Implements DeepLabV3+ with a ResNet-34 backbone and pretrained ImageNet weights.
- **CBAM (Convolutional Block Attention Module)**: Attention mechanism to improve feature extraction at different layers.
- **Multi-class segmentation**: Designed for semantic segmentation with 11 different classes, including the background.
- **TensorBoard support**: Visualize training progress and metrics using TensorBoard.
- **Early stopping**: Implements early stopping when the validation loss stops improving.
- **Custom Dice Loss**: Combines Dice Loss and Cross-Entropy Loss for better performance on imbalanced datasets.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/aiguo112/PanoDive360.git
   cd PanoDive360
   ```

2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that you have a CUDA-compatible GPU and PyTorch installed. You can install PyTorch by following the instructions [here](https://pytorch.org/get-started/locally/).

## Dataset Structure

The dataset should be structured as follows:

```text
data_split/
│
├── train/
│   ├── images/
│   └── masks/
├── valid/
│   ├── images/
│   └── masks/
```

- **images/**: Directory containing RGB images.
- **masks/**: Corresponding masks with labels for each class (as per the color mapping).

Make sure the masks are PNG files with the same filename as the images, following this naming convention:
- Images: `image_001.jpg`
- Masks: `mask_001.png`

## Usage

### Training the Model

1. Ensure that the dataset is properly structured as mentioned above.
2. You can configure any hyperparameters and file paths in the `config.py` file.
3. To train the model, run the following command:
   ```bash
   python main.py
   ```

The model checkpoints and TensorBoard logs will be saved in the `runs/` directory.

### Evaluating the Model

You can evaluate the model during training, as the script outputs both training and validation metrics for each epoch. If you wish to load a specific model checkpoint for inference, you can use the `load_checkpoint` function provided in `train.py`.

## Model Architecture

The custom model uses the **DeepLabV3+** architecture with a ResNet-34 encoder. Additionally, **CBAM (Convolutional Block Attention Module)** is added at three different layers to enhance the spatial and channel-wise attention for better segmentation results.

![Model Architecture](path_to_architecture_image.png)

## Files Overview

- **config.py**: Contains paths and parameters like input image size, number of classes, and the dataset directory.
- **utils.py**: Helper functions for converting between RGB masks and one-hot encoded masks.
- **dataset.py**: `SegmentationDataset` class and DataLoader setup.
- **losses.py**: Defines custom loss functions, including Dice Loss and a combined loss.
- **cbam.py**: Implements the CBAM block used in the custom DeepLabV3+ model.
- **model.py**: Defines the custom DeepLabV3+ model with CBAM.
- **train.py**: Contains the training loop, model evaluation, and checkpoint saving.
- **main.py**: Entry point for training the model.
- **requirements.txt**: Lists the necessary dependencies for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

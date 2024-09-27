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
   git clone https://github.com/your-username/custom-deeplabv3plus-cbam.git
   cd custom-deeplabv3plus-cbam

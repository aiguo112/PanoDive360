import math

import torch
import torch.nn as nn


class ERP_CBAM(nn.Module):
    def __init__(self, channels, reduction_ratio=16):
        super(ERP_CBAM, self).__init__()

        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(channels, channels // reduction_ratio, kernel_size=1),
            nn.ReLU(),
            nn.Conv2d(channels // reduction_ratio, channels, kernel_size=1),
            nn.Sigmoid()
        )

        self.spatial_conv = nn.Conv2d(2, 1, kernel_size=7, padding=3)

        self.alpha = nn.Parameter(torch.ones(1))
        self.beta = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        ca = self.channel_attention(x)
        x = x * ca

        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        spatial_input = torch.cat([avg_out, max_out], dim=1)

        spatial_attention = self.spatial_conv(spatial_input)
        spatial_attention = torch.sigmoid(spatial_attention)

        _, _, height, _ = x.size()

        theta = (torch.arange(0, height).float().unsqueeze(1).to(x.device) / height) * math.pi - (math.pi / 2)
        theta_weight = self.alpha * torch.cos(theta) + self.beta

        spatial_attention = spatial_attention * theta_weight.view(1, 1, height, 1)
        x = x * spatial_attention

        return x

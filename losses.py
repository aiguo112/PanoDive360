import torch
import torch.nn as nn

class DiceLoss(nn.Module):
    def __init__(self):
        super(DiceLoss, self).__init__()

    def forward(self, inputs, targets, smooth=1):
        inputs = torch.sigmoid(inputs)
        intersection = (inputs * targets).sum(dim=2).sum(dim=2)
        dice = (2. * intersection + smooth) / (inputs.sum(dim=2).sum(dim=2) + targets.sum(dim=2).sum(dim=2) + smooth)
        return 1 - dice.mean()

cross_entropy_loss = nn.CrossEntropyLoss()
dice_loss = DiceLoss()

def combined_loss(inputs, targets):
    targets_onehot = torch.zeros(inputs.shape).cuda()
    targets_onehot.scatter_(1, targets.unsqueeze(1), 1)
    return cross_entropy_loss(inputs, targets) + dice_loss(inputs, targets_onehot)

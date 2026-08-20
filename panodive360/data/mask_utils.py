import numpy as np


def rgb_to_onehot(mask, color_map):
    mask_onehot = np.zeros((*mask.shape[:2], len(color_map)), dtype=np.float32)
    for rgb, idx in color_map.items():
        mask_onehot[np.all(mask == rgb, axis=-1), idx] = 1
    return mask_onehot


def onehot_to_rgb(mask, color_map):
    single_layer_mask = np.argmax(mask, axis=0)
    rgb_mask = np.zeros((mask.shape[1], mask.shape[2], 3), dtype=np.uint8)
    for i, rgb in enumerate(color_map.keys()):
        rgb_mask[single_layer_mask == i] = rgb
    return rgb_mask

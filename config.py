import os

# Point this at your local copy of the PanoDive360 split.
# Expected layout: {base_dir}/{train,valid}/{images,masks}
base_dir = os.environ.get('PANODIVE360_DATA', os.path.join('data_split'))
train_images_dir = os.path.join(base_dir, 'train', 'images')
train_masks_dir = os.path.join(base_dir, 'train', 'masks')
valid_images_dir = os.path.join(base_dir, 'valid', 'images')
valid_masks_dir = os.path.join(base_dir, 'valid', 'masks')

os.environ.setdefault('CUDA_VISIBLE_DEVICES', '0')

# Training script currently resizes to a square crop; source ERP frames are 2:1.
input_size = (1024, 1024)
num_classes = 11  # 10 foreground classes + background water

CLASS_NAMES = [
    'background',
    'diver',
    'shark',
    'fish',
    'sea_turtle',
    'dolphin',
    'sea_lion',
    'coral',
    'shipwreck',
    'seaweed',
    'rock',
]

# RGB label colors used in the PNG masks (see README).
color_map = {
    (0, 0, 0): 0,            # background
    (167, 242, 82): 1,       # diver
    (166, 3, 3): 2,          # shark
    (255, 237, 29): 3,       # fish
    (255, 0, 243): 4,        # sea turtle
    (30, 95, 170): 5,        # dolphin
    (169, 205, 248): 6,      # sea lion
    (106, 37, 163): 7,       # coral
    (115, 76, 20): 8,        # shipwreck
    (233, 180, 245): 9,      # seaweed
    (245, 94, 94): 10,       # rock
}

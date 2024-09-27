import os

# Directories for train, valid, and test sets
base_dir = r'/home/arbi/PycharmProjects/Data_Prep_Pano/data_split'
train_images_dir = os.path.join(base_dir, 'train', 'images')
train_masks_dir = os.path.join(base_dir, 'train', 'masks')
valid_images_dir = os.path.join(base_dir, 'valid', 'images')
valid_masks_dir = os.path.join(base_dir, 'valid', 'masks')

# Set the environment variable
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

# Parameters
input_size = (1024, 1024)
num_classes = 11  # Number of classes including the background

# Color mapping for masks
color_map = {
    (0, 0, 0): 0,
    (167, 242, 82): 1,
    (166, 3, 3): 2,
    (255, 237, 29): 3,
    (255, 0, 243): 4,
    (30, 95, 170): 5,
    (169, 205, 248): 6,
    (106, 37, 163): 7,
    (115, 76, 20): 8,
    (233, 180, 245): 9,
    (245, 94, 94): 10,
}

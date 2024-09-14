from PIL import Image
import os

def resize_image(image_path, output_path, target_width, target_height):
    """
    Resize an image while maintaining aspect ratio without adding padding.

    Parameters:
    image_path (str): Path to the input image file.
    output_path (str): Path to save the resized image.
    target_width (int): The target width of the resized image.
    target_height (int): The target height of the resized image.
    """
    with Image.open(image_path) as img:
        # Calculate the aspect ratio of the image and the target
        img_ratio = img.width / img.height
        target_ratio = target_width / target_height

        if img_ratio > target_ratio:
            # Image is wider than the target aspect ratio
            new_width = target_width
            new_height = round(target_width / img_ratio)
        else:
            # Image is taller than the target aspect ratio
            new_height = target_height
            new_width = round(target_height * img_ratio)

        # Resize the image to fit within the target dimensions without padding
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image
        img.save(output_path)

def resize_images_in_folder(input_folder, output_folder, target_width, target_height):
    """
    Resize all images in a folder while maintaining aspect ratio, without adding padding.

    Parameters:
    input_folder (str): Path to the folder containing images to resize.
    output_folder (str): Path to save the resized images.
    target_width (int): The target width for the resized images.
    target_height (int): The target height for the resized images.
    """
    supported_formats = ('.png', '.jpg', '.jpeg')

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(supported_formats):
                image_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, file)

                resize_image(image_path, output_path, target_width, target_height)

# Example usage:
input_frames_folder = r'/path/to/frames'  # Path to input frames folder
output_resized_folder = r'/path/to/resized/frames'  # Path to save resized frames

target_width = 1664  # Desired width
target_height = 832   # Desired height

resize_images_in_folder(input_frames_folder, output_resized_folder, target_width, target_height)

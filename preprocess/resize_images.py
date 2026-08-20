from PIL import Image
import os


def resize_image(image_path, output_path, target_width, target_height):
    """Resize an image to fit inside the target size without padding."""
    with Image.open(image_path) as img:
        img_ratio = img.width / img.height
        target_ratio = target_width / target_height

        if img_ratio > target_ratio:
            new_width = target_width
            new_height = round(target_width / img_ratio)
        else:
            new_height = target_height
            new_width = round(target_height * img_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(output_path)


def resize_images_in_folder(input_folder, output_folder, target_width, target_height):
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


if __name__ == '__main__':
    input_frames_folder = r'/path/to/frames'
    output_resized_folder = r'/path/to/resized/frames'
    target_width = 1664
    target_height = 832
    resize_images_in_folder(input_frames_folder, output_resized_folder, target_width, target_height)

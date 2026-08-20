import os
import subprocess


def convert_stereo_to_mono(input_folder, output_folder):
    """Convert dual-channel 360 video to monoscopic ERP with FFmpeg."""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.endswith('.mp4'):
            continue
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        try:
            subprocess.run([
                'ffmpeg',
                '-i', input_path,
                '-vcodec', 'h264_nvenc',
                '-vf', 'v360=eac:equirect',
                '-b:v', '50M',
                '-an',
                output_path,
            ], check=True)
            print(f'Successfully converted: {filename}')
        except subprocess.CalledProcessError as e:
            print(f'Error occurred while converting {filename}: {e}')

    print('All conversions are done.')


if __name__ == '__main__':
    input_folder = r'/path/to/input/videos'
    output_folder = r'/path/to/output/videos'
    convert_stereo_to_mono(input_folder, output_folder)

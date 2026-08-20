import os
import subprocess


def extract_frames(input_video_path, output_folder, frame_interval=5, output_format='png', fps=None):
    """Extract stills from a video with FFmpeg."""
    os.makedirs(output_folder, exist_ok=True)
    filter_option = f'fps={fps}' if fps else f'fps=1/{frame_interval}'
    output_pattern = os.path.join(output_folder, f'frame_%04d.{output_format}')
    subprocess.run([
        'ffmpeg', '-i', input_video_path,
        '-vf', filter_option,
        output_pattern,
    ])


def process_videos(input_folder, output_folder, frame_interval=5, output_format='png', fps=None):
    video_extensions = ('.mp4', '.mkv', '.avi', '.webm')
    video_files = [f for f in os.listdir(input_folder) if f.endswith(video_extensions)]

    for video_file in video_files:
        input_video_path = os.path.join(input_folder, video_file)
        video_output_folder = os.path.join(output_folder, os.path.splitext(video_file)[0])
        extract_frames(input_video_path, video_output_folder, frame_interval, output_format, fps)


if __name__ == '__main__':
    input_folder = r'/path/to/videos'
    output_folder = r'/path/to/frames'
    process_videos(input_folder, output_folder, frame_interval=5, output_format='png', fps=None)

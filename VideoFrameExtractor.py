import os
import subprocess

def extract_frames(input_video_path, output_folder, frame_interval=5, output_format='png', fps=None):
    """
    Extract frames from a video at a specific interval or using a custom FPS rate.

    Parameters:
    input_video_path (str): Path to the input video file.
    output_folder (str): Directory where extracted frames will be saved.
    frame_interval (int, optional): Time interval (in seconds) to extract frames. Defaults to 5 seconds.
    output_format (str, optional): Format of the output frames (png, jpg). Defaults to 'png'.
    fps (int, optional): Custom frames per second rate. If set, it overrides frame_interval.
    """
    os.makedirs(output_folder, exist_ok=True)
    
    # Use either fps or frame_interval to set the extraction rate
    filter_option = f"fps={fps}" if fps else f"fps=1/{frame_interval}"

    # FFmpeg command to extract frames
    output_pattern = os.path.join(output_folder, f'frame_%04d.{output_format}')
    subprocess.run([
        'ffmpeg', '-i', input_video_path,
        '-vf', filter_option,
        output_pattern
    ])

def process_videos(input_folder, output_folder, frame_interval=5, output_format='png', fps=None):
    """
    Process multiple videos from an input folder and extract frames.

    Parameters:
    input_folder (str): Path to the folder containing video files.
    output_folder (str): Path to the folder where extracted frames for all videos will be saved.
    frame_interval (int, optional): Time interval (in seconds) to extract frames. Defaults to 5 seconds.
    output_format (str, optional): Format of the output frames. Defaults to 'png'.
    fps (int, optional): Custom frames per second rate. If set, it overrides frame_interval.
    """
    video_extensions = ('.mp4', '.mkv', '.avi', '.webm')
    video_files = [f for f in os.listdir(input_folder) if f.endswith(video_extensions)]
    
    for video_file in video_files:
        input_video_path = os.path.join(input_folder, video_file)
        video_output_folder = os.path.join(output_folder, os.path.splitext(video_file)[0])

        extract_frames(input_video_path, video_output_folder, frame_interval, output_format, fps)

# Example usage:
input_folder = r'/path/to/videos'  # Replace with your input folder
output_folder = r'/path/to/frames'  # Replace with your output folder

frame_interval = 5  # Extract one frame every 5 seconds
output_format = 'png'  # You can also use 'jpg' or others
fps = None  # Optionally, use a custom FPS instead of frame_interval

process_videos(input_folder, output_folder, frame_interval, output_format, fps)

import os
import subprocess

# Function to convert stereo video to mono using FFmpeg
def convert_stereo_to_mono(input_folder, output_folder):
    """
    This function converts stereo 360° video files to mono using FFmpeg.
    
    Parameters:
    - input_folder (str): The folder containing input stereo video files.
    - output_folder (str): The folder where the converted mono videos will be saved.
    
    The function iterates through all the .mp4 files in the input folder and applies the
    FFmpeg command to convert them using the h264_nvenc codec and equirectangular projection.
    """
    # Ensure the output folder exists, create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # Process only .mp4 video files
        if filename.endswith('.mp4'):
            # Construct full paths for the input and output files
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Run the FFmpeg command to convert the stereo video to mono
            try:
                subprocess.run([
                    'ffmpeg', 
                    '-i', input_path,          # Input file path
                    '-vcodec', 'h264_nvenc',   # Use the NVIDIA NVENC codec for encoding
                    '-vf', 'v360=eac:equirect',# Apply 360 video transformation (equirectangular)
                    '-b:v', '50M',             # Set video bitrate to 50 Mbps
                    '-an',                     # Disable audio in the output
                    output_path                # Output file path
                ], check=True)
                print(f"Successfully converted: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error occurred while converting {filename}: {e}")

    print('All conversions are done.')

if __name__ == "__main__":
    # Define the input and output directories (user can modify these paths)
    input_folder = r"C:\path\to\input\videos"    # Replace with the path to your input folder
    output_folder = r"C:\path\to\output\videos"  # Replace with the path to your output folder

    # Run the conversion function
    convert_stereo_to_mono(input_folder, output_folder)

from moviepy import VideoFileClip
import os

input_file = "canary.mov"
output_file = "canary_optimized.gif"
target_size_mb = 5.0

# Initial attempt settings
width = 480
fps = 10

clip = VideoFileClip(input_file)

# Resize and write
print(f"Converting with width={width} and fps={fps}...")
final_clip = clip.resized(width=width)
final_clip.write_gif(output_file, fps=fps)

# Check size and retry if needed
file_size = os.path.getsize(output_file) / (1024 * 1024)
print(f"File size: {file_size:.2f} MB")

if file_size > target_size_mb:
    print("File too large. Retrying with lower specs...")
    width = 360
    fps = 8
    final_clip = clip.resized(width=width)
    final_clip.write_gif(output_file, fps=fps)
    print(f"New size: {os.path.getsize(output_file) / (1024 * 1024):.2f} MB")
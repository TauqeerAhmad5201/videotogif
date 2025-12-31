# Video to GIF Converter

A simple and efficient Python tool to convert video files to optimized GIF format with automatic size adjustment.

## Features

- 🎬 Convert video files to GIF format
- 📏 Automatic size optimization to meet target file size
- ⚙️ Configurable output dimensions and frame rate
- 🔄 Smart retry mechanism with reduced quality if file exceeds target size
- 💾 Target file size control (default: 5 MB)

## Prerequisites

- Python 3.7 or higher
- moviepy library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/videotogif.git
cd videotogif
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your video file in the project directory
2. Edit the `main.py` file to configure:
   - `input_file`: Path to your input video file
   - `output_file`: Desired output GIF filename
   - `target_size_mb`: Maximum GIF file size in MB

3. Run the converter:
```bash
python main.py
```

### Example

```python
input_file = "my_video.mov"
output_file = "my_video.gif"
target_size_mb = 5.0
```

## Configuration

The script uses these default settings:
- **Initial width**: 480px (height auto-scales)
- **Initial FPS**: 10 frames per second
- **Fallback width**: 360px (if file too large)
- **Fallback FPS**: 8 frames per second

You can modify these values in `main.py` to suit your needs.

## How It Works

1. Loads the input video file
2. Resizes video to specified width (maintains aspect ratio)
3. Converts to GIF at specified FPS
4. Checks output file size
5. If size exceeds target, automatically re-encodes with lower quality settings

## Supported Video Formats

The tool supports all video formats that moviepy/FFmpeg can handle:
- MOV
- MP4
- AVI
- MKV
- And many more

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [MoviePy](https://zulko.github.io/moviepy/)
- Powered by FFmpeg

## Troubleshooting

### Installation Issues
If you encounter issues installing moviepy, make sure you have FFmpeg installed:
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Large Output Files
If your GIF is still too large after conversion:
- Reduce the `width` value further (e.g., 320px)
- Lower the `fps` value (e.g., 6 fps)
- Trim your video to a shorter duration before conversion

## Future Enhancements

- [ ] Command-line argument support
- [ ] Batch processing multiple videos
- [ ] GUI interface
- [ ] Custom quality presets
- [ ] Progress bar for conversion

---

Made with ❤️ by ME + AI

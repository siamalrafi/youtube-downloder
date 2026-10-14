# YouTube Downloader (Python + yt-dlp)

A simple command-line tool to download YouTube videos or extract audio (MP3) from one or multiple URLs, with resolution selection and automatic folder organization.

## Features

- **Batch downloads** — paste multiple YouTube URLs (one per line) and download them all in one run
- **Two download modes**
    - **Video** — downloads video + audio merged into MP4
    - **Audio (MP3)** — extracts audio only, converted to MP3 at 320kbps
- **Resolution selection** — choose from all resolutions actually available for the video, or press **ENTER** to automatically use the best available resolution
- **Smart resolution fallback** — if a chosen resolution isn't available for a specific video in the batch, it automatically falls back to the next higher resolution (or best available)
- **Organized output folders**
    - Videos are saved to: `Downloads/Python Download`
    - Audio files are saved to: `Downloads/Python Download/Audio Only`
- **Automatic folder creation** — output folders are created automatically if they don't exist

## Requirements

### Software

- **Python 3.8+**
- **FFmpeg** — required for merging video/audio streams and converting audio to MP3

### Python Packages

- **yt-dlp**

## Installation

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/) if not already installed. Make sure to check **"Add Python to PATH"** during installation.

### 2. Install FFmpeg

**Using Windows Package Manager (winget):**

```bash
winget install Gyan.FFmpeg
```

**Or manually:**

1. Download FFmpeg from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) or [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract it to a folder on your system
3. Note the path to the `bin` folder inside the extracted files

### 3. Install yt-dlp

```bash
pip install yt-dlp
```

### 4. Configure FFmpeg Path

Open the script and update the `FFMPEG_PATH` variable to match your FFmpeg installation location:

```python
FFMPEG_PATH = r"C:\path\to\your\ffmpeg\bin"
```

## Usage

1. Run the script:
    ```bash
    python downloader.py
    ```
2. Paste one or more YouTube URLs, one per line. Press **ENTER** on an empty line when done.
3. Choose a mode:
    - `1` for Video
    - `2` for Audio (MP3)
4. If downloading video, choose a resolution from the list shown, or press **ENTER** to use the best available resolution automatically.
5. Wait for downloads to complete — progress is shown for each file.

## Output Structure

```
Downloads/
└── Python Download/
    ├── Video Title 1.mp4
    ├── Video Title 2.mp4
    └── Audio Only/
        ├── Song Title 1.mp3
        └── Song Title 2.mp3
```

## Notes

- `noplaylist: True` is set, so only the individual video at each URL is downloaded — not an entire playlist, even if the URL belongs to one.
- Audio is extracted at **320kbps MP3** quality.
- Make sure your FFmpeg path is correct, or merging (video mode) and MP3 conversion (audio mode) will fail.

## Disclaimer

This tool is intended for downloading content you have the right to download (e.g., your own videos, royalty-free content, or content licensed for offline use) . Respect YouTube's Terms of Service and copyright law when using this tool.

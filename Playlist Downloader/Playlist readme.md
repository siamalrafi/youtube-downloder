# YouTube Playlist Downloader (Python + yt-dlp)

A command-line tool to download an entire YouTube playlist as video, audio (MP3), or video-only, with resolution selection.

## Features

- **Full playlist download** — provide one playlist URL and download every video in it
- **Three download modes**
    - **Video + Audio** — normal video with sound, merged into MP4
    - **Audio only (MP3)** — extracts audio only, converted to MP3
    - **Video only** — video stream with no audio track
- **Resolution selection menu** — choose from preset resolutions (1080p, 720p, 480p, 360p), or select "Best available" / press **ENTER** to skip the limit and get the best quality
- **Numbered playlist filenames** — each file is saved with its playlist position, e.g. `01 - Song Title.mp3`
- **Error tolerance** — if a video in the playlist is private, deleted, or fails for any reason, the tool skips it and continues with the rest (`ignoreerrors: True`)
- **Automatic folder creation** — the output folder is created automatically if it doesn't exist

## Requirements

### Software

- **Python 3.8+**
- **FFmpeg** — required for merging video/audio streams and for MP3 conversion (must be installed and available on your system PATH)

### Python Packages

- **yt-dlp**

## Installation

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/). Make sure to check **"Add Python to PATH"** during installation.

### 2. Install FFmpeg

**Using Windows Package Manager (winget):**

```bash
winget install Gyan.FFmpeg
```

**Or manually:**

1. Download FFmpeg from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) or [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract it to a folder on your system
3. Add the `bin` folder inside the extracted files to your system's **PATH** environment variable

> Unlike some other scripts, this one does **not** set an `ffmpeg_location` manually — it relies on FFmpeg being available via PATH. Verify it works by running `ffmpeg -version` in your terminal/command prompt.

### 3. Install yt-dlp

```bash
pip install yt-dlp
```

## Usage

1. Run the script:
    ```bash
    python playlist_downloader.py
    ```
2. Enter the full YouTube **playlist URL** when prompted.
3. Choose a download mode:
    - `1` — Video + Audio
    - `2` — Audio only (MP3)
    - `3` — Video only (no sound)
4. If you chose mode `1` or `3`, choose a resolution:
    - `1` — 1080p
    - `2` — 720p
    - `3` — 480p
    - `4` — 360p
    - `5` — Best available
    - Press **ENTER** — also defaults to best available
5. The tool downloads every video in the playlist, skipping any that fail.

## Output

Files are saved to:

```
Downloads/
└── Python Playlist Downloader/
    ├── 01 - First Video Title.mp4
    ├── 02 - Second Video Title.mp4
    └── 03 - Third Video Title.mp4
```

Filenames are automatically numbered according to their position in the playlist.

## Notes

- If a requested resolution isn't available for a video, yt-dlp falls back within the format string (`best[height<=...]`) rather than failing outright.
- Audio mode extracts MP3 at **192kbps**.
- This script processes an entire playlist in one run — for downloading individual, unrelated videos, use a separate single/multi-URL downloader instead.

## Disclaimer

This tool is intended for downloading content you have the right to download (e.g., your own videos, royalty-free content, or content licensed for offline use). Respect YouTube's Terms of Service and copyright law when using this tool.

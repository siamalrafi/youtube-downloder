# YouTube Downloader Tools

Simple Python CLI tools to download YouTube videos, playlists, and audio (MP3) using `yt-dlp`.

## Scripts

- **`downloader.py`** — Download single/multiple YouTube video URLs (video or MP3), saves audio to an `Audio Only` subfolder.
- **`playlist_downloader.py`** — Download an entire YouTube playlist (video, audio-only, or video-only), with numbered filenames.

## Requirements

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) (installed and on PATH, or configured in the script)
- yt-dlp

## Installation

```bash
pip install yt-dlp
```

Install FFmpeg (Windows example):

```bash
winget install Gyan.FFmpeg
```

## Usage

```bash
python downloader.py
python playlist_downloader.py
```

Follow the on-screen prompts to choose download mode (video / audio / video-only) and resolution.

## Output

Downloaded files are saved under your `Downloads` folder in a dedicated subfolder for each script.

## Disclaimer

For downloading content you have the right to download. Respect YouTube's Terms of Service and copyright law.

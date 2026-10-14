from pathlib import Path
from yt_dlp import YoutubeDL

# ---------------------------
# Configuration
# --------------------------- 

# FFmpeg location
FFMPEG_PATH = r"C:\Users\Siam Al Rafi\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin"

# Automatically detect the Downloads folder
DOWNLOAD_FOLDER = Path.home() / "Downloads" / "Python Downloader"
AUDIO_FOLDER = DOWNLOAD_FOLDER / "Audio Only"

# ---------------------------
# Read multiple URLs
# ---------------------------

print("Paste YouTube URLs (one per line).")
print("Press ENTER twice when finished.\n")

urls = []

while True:
    url = input().strip()

    if not url:
        break

    urls.append(url)

if not urls:
    print("No URLs entered.")
    exit()

print(f"\nDownloads will be saved to:\n{DOWNLOAD_FOLDER}")

# ---------------------------
# Read first video to determine available resolutions
# ---------------------------

with YoutubeDL({"quiet": True}) as ydl:
    info = ydl.extract_info(urls[0], download=False)

video_formats = {}

for f in info["formats"]:
    if f.get("vcodec") != "none" and f.get("height"):

        h = f["height"]

        if (
            h not in video_formats
            or f.get("tbr", 0) > video_formats[h].get("tbr", 0)
        ):
            video_formats[h] = f

print("\n==============================")
print("      YouTube Downloader")
print("==============================")
print("1. Download Video")
print("2. Download Audio (MP3)")

choice = input("\nChoose: ").strip()

# =====================================================
# VIDEO
# =====================================================

if choice == "1":

    resolutions = sorted(video_formats)

    print("\nAvailable Resolutions:\n")

    for i, r in enumerate(resolutions, 1):
        print(f"{i}. {r}p")

    print("\nPress ENTER without typing anything to use the best available resolution.")

    while True:
        res_input = input("\nChoose resolution (or press ENTER for best): ").strip()

        if res_input == "":
            wanted_height = max(resolutions)
            print(f"No selection made — using best available resolution: {wanted_height}p")
            break

        try:
            idx = int(res_input) - 1

            if 0 <= idx < len(resolutions):
                wanted_height = resolutions[idx]
                break

            print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number, or press ENTER for best.")

    for count, url in enumerate(urls, start=1):

        print(f"\n[{count}/{len(urls)}] Fetching video information...")

        with YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        video_formats = {}

        for f in info["formats"]:

            if f.get("vcodec") != "none" and f.get("height"):

                h = f["height"]

                if (
                    h not in video_formats
                    or f.get("tbr", 0) > video_formats[h].get("tbr", 0)
                ):
                    video_formats[h] = f

        if wanted_height in video_formats:
            selected = video_formats[wanted_height]
        else:
            higher = [h for h in video_formats if h > wanted_height]

            if higher:
                selected = video_formats[min(higher)]
            else:
                selected = video_formats[max(video_formats)]

        print(f"Downloading {selected['height']}p...")

        options = {
            "format": f"{selected['format_id']}+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(DOWNLOAD_FOLDER / "%(title)s.%(ext)s"),
            "ffmpeg_location": FFMPEG_PATH,
            "noplaylist": True,
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])

# =====================================================
# AUDIO
# =====================================================

elif choice == "2":

    AUDIO_FOLDER.mkdir(parents=True, exist_ok=True)

    for count, url in enumerate(urls, start=1):

        print(f"\n[{count}/{len(urls)}] Downloading audio...")

        options = {
            "format": "bestaudio/best",
            "outtmpl": str(AUDIO_FOLDER / "%(title)s.%(ext)s"),
            "ffmpeg_location": FFMPEG_PATH,
            "noplaylist": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])

else:
    print("Invalid choice.")
    exit()

print("\n===================================")
print("✓ All downloads completed!")
print(f"Saved to: {DOWNLOAD_FOLDER}")
print("===================================")
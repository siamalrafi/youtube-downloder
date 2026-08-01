import os
import yt_dlp

OUTPUT_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "Python Playlist Downloader")


def download_playlist(playlist_url, mode="video", resolution=None, output_path=OUTPUT_PATH):
    os.makedirs(output_path, exist_ok=True)

    if mode == "audio":
        # Audio only, converted to mp3
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(playlist_index)s - %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ignoreerrors': True,
        }

    elif mode == "video_only":
        # Video stream only, no audio
        if resolution:
            fmt = f'bestvideo[height<={resolution}][ext=mp4]/bestvideo[height<={resolution}]'
        else:
            fmt = 'bestvideo[ext=mp4]/bestvideo'
        ydl_opts = {
            'format': fmt,
            'outtmpl': f'{output_path}/%(playlist_index)s - %(title)s.%(ext)s',
            'ignoreerrors': True,
        }

    else:  # mode == "video" (video + audio merged)
        if resolution:
            fmt = f'bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}]'
        else:
            fmt = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ydl_opts = {
            'format': fmt,
            'outtmpl': f'{output_path}/%(playlist_index)s - %(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'ignoreerrors': True,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ").strip()

    print("\nChoose download mode:")
    print("1. Video + Audio (normal)")
    print("2. Audio only (mp3)")
    print("3. Video only (no sound)")
    choice = input("Enter 1, 2, or 3: ").strip()

    mode_map = {"1": "video", "2": "audio", "3": "video_only"}
    mode = mode_map.get(choice, "video")

    resolution = None
    if mode in ("video", "video_only"):
        print("\nChoose max resolution:")
        print("1. 1080p")
        print("2. 720p")
        print("3. 480p")
        print("4. 360p")
        print("5. Best available (no limit)")
        res_choice = input("Enter 1-5 (or press Enter for best): ").strip()

        res_map = {
            "1": "1080",
            "2": "720",
            "3": "480",
            "4": "360",
            "5": None,
        }

        if res_choice == "":
            resolution = None
        elif res_choice in res_map:
            resolution = res_map[res_choice]
        else:
            print("Invalid choice, defaulting to best available.")
            resolution = None

    download_playlist(playlist_url, mode=mode, resolution=resolution)
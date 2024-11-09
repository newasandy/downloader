import yt_dlp

def download_youtube_video(url, output_path):
    # Set up options for yt_dlp to download the video in the best format
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file path
        'merge_output_format': 'mp4',  # Merge video and audio into mp4
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])  # Download video

        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
url = "https://www.youtube.com/watch?v=2112ZFrdZBk"
output_path = "./"  # Specify the folder where you want to save the file
download_youtube_video(url, output_path)

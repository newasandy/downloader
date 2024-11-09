import yt_dlp

def download_youtube_audio(url, output_path):
    # Set up options for yt_dlp to download only the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file path
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from: {url}")
            ydl.download([url])  # Download audio

        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage

collection_url = ["https://www.youtube.com/watch?v=aPi3aHwS6Y4",
                  "https://www.youtube.com/watch?v=CFX-v0RtnZ4",
                  "https://www.youtube.com/watch?v=xxFyLeAfS2A",
                  "https://www.youtube.com/watch?v=ftEzdVJWdDA",
                  "https://www.youtube.com/watch?v=taeE9_EQGwY",
                  "https://www.youtube.com/watch?v=qnT7lCH1_gg",
                  "https://www.youtube.com/watch?v=D-mERpuyZV8",
                  "https://www.youtube.com/watch?v=o4lsa0wyvyY",
                  "https://www.youtube.com/watch?v=Bw1IqmDRXQo",
                  "https://www.youtube.com/watch?v=fcEIpx7swLQ"]

# url = "https://www.youtube.com/watch?v=wxmehzGmN9s"

for url in collection_url:
    output_path = "./"  # Specify the folder where you want to save the file
    download_youtube_audio(url, output_path)

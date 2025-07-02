import csv
import os
import yt_dlp as ytdlp

# Function to download a YouTube video
def download_video(url, output_path):
    try:
        print(f"\nAttempting to download: {url}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_path, '%(title).200s.%(ext)s'),  # limit long filenames
            'noplaylist': True,
            'quiet': False,
            'restrictfilenames': True  # safer filenames
        }
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Function to read CSV and download videos
def download_videos_from_csv(csv_file, output_path):
    with open(csv_file, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("CSV Headers:", reader.fieldnames)

        for index, row in enumerate(reader, start=1):
            link = row['link'].strip()

            if 'youtu' in link:
                print(f"\n🔹 ({index}) Processing link: {link}")
                download_video(link, output_path)
            else:
                print(f"({index}) Skipped non-YouTube link: {link}")

# File paths
csv_file = 'csv_video_links.csv'
output_path = './YTVideo'

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Start downloading
download_videos_from_csv(csv_file, output_path)

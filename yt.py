import sys
import yt_dlp
import json
import os

if len(sys.argv) < 2:
    print("Usage: python yt.py <video_id>")
    sys.exit(1)

video_id = sys.argv[1]
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

# Store downloaded file in /home/node using video_id as filename
output_dir = "/home/node"
filename_mp4 = f"{video_id}.mp4"
output_template = os.path.join(output_dir, f"{video_id}.%(ext)s")

ydl_opts = {
    'outtmpl': output_template,
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'quiet': True,
    'noplaylist': True
}

results = []

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        title = info.get("title", "unknown_title")
        category_id = info.get("categoryId")  # should be an int or None
        file_path = os.path.join(output_dir, filename_mp4)

    results.append({
        "video_id": video_id,
        "title": title,
        "category_id": category_id,
        "status": "downloaded",
        "file_path": file_path,
        "binary": {
            "data": {
                "fileName": filename_mp4,
                "filePath": file_path,
                "mimeType": "video/mp4"
            }
        }
    })
except Exception as e:
    results.append({
        "video_id": video_id,
        "status": "error",
        "error": str(e)
    })

print(json.dumps(results, indent=2))

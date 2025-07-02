# 📅 YouTube Video Downloader from CSV

[![yt-dlp Version](https://img.shields.io/pypi/v/yt-dlp?label=yt-dlp&color=blue)](https://pypi.org/project/yt-dlp/)
[![Python](https://img.shields.io/badge/Python-3.7%2B-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🚀 Bulk download YouTube videos from a simple CSV file using `yt-dlp` with clean filenames and organized output.

---

## ✨ Features

✅ Read video URLs from a `.csv` file  
🎥 Download best video and audio in `.mp4` format  
🧹 Automatically clean and safe filenames  
📁 Output folder auto-created  
⚠️ Skips non-YouTube links  
📄 Simple logs for each download

---

## 📂 Project Structure

```
📁 Project Root
├── download_videos.py        # Main Python script
├── nxt2.csv                  # Your CSV with video links (column: 'link')
└── nxtV2/                    # Folder for downloaded videos
```

📄 **Sample CSV Format (`nxt2.csv`):**

```csv
link
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2
```

---

## 🚀 How to Use

### 🔧 1. Install Dependencies

```bash
pip install yt-dlp
```

### 📄 2. Prepare Your CSV File

- Make sure your CSV has a `link` column.
- Save it as `nxt2.csv` or update the filename in the script.

### ▶️ 3. Run the Script

```bash
python download_videos.py
```

🗂️ Videos will be saved inside the `nxtV2/` directory.

---

## ⚠️ Notes

- 🚩 Only valid **YouTube** links will be processed.
- ✂️ Long titles are truncated for OS-safe filenames.
- ⚡ Uses [yt-dlp](https://github.com/yt-dlp/yt-dlp), a modern fork of youtube-dl with improved performance and features.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- 🎞️ [yt-dlp](https://github.com/yt-dlp/yt-dlp) – modern video downloader engine.

---

> Built with 💻 by Shibam

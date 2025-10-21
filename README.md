# 🎬 Video Downloader Telegram Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)

**A simple Telegram bot for downloading videos from X (Twitter) and Pinterest**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Requirements](#-requirements)

</div>

---

## ✨ Features

- 📥 Download videos from **X (Twitter)** and **Pinterest**
- 🎯 Automatic video conversion to MP4 format
- 🔄 Background request processing
- 🚦 Queue system to prevent overload
- 📱 Direct video sending to Telegram
- 🎨 Simple and intuitive interface

## 🛠 Requirements

Before installation, make sure you have:

- **Python 3.8+**
- **FFmpeg** (for video conversion)
- **pip** (Python package manager)

### Installing FFmpeg

**Windows:**
```bash
# Download from official website: https://ffmpeg.org/download.html
# Add FFmpeg to PATH
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/NEIDTM/TelegramBot-VideoDownloader.git
cd TelegramBot-VideoDownloader
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create a `requirements.txt` file with the following content:**
```txt
python-telegram-bot
yt-dlp
requests
```

4. **Get your bot token:**
   - Open [@BotFather](https://t.me/BotFather) in Telegram
   - Send the `/newbot` command
   - Follow the instructions and save the token

5. **Configure the bot:**
   - Open the `bot.py` file
   - Replace `YOUR_BOT_TOKEN` with your actual token:
   ```python
   application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
   ```

## 🚀 Usage

1. **Run the bot:**
```bash
python bot.py
```

2. **In Telegram:**
   - Find your bot by name
   - Send the `/start` command
   - Send a video link from X or Pinterest
   - Wait for the download and receive your video!

## 📝 Link Examples

The bot supports the following link formats:

- `https://twitter.com/user/status/123456789`
- `https://x.com/user/status/123456789`
- `https://pinterest.com/pin/123456789/`
- `https://pin.it/abc123`

## ⚙️ How It Works

1. User sends a video link
2. Bot validates the link
3. A temporary script is created for background downloading
4. Video is downloaded using `yt-dlp`
5. Conversion to MP4 if necessary
6. Video is sent to the user in Telegram
7. Temporary files are deleted

---

<div align="center">

**Made with ❤️ for the Telegram community**

⭐ Star this project if you like it!

</div>

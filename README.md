# 🎬 Video Downloader Telegram Bot

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="50" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="50" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/X_logo_2023_%28white%29.png/500px-X_logo_2023_%28white%29.png" alt="X/Twitter" width="50" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Pinterest.svg/2048px-Pinterest.svg.png" alt="Pinterest" width="54" height="54"/>
</p>


**A simple Telegram bot for downloading videos from X (Twitter) and Pinterest**

<div align="center">

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

### Installing Python

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT:** Check "Add Python to PATH" during installation
4. Verify installation:
```bash
python --version
```

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Installing FFmpeg

FFmpeg is required for converting videos to MP4 format.

**Windows:**

**Option 1: Using Chocolatey (Easiest)**
```bash
choco install ffmpeg
```

**Option 2: Manual Installation**
1. Download FFmpeg from [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/)
2. Download **ffmpeg-release-essentials.zip**
3. Extract the archive to `C:\ffmpeg`
4. Add FFmpeg to PATH:
   - Press `Win + R` → type `sysdm.cpl` → press Enter
   - Go to **"Advanced"** tab → click **"Environment Variables"**
   - In **"System variables"** section, find `Path` → click **"Edit"**
   - Click **"New"** → add path: `C:\ffmpeg\bin`
   - Click **"OK"** on all windows
5. **Restart your terminal** (or reboot your computer)
6. Verify installation:
```bash
ffmpeg -version
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

Verify FFmpeg installation:
```bash
ffmpeg -version
```

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/NEIDTM/TelegramBot-VideoDownloader.git
cd TelegramBot-VideoDownloader
```

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

If you encounter permission errors on Linux/macOS, use:
```bash
pip install --user -r requirements.txt
```

### Step 3: Get Your Bot Token

1. Open Telegram and find [@BotFather](https://t.me/BotFather)
2. Send the command `/newbot`
3. Follow the instructions:
   - Choose a name for your bot (e.g., "My Video Downloader")
   - Choose a username for your bot (must end with 'bot', e.g., "my_video_dl_bot")
4. BotFather will give you a token that looks like:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```
5. **Copy this token** - you'll need it in the next step

### Step 4: Configure the Bot

1. Open the `bot.py` file in any text editor
2. Find this line (near the bottom of the file):
   ```python
   application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
   ```
3. Replace `YOUR_BOT_TOKEN` with your actual token from BotFather:
   ```python
   application = ApplicationBuilder().token("1234567890:ABCdefGHIjklMNOpqrsTUVwxyz").build()
   ```
4. Save the file

### Step 5: Run the Bot

```bash
python bot.py
```

If you see a message like "Application started", your bot is running! 🎉

**Keep the terminal window open** - the bot will stop if you close it.

## 🚀 Usage

### Starting the Bot

1. Make sure the bot is running (see Step 5 above)
2. Open Telegram on your phone or desktop
3. Find your bot by the username you created (e.g., @my_video_dl_bot)
4. Click **"Start"** or send the `/start` command

### Downloading Videos

1. Copy a video link from X (Twitter) or Pinterest
2. Paste the link into the chat with your bot
3. Wait a few seconds - the bot will send you a message confirming the download started
4. The video will be sent to you automatically when ready!

### Supported Platforms

✅ **X (Twitter):**
- `https://twitter.com/username/status/123456789`
- `https://x.com/username/status/123456789`

✅ **Pinterest:**
- `https://pinterest.com/pin/123456789/`
- `https://pin.it/abc123`

### Example

```
You: https://twitter.com/elonmusk/status/123456789

Bot: Your download request has been sent, the video will start downloading in the background.

[A few moments later...]

Bot: [Sends video file]
```

## 📂 Project Structure

After running the bot, your folder will look like this:

```
TelegramBot-VideoDownloader/
├── bot.py                          # Main bot file
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── download_script_[uuid].py       # Temporary scripts (auto-deleted)
└── downloads/                      # Downloaded videos (auto-deleted after sending)
    └── video_[uuid].mp4
```

**Note:** Temporary files are automatically deleted after use to save disk space.


## 🔧 Advanced Configuration

### Running in Background (Linux/macOS)

To keep the bot running after closing the terminal:

```bash
nohup python bot.py &
```

To stop the bot:
```bash
pkill -f bot.py
```

### Running as a Service (Linux)

Create a systemd service file `/etc/systemd/system/videobot.service`:

```ini
[Unit]
Description=Telegram Video Downloader Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/TelegramBot-VideoDownloader
ExecStart=/usr/bin/python3 bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl enable videobot
sudo systemctl start videobot
```

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

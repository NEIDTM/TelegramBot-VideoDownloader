import os
import subprocess
import asyncio
import uuid
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

active_requests = {}

async def download_video(url: str, chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder = current_dir
    os.makedirs(folder, exist_ok=True)

    script_id = str(uuid.uuid4())
    script_filename = os.path.join(folder, f"download_script_{script_id}.py")

    with open(script_filename, 'w', encoding='utf-8') as script_file:
        script_content = f"""
import os
import yt_dlp
import subprocess
import requests

url = "{url}"
chat_id = {chat_id}
bot_token = "{context.bot.token}"
current_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(current_dir, "downloads")
os.makedirs(folder, exist_ok=True)

unique_id = "{uuid.uuid4()}"
video_filename = os.path.join(folder, f'video_{{unique_id}}.%(ext)s')

ydl_opts = {{
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': video_filename,
    'quiet': True,
}}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Starting to upload video...")
        info_dict = ydl.extract_info(url, download=True)
        final_video_filename = ydl.prepare_filename(info_dict)
        print(f"Video downloaded: {{final_video_filename}}")

        mp4_filename = None
        if final_video_filename.endswith('.webm'):
            mp4_filename = os.path.splitext(final_video_filename)[0] + '.mp4'
            subprocess.run(['ffmpeg', '-i', final_video_filename, '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', mp4_filename], check=True)
            if os.path.exists(final_video_filename):
                os.remove(final_video_filename)
            video_to_send = mp4_filename
        else:
            video_to_send = final_video_filename

        if os.path.exists(video_to_send):
            with open(video_to_send, 'rb') as video:
                requests.post(
                    f"https://api.telegram.org/bot{{bot_token}}/sendVideo",
                    data={{'chat_id': chat_id}},
                    files={{'video': video}}
                )
            os.remove(video_to_send)

except Exception as e:
    print(f"Couldn't download the video: {{str(e)}}")

os.remove(__file__)
"""
        script_file.write(script_content)

    try:
        subprocess.Popen(['python', script_filename])
        await context.bot.send_message(chat_id=chat_id, text="Your download request has been sent, the video will start downloading in the background.")
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error running script: {str(e)}")
    
    del active_requests[chat_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hey! Send me a link to a video from X or Pinterest and I will send it to you!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    chat_id = update.message.chat_id
    print(f"Received link: {url}")

    if chat_id in active_requests:
        await context.bot.send_message(chat_id=chat_id, text="Please wait for the previous request to complete.")
        return

    if ("twitter.com" in url or "x.com" in url or 
        "pinterest.com" in url or "pin.it" in url):
        
        active_requests[chat_id] = url
        await download_video(url, chat_id, context)
    else:
        await context.bot.send_message(chat_id=chat_id, text="Please send the correct link to the video from X or Pinterest.")

def main() -> None:
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()

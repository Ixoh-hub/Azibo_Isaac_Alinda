import os
import time
import requests
import schedule
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"✅ Sent: {text}")
    else:
        print(f"❌ Failed: {response.status_code} - {response.text}")

def load_posts():
    try:
        with open(os.path.join(BASE_DIR, "posts.txt"), "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ posts.txt not found.")
        return []

def scheduled_post():
    global posts
    if posts:
        send_telegram_message(posts.pop(0))
    else:
        print("📭 No more scheduled posts.")

if __name__ == "__main__":
    posts = load_posts()

    # 1. Immediate post
    send_telegram_message("Ixoh's ai schedular Y’all 🌍🚀")

    # 2. Schedule 1st post after 10 minutes
    schedule.every(10).minutes.do(scheduled_post).tag("test1")

    # 3. Schedule 2nd post after 20 minutes
    schedule.every(20).minutes.do(scheduled_post).tag("test2")

    # 4. Daily posts at 10:00 AM
    schedule.every().day.at("10:00").do(scheduled_post)

    print("🤖 Telegram Bot running...")
    while True:
        schedule.run_pending()
        time.sleep(30)

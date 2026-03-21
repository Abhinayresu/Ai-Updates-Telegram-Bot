import feedparser
import requests
import google.generativeai as genai 
import os
import time


GEMINI_API_KEY = "AIz...Q" 
TELEGRAM_BOT_TOKEN = "8374..." 
TELEGRAM_CHANNEL = "@aiupdatestelugu"

lock_file = "jimmy.lock" 


if os.path.exists(lock_file):
    if time.time() - os.path.getmtime(lock_file) < 10: 
        print("🚫 Jimmy is already running. Wait 10 seconds and try again!")
        exit()


with open(lock_file, "w") as f:
    f.write("running")


print("🔍 Scanning Elite AI Sources...")

FEEDS = [
    "https://news.mit.edu/rss/topic/artificial-intelligence", 
    "https://www.analyticsvidhya.com/blog/category/machine-learning/feed/",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    "https://emerj.com/feed/",
    "https://news.google.com/rss/search?q=(The+Rundown+AI+OR+Superhuman+AI+OR+The+Neuron+OR+TLDR+AI+OR+Ben's+Bites)+when:24h"
]

all_news_pool = ""
for url in FEEDS:
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]: 
        all_news_pool += f"Source: {feed.feed.get('title', 'AI Source')}\nTitle: {entry.title}\nLink: {entry.link}\n\n"


print("🧠 Ranking Top 3-5 stories...")

try:
    # Stable configuration
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
You are Jimmy, a chill AI News Anchor for the 'AI Updates Telugu' Telegram channel. 
Your audience is Gen-Z CSE students and young entrepreneurs who want the real deal.

MISSION:
1. FILTER the news pool below and select ONLY the TOP 2 or 3 most important stories. 
2. DISCARD anything that isn't absolutely "mind-blowing" or career-changing.
3. FORMAT: Write in plain text. NO bold marks (**), NO markdown headers (###), NO italics. 
4. STYLE: Use a mix of Telugu and English (Vibecoding style). Keep it high-energy.


Rules for Content:
- Start with:"Namasthe mawa! 🚀 Eeroju top 2 updates mathram crazy unnayi..."
- Use simple emojis as bullet points (like ⚡ or 🔥).
- For each story: Give the title, a 1-sentence "Enduku important?" in Telugu, and the link.
- Use HTML for links: <a href="LINK">🔗 Details ikkada</a>

YOUTUBE PROMO:
    Channel: https://www.youtube.com/@Abhinayresu45
    
    CRITICAL RULE: Create a NEW, funny Gen-Z Telugu CTA every day. 
    Don't repeat the same line! Mix it up with different "Mawa" vibes.
    Examples of the vibe (but don't just copy these):
    - "Subscribe chesko mawa, veedu manchi content isthadu ledante night nidra podu."
    - "Anna channel subscribe cheskondi, tech lo thopu avvochu!"
    - "Free ga knowledge isthunnadu, oka sub veyyakapothe ela mawa?"
    - "Veedi content chusthe brain sharp avthadi, subscribe kottu mawa!"

    
STRICT NEGATIVE CONSTRAINTS:
- DO NOT use double asterisks ** anywhere.
- DO NOT use more than 3 stories.
- DO NOT sound like a robot.

Raw News Pool:
{all_news_pool}
"""

    response = model.generate_content(prompt)
    final_post_text = response.text[:4000] 

except Exception as e:
    print(f"❌ AI Error: {e}")
    
    if os.path.exists(lock_file):
        os.remove(lock_file)
    exit()


print("🚀 Jimmy is broadcasting...")
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": TELEGRAM_CHANNEL,
    "text": final_post_text,
    "parse_mode": "HTML",
    "disable_web_page_preview": False
}
telegram_response = requests.post(url, json=payload)

if telegram_response.status_code == 200:
    print("✅ Success! The 'Elite Edition' post is live!")
else:
    print(f"❌ Error: {telegram_response.text}")
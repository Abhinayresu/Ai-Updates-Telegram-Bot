import requests


BOT_TOKEN = "8374...." 


CHANNEL_ID = "@aiupdatestelugu" 

# What Jimmy is going to say
message = "Namasthe mawaa! 🚀 Jimmy the Bot is officially online. Get ready for the latest AI updates!"

# The instructions for Telegram
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

print("Waking Jimmy up and sending message...")

# Firing the message off to the internet
response = requests.post(url, json=payload)

#  Checking if it worked
if response.status_code == 200:
    print("✅ Success! Check your Telegram channel on your phone right now.")
else:
    print(f"❌ Oops, something went wrong: {response.text}")
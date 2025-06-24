#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23480065"))
API_HASH = environ.get("API_HASH", "32edb7d7fc1523b436109bff8ea061fc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7760196814"))
CREDIT = "𝖙𝖍𝖆𝖐𝖚𝖗 𝖇𝖔𝖙𝖘"(https://t.me/StudyXashish)
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

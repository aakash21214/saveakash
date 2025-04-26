# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "12916125")
API_HASH = os.getenv("API_HASH", "dfebf9cc52b859771cf8a1d447e751a5")
BOT_TOKEN = os.getenv("BOT_TOKEN", "2073340158:AAEd_8yntof1ctSZUHptuDLi6oJtSMmkNPI")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://minakshisharma12320:FFEeUVJyHJKFJKa1@cluster0.0ofreqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "1651746145").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1001913986602")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1001817192495")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))

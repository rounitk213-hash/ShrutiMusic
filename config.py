# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ⚙️ CONFIGURATION FILE | Powered By @WTF_WhyMeeh & @ShrutiBots
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("33366736"))
API_HASH = os.getenv("3cdd9d57996df6a3aa8f551913bc1fd9")
BOT_TOKEN = os.getenv("8150846526:AAETRwCp9_wq3W7Yo6clYmGbZMup6Y4VpT4")
OWNER_ID = int(os.getenv("OWNER_ID", 8189688996))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "shdxmr")
BOT_USERNAME = os.getenv("BOT_USERNAME", "DARKANGEL_MUSICBOT")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI", mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", -1003596116023))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/ShrutiMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/abtshd")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+BwsESIsQ4EcxNTg9")
INSTAGRAM = os.getenv("INSTAGRAM", "")
YOUTUBE = os.getenv("YOUTUBE", "")
GITHUB = os.getenv("GITHUB", "")
DONATE = os.getenv("DONATE", "")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", BQJDvkkAj6Z_8cNbqTkylFdYpjR3_8ynb1855S_WpN3pt4F6mR98UTi7EJ1TSyVqIbGKw0bun2C8qDZkDbGi_Ip2n6izrOOJlapXXYN_dsBNbufZpdOXy4h8QXZ4E4Qrm0OH_nJxpMgyzGwpbk3x_HlWvoSijvRWty62Eif8pDd7KdJ2FB-6j51pRRlwjg3sAokIvU9g-lxURbqvHsqWFMycEU8Mc6Aggw8R3F1zsmzLt0jtumyUZph7dzsFHY07wQSFN3OvqnJ0omOlSbjWGfAs9gDYcPNNm430LLBBney2VREJQoSOwZPMDJiBchzgZVxUqBjiD8g1VISbEOYs5hAUE9AiwwAAAAH1lpPAAA)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg")
PING_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/eehxb4.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ✅ CONFIG LOADED SUCCESSFULLY | Designed By @WTF_WhyMeeh
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 

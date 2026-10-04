import os

from dotenv import load_dotenv

load_dotenv()


# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", ",")


# API
NEKOS_BEST_API_URL = os.getenv(
    "NEKOS_BEST_API_URL",
    "https://nekos.best/api/v2"
)


# Database
MONGODB_URI = os.getenv("MONGODB_URI")


# Staff
BOT_OWNER_ID = os.getenv("BOT_OWNER_ID")
CO_OWNER_ID = os.getenv("CO_OWNER_ID")

DEVELOPER_IDS = [
    user_id.strip()
    for user_id in os.getenv("DEVELOPER_IDS", "").split(",")
    if user_id.strip()
]


# Basic validation
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is missing from .env")
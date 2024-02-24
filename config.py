from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f6cabf06615d4bbdc4136.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/781e980163d5a78afeeae.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/About_Info_Devil")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Devilxdiscuss")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/file/a72e3a22e9bc43d35cec9.jpg"

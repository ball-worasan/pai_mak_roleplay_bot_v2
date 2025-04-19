import os
from dotenv import load_dotenv

load_dotenv()

def _env(name: str, default=None, cast=str):
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    return cast(value) if cast is str else cast(value)

DISCORD_API_TOKEN = _env("DISCORD_API_TOKEN")
LOG_DATA_CHANNEL_ID = _env("LOG_DATA_CHANNEL_ID", cast=int)
LOG_JOIN_QUIT_CHANNEL_ID = _env("LOG_JOIN_QUIT_CHANNEL_ID", cast=int)
ROLE_CHANNEL_ID = _env("ROLE_CHANNEL_ID", cast=int)
CHAT_CHANNEL_ID = _env("CHAT_CHANNEL_ID", cast=int)
ROLE = _env("ROLE", cast=int)
ROLE_EMOJI = _env("ROLE_EMOJI")

ANNOUNCEMENTS_CHANNEL_ID = _env("ANNOUNCEMENTS_CHANNEL_ID", cast=int, default=0)
REPORTS_CHANNEL_ID = _env("REPORTS_CHANNEL_ID", cast=int, default=0)
ADMIN_ROLE_ID = _env("ADMIN_ROLE_ID", cast=int, default=None)
SERVER_IP = _env("SERVER_IP", default="pai-roleplay.fun:30120")

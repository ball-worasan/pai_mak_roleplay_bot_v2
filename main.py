import asyncio
import logging
import pathlib
import discord
from discord.ext import commands
from core.logger import setup_logging
from core.embeds import send_embed
import config.settings as setting

setup_logging()
logger = logging.getLogger("bot")

BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"

async def load_dir(bot: commands.Bot, path: pathlib.Path, prefix: str):
    tasks = [
        bot.load_extension(f"{prefix}.{p.stem}")
        for p in path.glob("*.py") if p.stem != "__init__"
    ]
    await asyncio.gather(*tasks, return_exceptions=False)

def create_bot() -> commands.Bot:
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        await load_dir(bot, CMDS_DIR, "cmds")
        await load_dir(bot, COGS_DIR, "cogs")
        logger.info("Bot ready as %s", bot.user)
        await send_embed(
            bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="Bot Started",
            description=f"User: {bot.user} (ID: {bot.user.id})",
            author=bot.user
        )

    return bot

if __name__ == "__main__":
    bot = create_bot()
    bot.run(setting.DISCORD_API_TOKEN)
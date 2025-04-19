import traceback, discord
from discord.ext import commands
import config.settings as setting
from core.embeds import send_embed

class SafeError(commands.Cog):
    """Global error catcher: handles any uncaught errors and logs them."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("ไม่พบคำสั่งนี้ พิมพ์ `!help` เพื่อดูคำสั่งที่ถูกต้อง", delete_after=5)
            return
        await ctx.send(f"เกิดข้อผิดพลาด: {error}", delete_after=10)
        tb = ''.join(traceback.format_exception(type(error), error, error.__traceback__))[:1900]
        await send_embed(self.bot, channel_id=setting.LOG_DATA_CHANNEL_ID,
                         title="Error", description=str(error),
                         description2=f"```{tb}```", color=0xFF5555,
                         author=ctx.author if ctx else None)

async def setup(bot):
    await bot.add_cog(SafeError(bot))
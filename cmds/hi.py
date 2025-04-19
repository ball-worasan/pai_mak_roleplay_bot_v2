from discord.ext import commands
from core.embeds import send_embed
import config.settings as setting

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="ส่งข้อความต้อนรับ")
    async def hi(self, ctx):
        await ctx.send("สวัสดี! ฉันคือ HardCraft Bot")
        await send_embed(
            ctx.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="ใช้คำสั่ง !hi",
            description=f"{ctx.author.display_name} ใช้คำสั่ง !hi",
            author=ctx.author
        )

async def setup(bot):
    await bot.add_cog(Hi(bot))
from discord.ext import commands
from core.embeds import send_embed
import config.settings as setting

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="แสดงข้อความช่วยเหลือ")
    async def help(self, ctx):
        help_text = "**คำสั่งที่มีให้ใช้งาน**\n\n"                         "* `!hi` - ทักทายบอท\n"                         "* `!help` - แสดงหน้าช่วยเหลือ"
        await ctx.send(help_text)
        await send_embed(
            ctx.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="ใช้คำสั่ง !help",
            description=f"{ctx.author.display_name} เปิดหน้าช่วยเหลือ",
            author=ctx.author
        )

async def setup(bot):
    await bot.add_cog(Help(bot))
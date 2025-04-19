"""Send a custom embed message (Manage Messages)"""
from discord.ext import commands
from core.embeds import send_embed
from core.decorators import require_manage_messages
import config.settings as setting

class Msg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="msg", description="ส่ง Embed 1‑3 บรรทัด  !msg <title> [desc] [footer]")
    @require_manage_messages()
    async def msg(self, ctx, title: str, desc: str | None = None, footer: str | None = None):
        await ctx.message.delete()
        await send_embed(
            ctx.bot,
            channel_id=ctx.channel.id,
            title=title,
            description=desc or "",
            description2=footer,
            author=ctx.author
        )
        await send_embed(
            ctx.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="Log !msg",
            description=f"{ctx.author.display_name} ส่ง embed ใน {ctx.channel.mention}",
            author=ctx.author
        )

async def setup(bot):
    await bot.add_cog(Msg(bot))
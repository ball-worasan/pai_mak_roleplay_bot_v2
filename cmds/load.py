"""Hot‑swap extensions (Manage Messages)"""
from discord.ext import commands
from core.decorators import require_manage_messages
from core.embeds import send_embed
import config.settings as setting

class Loader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def _action(self, ctx, op: str, ext_type: str, name: str):
        ext = f"{ext_type}.{name}"
        try:
            if op == "load":
                await self.bot.load_extension(ext)
            elif op == "unload":
                await self.bot.unload_extension(ext)
            elif op == "reload":
                await self.bot.reload_extension(ext)
            await ctx.send(f"{op.title()} `{ext}` สำเร็จ", delete_after=5)
            await send_embed(
                ctx.bot,
                channel_id=setting.LOG_DATA_CHANNEL_ID,
                title=f"{op.title()} extension",
                description=f"{ctx.author.display_name} {op} `{ext}`",
                author=ctx.author
            )
        except Exception as e:
            await ctx.send(f"{op} `{ext}` ล้มเหลว: {e}", delete_after=10)

    @commands.command()
    @require_manage_messages()
    async def load(self, ctx, ext_type: str, name: str):
        await self._action(ctx, "load", ext_type, name)

    @commands.command()
    @require_manage_messages()
    async def unload(self, ctx, ext_type: str, name: str):
        await self._action(ctx, "unload", ext_type, name)

    @commands.command()
    @require_manage_messages()
    async def reload(self, ctx, ext_type: str, name: str):
        await self._action(ctx, "reload", ext_type, name)

async def setup(bot):
    await bot.add_cog(Loader(bot))
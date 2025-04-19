"""Clear messages in a text channel (Manage Messages required)"""
import asyncio
import discord
from discord.ext import commands
from core.embeds import send_embed
from core.decorators import require_manage_messages
import config.settings as setting

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", description="ลบข้อความ (จำนวน | all)")
    @require_manage_messages()
    async def clear(self, ctx, amount: str | None = None):
        await ctx.message.delete()

        if amount is None:
            await ctx.send("โปรดระบุจำนวนหรือ 'all'", delete_after=5)
            return

        if amount.lower() == "all":
            deleted = await ctx.channel.purge()
            await send_embed(
                ctx.bot,
                channel_id=setting.LOG_DATA_CHANNEL_ID,
                title="Clear",
                description=f"{ctx.author.display_name} ลบข้อความทั้งหมด ({len(deleted)}) ใน {ctx.channel.mention}",
                author=ctx.author
            )
            return

        try:
            count = int(amount)
            if not 1 <= count <= 100:
                raise ValueError
        except ValueError:
            await ctx.send("จำนวนต้องเป็น 1‑100 หรือ 'all'", delete_after=5)
            return

        deleted = await ctx.channel.purge(limit=count+1)
        await send_embed(
            ctx.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="Clear",
            description=f"{ctx.author.display_name} ลบ {len(deleted)-1} ข้อความใน {ctx.channel.mention}",
            author=ctx.author
        )

async def setup(bot):
    await bot.add_cog(Clear(bot))
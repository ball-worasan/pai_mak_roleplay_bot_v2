"""Setup reaction‑role verification (Manage Messages)"""
from discord.ext import commands
import discord
from core.decorators import require_manage_messages
from core.embeds import send_embed
import config.settings as setting

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="verify")
    @require_manage_messages()
    async def verify(self, ctx, channel_id: int, message_id: int, emoji: str, role_id: int):
        await ctx.message.delete()

        ch = ctx.guild.get_channel(channel_id)
        role = ctx.guild.get_role(role_id)
        if not ch or not role:
            await ctx.send("Channel/Role ไม่ถูกต้อง", delete_after=5)
            return

        try:
            msg = await ch.fetch_message(message_id)
            await msg.clear_reactions()
            await msg.add_reaction(emoji)
        except discord.NotFound:
            await ctx.send("ไม่พบข้อความ", delete_after=5)
            return

        await send_embed(
            ctx.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="ตั้งค่า Reaction‑Role",
            description=f"{ctx.author.display_name} ตั้งค่าใน {ch.mention}",
            author=ctx.author
        )

async def setup(bot):
    await bot.add_cog(Verify(bot))
from discord.ext import commands
import discord
from core.decorators import require_admin
from core.embeds import send_embed
import config.settings as setting

class AdminCommands(commands.Cog):
    """คำสั่งสำหรับทีมงาน Pai Mak Roleplay"""
    def __init__(self, bot):
        self.bot = bot
        self.promo_message = "ขณะนี้ยังไม่มีโปรโมชั่น"

    # ตั้งข้อความโปรโมชั่น
    @commands.command(name="setpromo", description="ตั้งข้อความโปรโมชั่น")
    @require_admin()
    async def set_promo(self, ctx, *, message: str):
        self.promo_message = message
        await ctx.send("อัปเดตโปรโมชั่นเรียบร้อย")
        await send_embed(
            self.bot,
            channel_id=setting.ANNOUNCEMENTS_CHANNEL_ID,
            title="ประกาศโปรโมชั่นใหม่",
            description=message,
            role_id=None,
            author=ctx.author
        )

    # สร้างประกาศ
    @commands.command(name="announce", description="ประกาศข้อความ (Admin)")
    @require_admin()
    async def announce(self, ctx, title: str, *, message: str):
        await send_embed(
            self.bot,
            channel_id=setting.ANNOUNCEMENTS_CHANNEL_ID,
            title=title,
            description=message,
            role_id=None,
            author=ctx.author
        )
        await ctx.send("ประกาศส่งเรียบร้อย!")

    # จัดการผู้เล่น (kick)
    @commands.command(name="kick", description="เตะผู้ใช้ (Admin)")
    @require_admin()
    async def kick_member(self, ctx, member: discord.Member, *, reason: str = "ไม่ระบุ"):
        await member.kick(reason=reason)
        await send_embed(
            self.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="Kick สมาชิก",
            description=f"{member} ถูกเตะโดย {ctx.author}",
            description2=f"เหตุผล: {reason}",
            author=ctx.author
        )
        await ctx.send(f"เตะ {member.display_name} เรียบร้อย")

    # จัดการผู้เล่น (ban)
    @commands.command(name="ban", description="แบนผู้ใช้ (Admin)")
    @require_admin()
    async def ban_member(self, ctx, member: discord.Member, *, reason: str = "ไม่ระบุ"):
        await member.ban(reason=reason)
        await send_embed(
            self.bot,
            channel_id=setting.LOG_DATA_CHANNEL_ID,
            title="Ban สมาชิก",
            description=f"{member} ถูกแบนโดย {ctx.author}",
            description2=f"เหตุผล: {reason}",
            author=ctx.author
        )
        await ctx.send(f"แบน {member.display_name} เรียบร้อย")

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
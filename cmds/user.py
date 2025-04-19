from discord.ext import commands
import config.settings as setting
from core.embeds import send_embed

class UserCommands(commands.Cog):
    """คำสั่งทั่วไปสำหรับผู้เล่น Pai Mak Roleplay"""
    def __init__(self, bot):
        self.bot = bot

    # แสดง IP และสถานะคร่าวๆ
    @commands.command(name="server", description="ดู IP และข้อมูลเบื้องต้นของเซิร์ฟเวอร์")
    async def server_info(self, ctx):
        await ctx.send(f"Pai Mak Roleplay IP: `{setting.SERVER_IP}`\nเข้ามาเล่นกันได้เลย!")

    # ดูโปรโมชั่นปัจจุบัน
    @commands.command(name="promo", description="ดูโปรโมชั่นล่าสุด")
    async def current_promo(self, ctx):
        promo = self.bot.get_cog("AdminCommands").promo_message if self.bot.get_cog("AdminCommands") else "ขณะนี้ยังไม่มีโปรโมชั่น"
        await ctx.send(promo)

    # รายงานปัญหา / ผู้เล่น
    @commands.command(name="report", description="รายงานปัญหาหรือผู้เล่น (ใช้ !report <ข้อความ>)")
    async def report(self, ctx, *, message: str | None = None):
        if not message:
            await ctx.send("โปรดพิมพ์รายละเอียดหลังคำสั่ง เช่น `!report มีผู้เล่นโกงที่เส้น 1`")
            return
        await send_embed(
            self.bot,
            channel_id=setting.REPORTS_CHANNEL_ID,
            title="รายงานใหม่",
            description=f"จาก {ctx.author.mention}",
            description2=message,
            author=ctx.author,
            role_id=None
        )
        await ctx.send("รับรายงานแล้ว ทีมงานจะตรวจสอบโดยเร็วที่สุด ขอบคุณ!")

async def setup(bot):
    await bot.add_cog(UserCommands(bot))
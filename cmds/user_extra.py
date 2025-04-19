"""Additional user-facing commands (>10)"""
from discord.ext import commands
from core.embeds import send_embed
import config.settings as setting
import random, time

class ExtraUserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    # 1
    @commands.command(name="rules")
    async def show_rules(self, ctx):
        rules = "**กฎหลักของ Pai Mak Roleplay**\n1. ห้ามใช้โปรแกรมโกง\n2. ห้ามพฤติกรรม Toxic\n3. ... (ดูรายละเอียดเพิ่มเติมในเว็บไซต์)"
        await ctx.send(rules)

    # 2
    @commands.command(name="discord")
    async def invite_link(self, ctx):
        await ctx.send("กดเพื่อเข้าดิสคอร์ดสำรอง: https://discord.gg/example")

    # 3
    @commands.command(name="website")
    async def website(self, ctx):
        await ctx.send("เว็บไซต์หลัก: https://pai-mak-roleplay.example.com")

    # 4
    @commands.command(name="uptime")
    async def uptime(self, ctx):
        secs = int(time.time() - self.start_time)
        hrs, rest = divmod(secs, 3600)
        mins, secs = divmod(rest, 60)
        await ctx.send(f"บอทออนไลน์มาแล้ว {hrs}h {mins}m {secs}s")

    # 5
    @commands.command(name="playercount")
    async def player_count(self, ctx):
        # _stub_: replace with query to FiveM if needed
        players = random.randint(0, 64)
        await ctx.send(f"จำนวนผู้เล่นในเซิร์ฟเวอร์ตอนนี้: {players}/64")

    # 6
    @commands.command(name="staff")
    async def staff_list(self, ctx):
        await ctx.send("ทีมงานหลัก: admin1, admin2, support1...")

    # 7
    @commands.command(name="donate")
    async def donate_info(self, ctx):
        await ctx.send("สนับสนุนเซิร์ฟเวอร์ได้ที่ https://boosty.example.com/pai-mak")

    # 8
    @commands.command(name="jobs")
    async def list_jobs(self, ctx):
        jobs = ["ตำรวจ", "หมอ", "แท็กซี่", "นักขุดแร่", "เมสเซนเจอร์"]
        await ctx.send("งานที่มีใน Pai Mak RP: " + ", ".join(jobs))

    # 9
    @commands.command(name="vehicles")
    async def vehicle_shop(self, ctx):
        await ctx.send("ดูรายการรถได้ที่โชว์รูมภายในเกม หรือ /vehicleshop")

    # 10
    @commands.command(name="faq")
    async def faq(self, ctx):
        await ctx.send("คำถามที่พบบ่อย: https://pai-mak-roleplay.example.com/faq")

    # 11
    @commands.command(name="event")
    async def next_event(self, ctx):
        await ctx.send("กิจกรรมถัดไป: แข่งรถวันศุกร์ 20:00 น. เจอกัน!")

    # 12
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency*1000)} ms")

async def setup(bot):
    await bot.add_cog(ExtraUserCommands(bot))
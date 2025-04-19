"""Additional admin‑only commands (>10)"""
from discord.ext import commands, tasks
import discord, asyncio
from core.embeds import send_embed
from core.decorators import require_admin
import config.settings as setting
import datetime

class ExtraAdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1
    @commands.command(name="whitelist")
    @require_admin()
    async def whitelist(self, ctx, member: discord.Member):
        await ctx.send(f"เพิ่ม {member.display_name} เข้าสู่ whitelist (stub)")

    # 2
    @commands.command(name="unwhitelist")
    @require_admin()
    async def unwhitelist(self, ctx, member: discord.Member):
        await ctx.send(f"ลบ {member.display_name} ออกจาก whitelist (stub)")

    # 3
    @commands.command(name="addrole")
    @require_admin()
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"เพิ่ม role {role.name} ให้ {member.display_name}")

    # 4
    @commands.command(name="removerole")
    @require_admin()
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"ลบ role {role.name} จาก {member.display_name}")

    # 5
    @commands.command(name="mute")
    @require_admin()
    async def mute(self, ctx, member: discord.Member, minutes: int = 10):
        await ctx.send(f"ปิดเสียง {member.display_name} {minutes} นาที (stub)")

    # 6
    @commands.command(name="unmute")
    @require_admin()
    async def unmute(self, ctx, member: discord.Member):
        await ctx.send(f"เปิดเสียง {member.display_name} (stub)")

    # 7
    @commands.command(name="slowmode")
    @require_admin()
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"ตั้ง slowmode {seconds}s สำเร็จ")

    # 8
    @commands.command(name="lock")
    @require_admin()
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("ห้องนี้ถูกล็อกแล้ว")

    # 9
    @commands.command(name="unlock")
    @require_admin()
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("ห้องนี้ถูกปลดล็อกแล้ว")

    # 10
    @commands.command(name="purge")
    @require_admin()
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"ลบ {len(deleted)-1} ข้อความเรียบร้อย", delete_after=5)

    # 11
    @commands.command(name="poll")
    @require_admin()
    async def poll(self, ctx, duration_minutes: int, *, question: str):
        msg = await ctx.send(
            f"📊 **{question}**\\nโหวต 👍 / 👎 (สิ้นสุดภายใน {duration_minutes} นาที)"
        )
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

        await asyncio.sleep(duration_minutes * 60)

        new_msg = await ctx.channel.fetch_message(msg.id)
        ups   = discord.utils.get(new_msg.reactions, emoji='👍').count - 1
        downs = discord.utils.get(new_msg.reactions, emoji='👎').count - 1
        await ctx.send(f"ผลโหวต: 👍 {ups} | 👎 {downs}")


    # 12
    @commands.command(name="schedule")
    @require_admin()
    async def schedule_announcement(self, ctx, time_str: str, *, message: str):
        """Schedule announce HH:MM 24h format"""
        target = datetime.datetime.strptime(time_str, "%H:%M").time()
        await ctx.send(f"จะประกาศข้อความตามตาราง {time_str}")
        # stub actual scheduling; production use tasks.loop

    # 13
    @commands.command(name="announceimg")
    @require_admin()
    async def announce_image(self, ctx, title: str, url: str):
        embed = discord.Embed(title=title, color=0xFAD5B0)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    # 14
    @commands.command(name="giveitem")
    @require_admin()
    async def give_item(self, ctx, member: discord.Member, item: str, amount: int = 1):
        await ctx.send(f"ให้ {item} x{amount} แก่ {member.display_name} (stub)")

    # 15
    @commands.command(name="setmoney")
    @require_admin()
    async def set_money(self, ctx, member: discord.Member, amount: int):
        await ctx.send(f"ตั้งเงิน {member.display_name} = {amount}$ (stub)")

    # 16
    @commands.command(name="tp")
    @require_admin()
    async def teleport(self, ctx, member: discord.Member, x: float, y: float, z: float):
        await ctx.send(f"เทเลพอร์ต {member.display_name} ไปพิกัด ({x},{y},{z}) (stub)")

    # 17
    @commands.command(name="setjob")
    @require_admin()
    async def set_job(self, ctx, member: discord.Member, job: str):
        await ctx.send(f"ตั้งอาชีพ {member.display_name} เป็น {job} (stub)")

    # 18
    @commands.command(name="revive")
    @require_admin()
    async def revive(self, ctx, member: discord.Member):
        await ctx.send(f"ชุบชีวิต {member.display_name} (stub)")

    # 19
    @commands.command(name="weather")
    @require_admin()
    async def set_weather(self, ctx, weather: str):
        await ctx.send(f"เปลี่ยนสภาพอากาศเป็น {weather} (stub)")

    # 20
    @commands.command(name="settime")
    @require_admin()
    async def set_time(self, ctx, hour: int, minute: int = 0):
        await ctx.send(f"ตั้งเวลาในเกม {hour:02d}:{minute:02d} (stub)")

async def setup(bot):
    await bot.add_cog(ExtraAdminCommands(bot))
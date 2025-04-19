import discord
from itertools import cycle
from discord.ext import commands, tasks


class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status = cycle([
            "HardCraft Server!",
            "Version 1.21",
            "โปรโมชั่นเติมเงิน x1.5",
            "IP : hardcraft.fun"
        ])

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.status_loop.is_running():
            self.status_loop.start()

    @tasks.loop(minutes=1)
    async def status_loop(self):
        await self.bot.change_presence(activity=discord.Game(next(self.status)))

    @status_loop.before_loop
    async def before_status_loop(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(StatusCog(bot))
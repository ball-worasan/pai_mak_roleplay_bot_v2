import functools, traceback
from discord.ext import commands
from core.embeds import send_embed
import config.settings as setting

def require_admin():
    admin_role_id = getattr(setting, "ADMIN_ROLE_ID", None)
    def deco(func):
        @functools.wraps(func)
        async def wrap(self, ctx, *args, **kwargs):
            if ctx.author.guild_permissions.manage_guild:
                return await func(self, ctx, *args, **kwargs)
            if admin_role_id:
                role = ctx.guild.get_role(admin_role_id)
                if role and role in ctx.author.roles:
                    return await func(self, ctx, *args, **kwargs)
            await ctx.send("คุณไม่มีสิทธิ์ใช้งานคำสั่งนี้", delete_after=5)
        return wrap
    return deco

def require_manage_messages():
    def deco(func):
        @functools.wraps(func)
        async def wrap(self, ctx, *args, **kwargs):
            if ctx.author.guild_permissions.manage_messages:
                return await func(self, ctx, *args, **kwargs)
            await ctx.send("ต้องมีสิทธิ์ Manage Messages", delete_after=5)
        return wrap
    return deco

def safe_command():
    """Wrap command to catch unexpected errors and log them."""
    def deco(func):
        @functools.wraps(func)
        async def wrap(self, ctx, *args, **kwargs):
            try:
                return await func(self, ctx, *args, **kwargs)
            except commands.CommandError:
                raise
            except Exception as e:
                tb = ''.join(traceback.format_exception(type(e), e, e.__traceback__))[:1500]
                await ctx.send(f"เกิดข้อผิดพลาดภายในคำสั่ง: {e}", delete_after=10)
                await send_embed(ctx.bot, channel_id=setting.LOG_DATA_CHANNEL_ID,
                                 title="Unhandled Exception", description=str(e),
                                 description2=f"```{tb}```", author=ctx.author, color=0xFF0000)
        return wrap
    return deco
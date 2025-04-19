from __future__ import annotations
import discord
from discord.ext import commands

DEFAULT_COLOR = 0xFAD5B0


async def send_embed(
    bot: commands.Bot,
    *,
    channel_id: int,
    title: str,
    description: str,
    description2: str | None = None,
    color: int = DEFAULT_COLOR,
    role_id: int | None = None,
    author: discord.abc.User | str | None = None,
    icon_url: str | None = None,
) -> None:
    """Utility to build and send an embed message safely."""
    channel = bot.get_channel(channel_id)
    if channel is None:
        raise ValueError(f"Channel {channel_id} not found")

    if description2:
        description = f"{description}\n{description2}"

    if not (0 <= color <= 0xFFFFFF):
        color = DEFAULT_COLOR

    embed = discord.Embed(title=title, description=description, color=color)

    if author:
        name = getattr(author, "display_name", str(author))
        avatar = getattr(author, "avatar", None)
        icon = icon_url or (avatar.url if avatar else None)  # None = ไม่ส่งค่า
        embed.set_author(name=name, icon_url=icon)

    if role_id:
        await channel.send(f"<@&{role_id}>")

    await channel.send(embed=embed)

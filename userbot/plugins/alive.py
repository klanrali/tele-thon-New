"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No Name set yet. iqthon."

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit(" - 𖡻 TeleThon For Arabic 𖢕 \n"
                     " - 𖡻 Version: 1.0.3 𖢕\n"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     " - 𖡻 orders : Here 𖢕\n"
                     " - 𖡻 Source : Here 𖢕\n"
                    f" - 𖡻 My Master : {DEFAULTUSER} 𖢕\n")

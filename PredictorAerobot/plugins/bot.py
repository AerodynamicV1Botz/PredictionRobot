import os
import asyncio
import sys
import git
import heroku3
# Changed root to SpamFighterAerobot
from SpamFighterAerobot import BOT0, BOT1
from SpamFighterAerobot import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from SpamFighterAerobot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from SpamFighterAerobot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime


Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%ssudoadd(?: |$)(.*)" % hl))
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%ssudoadd@SpamFighter_Aerobot(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%ssudoadd(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%ssudoadd@SpamFighter_Aerobot(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        AERO = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[AERO] = newsudo   

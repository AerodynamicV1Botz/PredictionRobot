import os
import asyncio
import sys
import heroku3
# Changed root to SpamFighterAerobot
from aerobot import app
from pyrogram import Client, filters
from pyrogram.types import Message
from Config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY


Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@Client.on_message(filters.user(OWNER_ID) & filters.user(SUDO_USERS) & filters.command("addsudo"))
@Client.on_message(filters.user(OWNER_ID) & filters.user(SUDO_USERS) & filters.command("addsudo@PredictorAerobot"))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        AERO = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.Config()
        if msg is None:
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

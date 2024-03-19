from pyrogram import filters, Client 

from .aerobot import app
from PredictorAerobot.misc import SUDOERS
from PredictorAerobot.utils.database import add_off, add_on
from PredictorAerobot.utils.decorators.language import language


@Client.on_message(filters.command(["logger"]) & SUDOERS)
@language
async def logger(bot, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)

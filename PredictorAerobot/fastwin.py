from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import FASTWIN_IMG

# Fastwin Message
@Client.on_message(filters.private & filters.incoming & filters.command("fastwin"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin@PredictorAerobot"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin"))
async def _fastwin(bot, msg):
    await msg.reply_photo(
        FASTWIN_IMG,
        caption=Data.FASTWIN,
        reply_markup=InlineKeyboardMarkup(Data.fasthome_buttons)
                  )

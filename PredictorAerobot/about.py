from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Config import START_IMG

# Help Message
@Client.on_message(filters.private & filters.command("about@PredictorAerobot"))
@Client.on_message(filters.private & filters.command("about"))
async def _about(bot, msg):
    await msg.reply_photo(START_IMG,
        caption=Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.about_buttons)
        )

from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Config import START_IMG

# Help Message
@Client.on_message(filters.private & filters.command("chat@PredictorAerobot"))
@Client.on_message(filters.private & filters.command("chat"))
async def chat(bot, msg):
    await msg.reply_photo(START_IMG,
        caption=Data.CHAT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.about_back)
        )
  

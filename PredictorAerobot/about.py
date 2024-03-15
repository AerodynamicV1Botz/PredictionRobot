from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import START_IMG

# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("about"))
@Client.on_message(filters.text & filters.incoming & filters.command("about@Aero_Force2_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("about@Aero_Force_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("about"))
async def _about(bot, msg):
    await msg.reply_photo(
        START_IMG,
        caption=Data.ABOUT,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

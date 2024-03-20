from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Data import START_IMG

# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
@Client.on_message(filters.text & filters.incoming & filters.command("help@PredictorAerobot"))
@Client.on_message(filters.text & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await msg.reply_photo(
        START_IMG,
        caption="**Here's How to Use Me ?**\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

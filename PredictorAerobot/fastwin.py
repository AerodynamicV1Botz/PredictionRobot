from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import START_IMG

# Fastwin Message
@Client.on_message(filters.private & filters.incoming & filters.command("fastwin"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin@Aero_Force2_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin@Aero_Force_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin"))
async def _fastwin(bot, msg):
    await msg.reply_photo(
        START_IMG,
        caption="**Here's How to Use Me ?**\n" + Data.FASTWIN ,
        reply_markup=InlineKeyboardMarkup(Data.fasthome_buttons)
                  )

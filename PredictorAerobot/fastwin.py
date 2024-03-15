from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Data import FASTWIN_IMG
import random 

# Start Message
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin"))
@Client.on_message(filters.private & filters.incoming & filters.command("fastwin"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin@PredictorAerobot"))
async def fastwin(bot, msg):
	await msg.reply_photo(
	random.choice(FASTWIN_IMG),
	caption=Data.FASTWIN,
	reply_markup=InlineKeyboardMarkup(Data.fastwinbuttons)
	)

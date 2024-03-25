from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Aero import FASTWIN_IMG
import random 

# Start Message
@Client.on_message(filters.private & filters.command("fastwin"))
@Client.on_message(filters.private & filters.command("fastwin@PredictorAerobot"))
async def fastwin(bot, msg):
	await msg.reply_photo(
	random.choice(FASTWIN_IMG),
	caption=Data.FASTWIN,
	reply_markup=InlineKeyboardMarkup(Data.fastwinbuttons)
	)
@Client.on_message(filters.group & filters.command("fastwin"))
@Client.on_message(filters.group & filters.command("fastwin@PredictorAerobot"))
async def fastwin(bot, msg):
	await msg.reply_photo(
	random.choice(FASTWIN_IMG),
	caption=Data.FASTWIN,
	reply_markup=InlineKeyboardMarkup(Data.fastwinbuttons)
	)

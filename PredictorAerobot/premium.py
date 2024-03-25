from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Config import START_IMG
import random 

# Start Message
@Client.on_message(filters.private & filters.command("premium"))
@Client.on_message(filters.private & filters.command("premium@PredictorAerobot"))
async def premium(bot, msg):
	await msg.reply_photo(START_IMG,
	caption=Data.PREMIUM,
	reply_markup=InlineKeyboardMarkup(Data.paymemthome)
  )

# Start Message
@Client.on_message(filters.group & filters.command("premium"))
@Client.on_message(filters.group & filters.command("premium@PredictorAerobot"))
async def premium(bot, msg):
	await msg.reply_photo(START_IMG,
	caption=Data.PREMIUM,
	reply_markup=InlineKeyboardMarkup(Data.paymemthome)
			     )
	

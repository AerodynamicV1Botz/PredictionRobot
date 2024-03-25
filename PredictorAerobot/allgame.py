from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Config import START_IMG
import random 

# Start Message
@Client.on_message(filters.private & filters.command("allgame"))
@Client.on_message(filters.private & filters.command("allgame@PredictorAerobot"))
async def allgame(bot, msg):
	await msg.reply_photo(START_IMG,
	caption=Data.ALLGAME,
	reply_markup=InlineKeyboardMarkup(Data.allgamebuttons)
  )
# Start Message
@Client.on_message(filters.group & filters.command("allgame"))
@Client.on_message(filters.group & filters.command("allgame@PredictorAerobot"))
async def allgame(bot, msg):
	await msg.reply_photo(START_IMG,
	caption=Data.ALLGAME,
	reply_markup=InlineKeyboardMarkup(Data.allgamebuttons)
        )
	

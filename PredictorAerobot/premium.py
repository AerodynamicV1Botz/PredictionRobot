from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Data import START_IMG
import random 

# Start Message
@Client.on_message(filters.text & filters.incoming & filters.command("premium"))
@Client.on_message(filters.private & filters.incoming & filters.command("premium"))
@Client.on_message(filters.text & filters.incoming & filters.command("premium@PredictorAerobot"))
async def premium(bot, msg):
	await msg.reply_photo(
	random.choice(START_IMG),
	caption=Data.PREMIUM_SUBSCRIPTION,
	reply_markup=InlineKeyboardMarkup(Data.premiumbuttons)
  )

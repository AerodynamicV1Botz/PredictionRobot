from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Data import PAYMENT_IMG
import random 

# Start Message
@Client.on_message(filters.text & filters.incoming & filters.command("payment"))
@Client.on_message(filters.private & filters.incoming & filters.command("payment"))
@Client.on_message(filters.text & filters.incoming & filters.command("payment@PredictorAerobot"))
async def payment(bot, msg):
	await msg.reply_photo(
	random.choice(PAYMENT_IMG),
	caption=Data.PAYMENT,
	reply_markup=InlineKeyboardMarkup(Data.paymentbuttons)
  )

from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message 
from Data import PAYMENT_IMG
import random 

# Start Message
@Client.on_message(filters.text & filters.incoming & filters.command("qr"))
@Client.on_message(filters.private & filters.incoming & filters.command("qr"))
@Client.on_message(filters.text & filters.incoming & filters.command("qr@PredictorAerobot"))
async def qr(bot, msg):
	await msg.reply_photo(
	random.choice(PAYMENT_IMG),
	caption=Data.QR,
	reply_markup=InlineKeyboardMarkup(Data.qrbuttons)
  )

# Start Group Message
@Client.on_message(filters.group & filters.command("qr"))
@Client.on_message(filters.group & filters.command("qr"))
@Client.on_message(filters.group & filters.command("qr@PredictorAerobot"))
async def qr(bot, msg):
	await msg.reply_photo(
	random.choice(PAYMENT_IMG),
	caption=Data.QR,
	reply_markup=InlineKeyboardMarkup(Data.qrbuttons)
	)

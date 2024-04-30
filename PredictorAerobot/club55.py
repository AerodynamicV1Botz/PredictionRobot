from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Config import START_IMG
import random 

# Start Group Message 
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("55club"))
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("55club@PredictorAerobot"))
async def club55_gp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.CLUB55.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.club55_group_buttons)
			     )
	
@Client.on_message(filters.private & filters.command("55club"))
@Client.on_message(filters.private & filters.command("55club@PredictorAerobot"))
async def club55(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.CLUB55.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.club55_buttons)
			     )
	

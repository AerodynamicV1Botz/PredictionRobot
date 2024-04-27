from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Config import START_IMG
import random 

# Start Group Message 
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("lucknow"))
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("lucknow@PredictorAerobot"))
async def lucknow_gp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.LUCKNOW.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.lucknow_group_buttons)
			     )
	
@Client.on_message(filters.private & filters.command("lucknow"))
@Client.on_message(filters.private & filters.command("lucknow@PredictorAerobot"))
async def lucknow(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.LUCKNOW.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.lucknow_buttons)
			     )
	

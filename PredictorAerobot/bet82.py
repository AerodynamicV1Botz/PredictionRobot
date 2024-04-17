from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Config import START_IMG
import random 

# Start Group Message 
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("82lottery"))
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("82lottery@PredictorAerobot"))
async def bet82_gp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.BET82.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.bet82_group_buttons)
			     )
	
@Client.on_message(filters.private & filters.command("82lottery"))
@Client.on_message(filters.private & filters.command("82lottery@PredictorAerobot"))
async def bet82(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.BET82.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.bet82_buttons)
			     )
	

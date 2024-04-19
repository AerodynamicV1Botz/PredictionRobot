from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Data import GOAGAMESIZE
import random 

# Bounty Game Wingo Prediction 
async def ggwingogp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(GOAGAMESIZE),
	caption=Data.GGRESULT.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.goagame_group_buttons)
	)

async def ggwingo(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(GOAGAMESIZE),
	caption=Data.GGRESULT.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.goagame_result_buttons)
	)
						    

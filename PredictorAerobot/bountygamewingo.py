from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Data import BOUNTYGAMESIZE
import random 

# Bounty Game Wingo Prediction 
async def bountygamewingogp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(BOUNTYGAMESIZE),
	caption=Data.BOUNTYGAMERESULT.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.bountygame_group_buttons)
	)

async def bountygamewingo(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(BOUNTYGAMESIZE),
	caption=Data.BOUNTYGAMERESULT.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.bountygame_result_buttons)
	)
						    

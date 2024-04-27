from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Config import START_IMG
import random 

# Start Group Message 
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("okwin"))
@Client.on_message(filters.text & filters.group & filters.incoming & filters.command("okwin@PredictorAerobot"))
async def okwin_gp(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.OKWIN.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.okwin_group_buttons)
			     )
	
@Client.on_message(filters.private & filters.command("okwin"))
@Client.on_message(filters.private & filters.command("okwin@PredictorAerobot"))
async def okwin(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.OKWIN.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.okwin_buttons)
			     )
	

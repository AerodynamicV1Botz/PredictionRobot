from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Config import START_IMG
import random 

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
@Client.on_message(filters.private & filters.incoming & filters.command("start@PredictorAerobot"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.START.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.start_buttons)
	)
# Start Group Message 
@Client.on_message(filters.text & filters.incoming & filters.command("start"))
@Client.on_message(filters.text & filters.incoming & filters.command("start@PredictorAerobot"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
	caption=Data.START.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.start_group_buttons)
        )


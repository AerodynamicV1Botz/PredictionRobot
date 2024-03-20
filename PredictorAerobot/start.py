from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

# Start Message
@Client.on_message(filters.group & filters.command("start"))
@Client.on_message(filters.group & filters.command("start@PredictorAerobot"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(https://graph.org/file/4a0df73c438e618ac337d.jpg"),
	caption=Data.START.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.startbuttons)
                       )

@Client.on_message(filters.private & filters.command("start"))
@Client.on_message(filters.private & filters.command("start@FunWinPredictorAerobot"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(https://graph.org/file/4a0df73c438e618ac337d.jpg),
	caption=Data.START.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.buttons)
			     )

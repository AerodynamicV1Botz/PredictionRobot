from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
from Data import DFASTPARITY_IMG

# Start Message
@Client.on_message(filters.text & filters.incoming & filters.command("fastparity"))
@Client.on_message(filters.private & filters.incoming & filters.command("fastparity"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastparity@PredictorAerobot"))
async def fastparity(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(DFASTPARITY_IMG),
	caption=Data.FASTPARITY.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.gamebuttons)
	)

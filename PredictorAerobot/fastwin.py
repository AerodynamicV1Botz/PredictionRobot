from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from Data import FASTWIN_IMG

# Fastwin Message
@Client.on_message(filters.private & filters.incoming & filters.command("fastwin"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin@PredictorAerobot"))
@Client.on_message(filters.text & filters.incoming & filters.command("fastwin"))
async def _fastwin(_, msg: Message):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(FASTWIN_IMG),
	caption=Data.FASTWIN.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.fastwinbuttons)
    )

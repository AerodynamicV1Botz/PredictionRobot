from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto
from Data import FUNWINFASTPARITY_IMG
import random 
from Config import OWNER_ID, SUDO_ID, SUDO_ID1, SUDO_ID2, SUDO_ID3

@Client.on_message(filters.user([OWNER_ID, SUDO_ID, SUDO_ID1, SUDO_ID2, SUDO_ID3]) & filters.command([

  
  
  
  
  
  

  
  
  
  
async def funwinfast(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(
	random.choice(FUNWINFASTPARITY_IMG),
	caption=Data.FUNWINFAST.format(msg.from_user.mention, mention),
	reply_markup=InlineKeyboardMarkup(Data.gamebuttons)
  )

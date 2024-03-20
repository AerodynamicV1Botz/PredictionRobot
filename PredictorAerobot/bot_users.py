from PredictorAerobot.database.users_sql import Users, num_users
from PredictorAerobot.database.chats_sql import num_chats
from PredictorAerobot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message
from Config import OWNER_ID, SUDO_ID

@Client.on_message( ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(OWNER_ID) & filters.user(SUDO_ID) & filters.command("stats"))
@Client.on_message(filters.user(OWNER_ID) & filters.user(SUDO_ID) & filters.command("stats@PredictorAerobot"))
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"**About This Bot** \n\nThis is Aero ✘ Force Subscriber~🇮🇳 \nA powerful Telegram subscribing bot to force users in your group to join a particular chat. \n──────────────────── \n➻ Users ≈ {users} \n➻ Chats ≈ 1{chats} \n──────────────────── \n★Network » @AerodynamicV1Botz \n★Developer » @AerodynamicV1_OFFICIAL \n★Update » @AerodynamicV1_UPDATE \n★Support » @AerodynamicV1_SUPPORT \n★Free Promotion » @AerodynamicV1_Promotion", quote=True)

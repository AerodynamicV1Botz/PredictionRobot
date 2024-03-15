from pyrogram import Client, filters


@Client.on_message(filters.text & filters.incoming & filters.command("id"))
@Client.on_message(filters.text & filters.incoming & filters.command("id@PredictorAerobot"))
async def id(_, msg):
    await msg.reply(f"Chat ID is : `{msg.chat.id}`", quote=True)

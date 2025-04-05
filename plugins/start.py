from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from config import START_IMG, JOIN_LINK

def register(app):
    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Join", url=JOIN_LINK)],
            [InlineKeyboardButton("👑 Owner", url="https://t.me/yourusername")],
            [InlineKeyboardButton("❓ Help", callback_data="help")],
            [InlineKeyboardButton("ℹ️ About", callback_data="about")]
        ])

        await message.reply_photo(
            photo=START_IMG,
            caption=f"""Hᴇʟʟᴏ {message.from_user.mention},\n
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ【ꜱᴘᴀᴍ & ʀᴀɪᴅ】ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ ᴀɴᴅ ʙᴇꜱᴛ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴄʀᴇᴀᴛᴇ Yᴏᴜʀ Oᴡɴ【ꜱᴘᴀᴍ & ʀᴀɪᴅ】ʙᴏᴛ""",
            reply_markup=keyboard
        )

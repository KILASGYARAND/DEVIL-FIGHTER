from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    if callback_query.data == "help":
        await callback_query.message.edit("**This bot helps you raid with fun galiyaan! Use /raid to start.**")

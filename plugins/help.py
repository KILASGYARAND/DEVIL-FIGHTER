from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    text = "**Available Commands:**\n\n" \
           "/raid - Start raiding the chat\n" \
           "/stopraid - Stop the ongoing raid\n" \
           "/target - Mention target user (Reply to user)\n" \
           "/setgali - Set custom galiyaan\n" \
           "/galilist - View current galiyaan"
    await message.reply(text)

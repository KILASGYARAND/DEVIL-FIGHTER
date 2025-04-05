from pyrogram import filters
from pyrogram.handlers import MessageHandler
import random

# Sample raid messages
raid_messages = [
    "Arey tu toh noob nikla!",
    "Tera dimaag reboot maang raha hai!",
    "Group raid ho gaya bhai!",
    "Kaun bola tujhe smart hai?",
    "Thoda chill kar, logic leak ho raha hai!",
    "Ye group ab hamare kabze me hai!",
    "Telegram pe aake bhi sense nahi seekha!"
]

async def raid_command(client, message):
    if message.chat.type not in ["group", "supergroup"]:
        await message.reply("Bhai ye command sirf groups me hi kaam karta hai.")
        return
    for _ in range(10):  # Send 10 raid messages
        await message.reply(random.choice(raid_messages))

raid_handler = MessageHandler(raid_command, filters.command("raid"))

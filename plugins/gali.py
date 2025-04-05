from pyrogram import Client, filters
import json
from config import GALI_JSON, OWNER_ID

def load_gali():
    with open(GALI_JSON, "r") as f:
        return json.load(f)

def save_gali(data):
    with open(GALI_JSON, "w") as f:
        json.dump(data, f, indent=2)

@Client.on_message(filters.command("setgali") & filters.user(OWNER_ID))
async def set_gali(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.reply("Usage: `/setgali gali1|gali2|gali3`", quote=True)
        return
    new_gali = args[1].split("|")
    data = load_gali()
    data["custom"] = new_gali
    save_gali(data)
    await message.reply("Custom galiyaan set successfully!")

@Client.on_message(filters.command("galilist"))
async def list_gali(client, message):
    data = load_gali()
    text = "**Default Galiyan:**\n" + "\n".join(data["default"]) + "\n\n"
    if data["custom"]:
        text += "**Custom Galiyan:**\n" + "\n".join(data["custom"])
    await message.reply(text)

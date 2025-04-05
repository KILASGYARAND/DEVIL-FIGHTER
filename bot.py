from pyrogram import Client
from plugins import start, help, raid, gali, callbacks

app = Client("devil fighter", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Add all handlers
start.register(app)
help.register(app)
raid.register(app)
gali.register(app)
callbacks.register(app)

app.run()

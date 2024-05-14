import os
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message

from ngrok import connect

api_id = os.getenv('API_ID', 0)
api_hash = os.getenv('API_HASH', '')
bot_token = os.getenv('BOT_TOKEN', '')

app = Client(
    name="cache",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(bot: Client, msg: Message):
    await msg.reply_text("""Hello!
use /mine for run server minecraft!""")

@app.on_message(filters.command("mine"))
async def run_server_ngrok(bot: Client, msg: Message):
    public_url = connect(token, 25565, 'us')
    message = f'ngrok connected! URL: {public_url}\n'
    await msg.reply_text(message)

print("running")
app.run()

import os
os.system("pip3 install pyrogram==1.4.16")
os.system("pip3 install TgCrypto")
os.system("pip3 install async-lru")
os.system("pip3 install PySocks")
os.system("pip3 install pyaes")

import asyncio
from pyrogram import Client,filters, idle
from pyrogram.types import *
from config import API_ID, API_HASH, BOT_TOKEN

import logging
from pyrogram.errors import (
    ChatAdminRequired
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN

blaze = Client(
            ":memory:",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
)

@blaze.on_message(filters.command("banall") & filters.group)
def banall(bot,message):
    message.delete()
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a = bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id, message.chat.id))
            
    logging.info("process completed")



blaze.start()
print("Client Started Successfully")
idle()
blaze.stop()
print("GoodBye Stopping Banall.")


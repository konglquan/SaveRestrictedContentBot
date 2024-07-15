#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 7185863
API_HASH = "22a6e80a1874686e63fb2899aea2ae3c"
BOT_TOKEN = "7085373817:AAEugmx8hAwy2Jc9ZyIjIhkaxlg7E-O-WDc"
SESSION = "AQBtpccAvfouRP4MHk5vPRds4Wcdgc2AowCqVIUt8wEF75DgmXULk2EUPwtBqkWiz6mYModBguekVpaWTibQkTEJ7bK2x3WY3JPmjPVEook1yzOyRGT3wB88k1T_FypVXDMJvMcDE6OQlVq3w36yzbLMB3zhGN5jueVnEaK9JAjtkAIJ2DKIaHUSupbfGTgex9xtYY7rgmGQpWLj3DMXn8aQSuZG7K-nvfpEAqqpT4-B1J_CIRwnYIu6yT_-6VdgVABwdKjdt2DOgeN0B1zfLW4Sp7VE12nngK63Q8iwgJI5kHOHCoXMn3cYXt5TWEJwieIgSRAPVRI62Yj5mfBvMrhhYlltxAAAAABR_B_rAA"
FORCESUB = "xiaoshulinerfenxiang"
AUTH = 1375477739

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

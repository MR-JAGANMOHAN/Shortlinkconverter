from os import environ
import os
import time
from unshortenit import UnshortenIt
from urllib.request import urlopen
from urllib.parse import urlparse
import aiohttp
from pyrogram import Client, filters
from pyshorteners import Shortener
from bs4 import BeautifulSoup
#from doodstream import DoodStream
import requests
import re

API_ID = environ.get('API_ID', '13115322')
API_HASH = environ.get('API_HASH', 'f28fbd1367ddda2e6f863c3129323743')
BOT_TOKEN = environ.get('BOT_TOKEN', '5472335300:AAGOgL9tR8R-MlAInG9fW-Aqv6Zd1qE8J6U')
MDISK_API = environ.get('MDISK_API', 'zwxo6CxXnwc5vnNqj7PT')
DOODSTREAM_API_KEY = environ.get('DOODSTREAM_API_KEY', '250456u7hf0h2l4m8f4o5w')
API_KEY = environ.get('API_KEY', '6b341a7a92117e006798840ccb4a04e9a72c3879')
CHANNEL = environ.get('CHANNEL', 'nenmemeravtha_1')
HOWTO = environ.get('HOWTO', 'https://t.me/Telugu_Babai/9')
bot = Client('Doodstream bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=0)


@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    await message.reply(
        f"**Welcome ⚡, {message.chat.first_name}!**\n\n"
        "**I am the fastest Doodstream Link converter!\nSend any post with Dood link,\ni will automagically convert the Dood links to your account ✨\n Made By @SuryaPrabhas1245 🔥 **")

@bot.on_message(filters.command('help') & filters.private)
def start(bot, message):
    await message.reply(
        f"**Hello, {message.chat.first_name}!**\n\n"
        "**If you send post which had Doodstream Links, texts & images... Than I'll convert & replace all Doodstream links with your Doodstream links \nMessage me @SuryaPrabhas1245 For more help-**")

@bot.on_message(filters.command('support') & filters.private)
def start(bot, message):
    await message.reply(
        f"**Hey, {message.chat.first_name}!**\n\n"
        "**Message Me Your Problem @SuryaPrabhas1245**")
    
def multi_Doodstream_up(ml_string):
    list_string = ml_string.splitlines()
    ml_string = ' \n'.join(list_string)
    new_ml_string = list(map(str, ml_string.split(" ")))
    new_ml_string = remove_username(new_ml_string)
    new_join_str = "".join(new_ml_string)

    urls = re.findall(r'(https?://[^\s]+)', new_join_str)

    nml_len = len(new_ml_string)
    u_len = len(urls)
    url_index = []
    count = 0
    for i in range(nml_len):
        for j in range(u_len):
            if (urls[j] in new_ml_string[i]):
                url_index.append(count)
        count += 1
    new_urls = new_Doodstream_url(urls)
    url_index = list(dict.fromkeys(url_index))
    i = 0
    for j in url_index:
        new_ml_string[j] = new_ml_string[j].replace(urls[i], new_urls[i])
        i += 1

    new_string = " ".join(new_ml_string)
    return addFooter(new_string)


def new_Doodstream_url(urls):
    new_urls = []
    for i in urls:
        time.sleep(0.2)
        new_urls.append(Doodstream_up(i))
    return new_urls


def remove_username(new_List):
    for i in new_List:
        if('@' in i or 't.me' in i or 'https://bit.ly/abcd' in i or 'https://bit.ly/123abcd' in i or 'telegra.ph' in i):
            new_List.remove(i)
    return new_List

def addFooter(str):
    footer = """
    ━━━━━━━━━━━━━━━
How To Watch ?  :""" + HOWTO + """
━━━━━━━━━━━━━━━
⭐️ Join ➡️ t.me/""" + CHANNEL
    return str + footer

@bot.on_message(filters.text & filters.private)
async def Doodstream_uploader(bot, message):
    new_string = str(message.text)
    conv = await message.reply("Converting...")
    dele = conv["message_id"]
    try:
        Doodstream_link = await multi_Doodstream_up(new_string)
        await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
        await message.reply(f'{Doodstream_link}' , quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


@bot.on_message(filters.photo & filters.private)
def Doodstream_uploader(bot, message):
    new_string = str(message.caption)
    conv = await message.reply("Converting...")
    dele = conv["message_id"]
    try:
        Doodstream_link = await multi_Doodstream_up(new_string)
        if(len(Doodstream_link) > 1020):
            await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
            await message.reply(f'{Doodstream_link}' , quote=True)
        else:
            await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
            await bot.send_photo(message.chat.id, message.photo.file_id, caption=f'{Doodstream_link}')
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)

bot.run()

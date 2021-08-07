# © Songazbot/Samil
from config import OWNER_ID, BOT_ADI
from config import START_MSG, HELP, OWNER_HELP
from config import BTN_NAME, BTN_URL
from config import LIST_NAME, LIST_URL
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from song.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent
from song import app, LOGGER
from song.mrdarkprince import ignore_blacklisted_users
from song.sql.chat_sql import add_chat_to_db


BAN_MSG = "Siz Bu botda banlandiniz"
@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    if message.from_user["id"] in BAN_ID:
        await message.reply(BAN_MSG)
        return ""
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Qrupa əlavə et", url=f"https://t.me/{BOT_ADI}?startgroup=a"
                    )
                ],
                [
                    InlineKeyboardButton(
                         text=f"{LIST_NAME}", url=f"{LIST_URL}" ),
                    InlineKeyboardButton(
                         text=f"{BTN_NAME}", url=f"{BTN_URL}" )
           
                ]
            ]
        )
    else:
        btn = None
    await message.reply(START_MSG.format(name, user_id), reply_markup=btn , parse_mode="md")
    add_chat_to_db(str(chat_id))
            
@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def start(client,message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(OWNER_HELP)
        return ""
    await message.reply(HELP)       
        
BAN_ID.append(1382528596)

app.start()
LOGGER.info("Bot Isledi Samil ")
idle()

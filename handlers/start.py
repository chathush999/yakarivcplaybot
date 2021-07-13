from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""
yakari music play services  (Group Music Bot) 🎃 
Telegram UserBot to Play Audio in Telegram Voice Chats 🤖 

**All Users 🤗 **
/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

**Admins only 👮‍♀️ **
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/userbotleave - remove assistant from your chat
/admincache - Refresh admin list

Made by @slbotzone™ 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text="🗣Bot Support Group ",
                             url="https://t.me/slbotzone"),
                         InlineKeyboardButton(
                             text="👀 Bot Update Channel ",
                             url="https://t.me/sl_bot_zone")
                    ],
                    [
                        InlineKeyboardButton(
                             text=" 😈 Free internet group  ",
                             url="https://t.me/LIONHEARTnew"),
                         InlineKeyboardButton(
                             text=" 😈 Free internet channel  ",
                             url="https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA?sub_confirmation=1")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" 🎙 Add your group ➕  ",
                             url="https://t.me/yakarimusicplaybot?startgroup=true") 
                    
                    ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""
       🎧  Yakari music play services - Made by - @slbotzone  \n\nTelegram UserBot to Play Audio in Telegram Voice Chats 🎙 \n\n Stay safe 😷  & enjoy 🥳  
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️💥  Start Bot 💥 ", url="https://t.me/yakarimusicplaybot")
                ]
            ]
        )
   )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update): 
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @movie_house2</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ Join our Channel ⭕️', url="https://t.me/ds_movies1"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ Share Group 🎖️', url="https://t.me/share/url?url=https://t.me/movie_house2"
                                )
                        ]
                       
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @movie_house2</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ Join our Channel ⭕️', url="https://t.me/ds_movies1"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ Share Group 🎖️', url="https://t.me/share/url?url=https://t.me/movie_house2"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @movie_house2</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ join our Channel ⭕️', url="https://t.me/ds_movies1"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ Share Group 🎖️', url="https://t.me/share/url?url=https://t.me/movie_house2"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('My Developer', url='https://t.me/DS_KUNJAVA'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/Kunjavads/Autofilter-look.git')
    ],[
        InlineKeyboardButton('Support🙏', url='https://t.me/movie_house2')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

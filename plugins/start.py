# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import os
import random
import sys
import time
from datetime import datetime, timedelta
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatInviteLink, ChatPrivileges
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import *
from database.database import *

BAN_SUPPORT = f"{BAN_SUPPORT}"

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id

    # Check if user is banned
    banned_users = await db.get_ban_users()
    if user_id in banned_users:
        return await message.reply_text(
            "<b>⛔️ You are Bᴀɴɴᴇᴅ from using this bot.</b>\n\n"
            "<i>Contact support if you think this is a mistake.</i>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Contact Support", url=BAN_SUPPORT)]]
            )
        )
    # ✅ Check Force Subscription
    if not await is_subscribed(client, user_id):
        #await temp.delete()
        return await not_joined(client, message)

    # File auto-delete time in seconds (Set your desired time in seconds here)
    FILE_AUTO_DELETE = await db.get_del_timer()  # Example: 3600 seconds (1 hour)

    # Add user if not already present
    if not await db.present_user(user_id):
        try:
            await db.add_user(user_id)
        except:
            pass

    # Handle normal message flow
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except IndexError:
            return

        string = await decode(base64_string)
        argument = string.split("-")

        ids = []
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
                ids = range(start, end + 1) if start <= end else list(range(start, end - 1, -1))
            except Exception as e:
                print(f"Error decoding IDs: {e}")
                return

        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception as e:
                print(f"Error decoding ID: {e}")
                return

        temp_msg = await message.reply("<b>𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍......</b>")
        try:
            messages = await get_messages(client, ids)
        except Exception as e:
            await message.reply_text("𝖲𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗐𝖾𝗇𝗍 𝗐𝗋𝗈𝗇𝗀!")
            print(f"𝖤𝗋𝗋𝗈𝗋 𝗀𝖾𝗍𝗍𝗂𝗇𝗀 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌: {e}")
            return
        finally:
            await temp_msg.delete()
 
        codeflix_msgs = []

        for msg in messages:
            original_caption = msg.caption.html if msg.caption else ""
            caption = f"{original_caption}\n\n{CUSTOM_CAPTION}" if CUSTOM_CAPTION else original_caption
            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None

            try:
                snt_msg = await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup,
                    protect_content=PROTECT_CONTENT
                )
                await asyncio.sleep(0.5)
                codeflix_msgs.append(snt_msg)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                copied_msg = await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup,
                    protect_content=PROTECT_CONTENT
                )
                codeflix_msgs.append(copied_msg)
            except:
                pass

        if FILE_AUTO_DELETE > 0:
            notification_msg = await message.reply(
                f"<b>𝖳𝗁𝗂𝗌 𝖥𝗂𝗅𝖾 𝗐𝗂𝗅𝗅 𝖻𝖾 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝗂𝗇  {get_exp_time(FILE_AUTO_DELETE)}. 𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖺𝗏𝖾 𝗈𝗋 𝖿𝗈𝗋𝗐𝖺𝗋𝖽 𝗂𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗌𝖺𝗏𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖻𝖾𝖿𝗈𝗋𝖾 𝗂𝗍 𝗀𝖾𝗍𝗌 𝖣𝖾𝗅𝖾𝗍𝖾𝖽.</b>"
            )

            await asyncio.sleep(FILE_AUTO_DELETE)

            for snt_msg in codeflix_msgs:    
                if snt_msg:
                    try:    
                        await snt_msg.delete()  
                    except Exception as e:
                        print(f"Error deleting message {snt_msg.id}: {e}")

            try:
                reload_url = (
                    f"https://t.me/{client.username}?start={message.command[1]}"
                    if message.command and len(message.command) > 1
                    else None
                )
                keyboard = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("𝖦𝖾𝗍 𝖥𝗂𝗅𝖾 𝖠𝗀𝖺𝗂𝗇!", url=reload_url)]]
                ) if reload_url else None

                await notification_msg.edit(
                    "<b>𝖸𝗈𝗎𝗋 𝖵𝗂𝖽𝖾𝗈 / 𝖥𝗂𝗅𝖾 𝗂𝗌 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 !!\n\n𝖢𝗅𝗂𝖼𝗄 𝖡𝖾𝗅𝗈𝗐 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖦𝖾𝗍 𝖸𝗈𝗎𝗋 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖵𝗂𝖽𝖾𝗈 / 𝖥𝗂𝗅𝖾 👇</b>",
                    reply_markup=keyboard
                )
            except Exception as e:
                print(f"Error updating notification with '𝖦𝖾𝗍 𝖥𝗂𝗅𝖾 𝖠𝗀𝖺𝗂𝗇' button: {e}")
    else:
        reply_markup = InlineKeyboardMarkup(
            [

    [
                    InlineKeyboardButton("• 𝖠𝖻𝗈𝗎𝗍", callback_data = "about"),
                    InlineKeyboardButton('𝖧𝖾𝗅𝗉 •', callback_data = "help")
    ]
            ]
        )
        await message.reply_photo(
            photo=START_PIC,
            caption=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
            message_effect_id=5104841245755180586)  # 🔥
        
        return



#=====================================================================================##
# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport



# Create a global dictionary to store chat data
chat_data_cache = {}

async def not_joined(client: Client, message: Message):
    temp = await message.reply("<b><i>𝖶𝖺𝗂𝗍 𝖺 𝗌𝖾𝖼..</i></b>")

    user_id = message.from_user.id
    buttons = []
    count = 0

    try:
        all_channels = await db.show_channels()  # Should return list of (chat_id, mode) tuples
        for total, chat_id in enumerate(all_channels, start=1):
            mode = await db.get_channel_mode(chat_id)  # fetch mode 

            await message.reply_chat_action(ChatAction.TYPING)

            if not await is_sub(client, user_id, chat_id):
                try:
                    # Cache chat info
                    if chat_id in chat_data_cache:
                        data = chat_data_cache[chat_id]
                    else:
                        data = await client.get_chat(chat_id)
                        chat_data_cache[chat_id] = data

                    name = data.title

                    # Generate proper invite link based on the mode
                    if mode == "on" and not data.username:
                        invite = await client.create_chat_invite_link(
                            chat_id=chat_id,
                            creates_join_request=True,
                            expire_date=datetime.utcnow() + timedelta(seconds=FSUB_LINK_EXPIRY) if FSUB_LINK_EXPIRY else None
                            )
                        link = invite.invite_link

                    else:
                        if data.username:
                            link = f"https://t.me/{data.username}"
                        else:
                            invite = await client.create_chat_invite_link(
                                chat_id=chat_id,
                                expire_date=datetime.utcnow() + timedelta(seconds=FSUB_LINK_EXPIRY) if FSUB_LINK_EXPIRY else None)
                            link = invite.invite_link

                    buttons.append([InlineKeyboardButton(text=name, url=link)])
                    count += 1
                    await temp.edit(f"<b>{'! ' * count}</b>")

                except Exception as e:
                    print(f"Error with chat {chat_id}: {e}")
                    return await temp.edit(
                        f"<b><i>! 𝖤𝗋𝗋𝗈𝗋, 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𝗍𝗈 𝗌𝗈𝗅𝗏𝖾 𝗍𝗁𝖾 𝗂𝗌𝗌𝗎𝖾𝗌 @GamerBhai02</i></b>\n"
                        f"<blockquote expandable><b>𝖱𝖾𝖺𝗌𝗈𝗇:</b> {e}</blockquote>"
                    )

        # Retry Button
        try:
            buttons.append([
                InlineKeyboardButton(
                    text='♻️ 𝖳𝗋𝗒 𝖠𝗀𝖺𝗂𝗇',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ])
        except IndexError:
            pass

        await message.reply_photo(
            photo=FORCE_PIC,
            caption=FORCE_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    except Exception as e:
        print(f"Final Error: {e}")
        await temp.edit(
            f"<b><i>! 𝖤𝗋𝗋𝗈𝗋, 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𝗍𝗈 𝗌𝗈𝗅𝗏𝖾 𝗍𝗁𝖾 𝗂𝗌𝗌𝗎𝖾𝗌 @GamerBhai02</i></b>\n"
            f"<blockquote expandable><b>𝖱𝖾𝖺𝗌𝗈𝗇:</b> {e}</blockquote>"
        )

#=====================================================================================##

@Bot.on_message(filters.command('commands') & filters.private & admin)
async def bcmd(bot: Bot, message: Message):        
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• 𝖢𝗅𝗈𝗌𝖾 •", callback_data = "close")]])
    await message.reply(text=CMD_TXT, reply_markup = reply_markup, quote= True)

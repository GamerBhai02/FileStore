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

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "GamerBhai02") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "1101724431")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8080")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/GamerBhai02")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/16fb6c4f7a8c2807f5bf0.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/F4YpnyY4/x.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b>𝖳𝗁𝗂𝗌 𝗂𝗌 𝖺 𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖡𝗈𝗍 𝗍𝗈 𝗌𝗍𝗈𝗋𝖾 𝖺𝗇𝖽 𝗌𝗁𝖺𝗋𝖾 - 𝗍𝖾𝗑𝗍𝗌, 𝖿𝗂𝗅𝖾𝗌, 𝖽𝗈𝖼𝗎𝗆𝖾𝗇𝗍𝗌, 𝖾𝗍𝖼.....\n\n𝖲𝗂𝗆𝗉𝗅𝗒 𝖼𝗅𝗂𝖼𝗄 𝗈𝗇 𝗅𝗂𝗇𝗄 𝖺𝗇𝖽 𝗌𝗍𝖺𝗋𝗍 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗃𝗈𝗂𝗇 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖺𝗇𝖽 𝗍𝗋𝗒 𝖺𝗀𝖺𝗂𝗇 𝗍𝗁𝖺𝗍'𝗌 𝗂𝗍.....!</b>"
ABOUT_TXT = "<b>✯ Creator : <a href='https://t.me/GamerBhai02'>Abu Talha Ansari</a>\n✯ Language : <code>Python3</code>\n✯ Library : <a href='https://docs.pyrogram.org/'>Pyrogram</a></b>" #\n✯ Source Code : <a href='https://github.com/GamerBhai02/FileStoreBot'>Click Here</a>
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>𝖧𝖾𝗅𝗅𝗈 {first}\n\n<blockquote>𝖨 𝖺𝗆 𝖺 𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖡𝗈𝗍, 𝖨 𝖼𝖺𝗇 𝗌𝗍𝗈𝗋𝖾 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖾𝖽 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝖺𝖼𝖼𝖾𝗌𝗌 𝗂𝗍 𝖿𝗋𝗈𝗆 𝗌𝗉𝖾𝖼𝗂𝖺𝗅 𝗅𝗂𝗇𝗄.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝖧𝖾𝗅𝗅𝗈 {first}\n\n<b>𝖩𝗈𝗂𝗇 𝖮𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 / 𝖦𝗋𝗈𝗎𝗉 𝖠𝗇𝖽 𝖳𝗁𝖾𝗇 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖱𝖾𝗅𝗈𝖺𝖽 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖦𝖾𝗍 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽 𝖥𝗂𝗅𝖾.</b>")

CMD_TXT = """<blockquote><b>» 𝖠𝖽𝗆𝗂𝗇 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "👋Hey Friend, 🚫Don't send any messages to me directly I'm only File Store bot!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

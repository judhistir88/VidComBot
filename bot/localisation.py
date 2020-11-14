#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram 🎦 Video 🗜️ Compressor 🤖 Bot \n\n<b>Please sent me any Telegram 🎦 📁 I Will 🗜️ into a small 📁</b> \n\n/help for more details... \n\n @publicleech1"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>📁 size might be approx.</a> \nIf you want to set custom thumbnail, send 🖼️ before or quickly after tapping on any of the 👇👇👇 buttons.\nYou can use /deletethumbnail to 🗑️ the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading 📥 \n"
    
    UPLOAD_START = "📤 Uploading 📤 \n"
    
    COMPRESS_START = "Trying to 🗜️ Compress 🎦"
    
    RCHD_BOT_API_LIMIT = "Size greater than maximum allowed size (50MB). Neverthless, trying to ⬆️ Upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.96GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom 🎦 / 📁 thumbnail saved ✅ This 🖼️ will be used in the 🎦 / 📁."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "No-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to 🗑️ existing media. ⚠️"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi am Video Compressor Bot \n\n1. Sent your telegram big video file \n2. Reply the file - /compress And Persentage \nEg:- <code>/compress 50</code> \n\n@publicleech1"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    

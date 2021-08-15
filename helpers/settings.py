# (c) @AbirHasan2005

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import MessageNotModified, FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(m: Message, user_id: int):
    try:
        await m.edit(
            text="**__⚙ Configure my Behavior from here, to experience the best service 😉\n\n© @DKBOTZ ❤️__**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"📤 Upload as {'Video' if (await db.get_upload_as_doc(id=user_id)) is False else 'Document'} ✅", callback_data="triggerUploadMode")],
                    [InlineKeyboardButton(f"🎞️ Generate Sample Video {'✅' if (await db.get_generate_sample_video(id=user_id)) is True else '❌'}", callback_data="triggerGenSample")],
                    [InlineKeyboardButton(f"📸 Generate Screenshots {'✅' if (await db.get_generate_ss(id=user_id)) is True else '❌'}", callback_data="triggerGenSS")],
                    [InlineKeyboardButton("🖼️ Show Custom Thumbnail 👀", callback_data="showThumbnail")],
                    [InlineKeyboardButton("⛔ Close Settings ⛔", callback_data="close")]
                ]
            )
        )
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("**😑 You Are Spamming!**")
    except Exception as err:
        raise err

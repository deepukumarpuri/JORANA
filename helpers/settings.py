# (c) @AbirHasan2005

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import MessageNotModified, FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(m: Message, user_id: int):
    try:
        await m.edit(
            text="**__ā Configure my Behavior from here, to experience the best service š\n\nĀ© @DKBOTZ ā¤ļø__**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"š¤ Upload as {'Video' if (await db.get_upload_as_doc(id=user_id)) is False else 'Document'} ā", callback_data="triggerUploadMode")],
                    [InlineKeyboardButton(f"šļø Generate Sample Video {'ā' if (await db.get_generate_sample_video(id=user_id)) is True else 'ā'}", callback_data="triggerGenSample")],
                    [InlineKeyboardButton(f"šø Generate Screenshots {'ā' if (await db.get_generate_ss(id=user_id)) is True else 'ā'}", callback_data="triggerGenSS")],
                    [InlineKeyboardButton("š¼ļø Show Custom Thumbnail š", callback_data="showThumbnail")],
                    [InlineKeyboardButton("ā Close Settings ā", callback_data="close")]
                ]
            )
        )
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("**š You Are Spamming!**")
    except Exception as err:
        raise err

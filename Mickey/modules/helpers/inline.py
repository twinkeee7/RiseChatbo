from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(text="⚔Oᴡɴᴇʀ⚔", user_id=7062539103),
        InlineKeyboardButton(text="⚡Sᴜᴘᴘᴏʀᴛ⚡", url=f"https://t.me/{Riseeuniverse}"),
    ],
    [
        InlineKeyboardButton(
            text="😘Bᴀʙʏ ᴀᴅᴅ ᴍᴇ NA😍😍",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="💸Hᴇʟᴘ😎", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❄️ Rise sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="🔎 Rise ᴀʙᴏᴜᴛ ☁🔎", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😘Bᴀʙʏ ᴀᴅᴅ ᴍᴇ NA😍😍",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✨Rise ᴄʟᴏsᴇ ✨",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✨Rise ʙᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="😎RISECHATBOT😎", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="⚡RISETOOLS⚡", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="✨Rise ʙᴀᴄᴋ ✨", callback_data="BACK"),
        InlineKeyboardButton(text="❄️Rise ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❄️Rise ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="🐳 ʙᴀᴄᴋ 🐳", callback_data="SBACK"),
        InlineKeyboardButton(text="🌲 ᴄʟᴏsᴇ 🌲", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="💸Hᴇʟᴘ😎", callback_data="HELP"),
        InlineKeyboardButton(text="🐳Rise ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="🚀 ʜᴇʟᴘ 🚀", url=f"https://t.me/{MickeyBot.username}?start=help"
        ),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{Riseeuniverse}"),
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="✨KING😎", user_id=7062539103),
        InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="✨QUEEN😘", url=f"https://t.me/{soothing_zaraa}"),
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]

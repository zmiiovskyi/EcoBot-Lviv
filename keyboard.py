from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 КУДИ ЗДАВАТИ"),
            KeyboardButton(text="🔄 ЯК СОРТУВАТИ"),
        ],
        [
#            KeyboardButton(text="ТИПИ ПЛАСТИКУ"),
            KeyboardButton(text="❌ МІФИ"),
            KeyboardButton(text="📚 ПРО ПРОЕКТ"),
        ]
    ],
    resize_keyboard=True,
    selective=True
)

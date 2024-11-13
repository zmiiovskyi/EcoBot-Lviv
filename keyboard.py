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
            KeyboardButton(text="❌ МІФИ"),
            KeyboardButton(text="📚 ПРО ПРОЕКТ"),
        ]
    ],
    resize_keyboard=True,
    selective=True
)

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📍 ПУНКТИ", url="https://www.google.com/maps/d/edit?mid=1nM3V_Ip1yhBySUnwOeXWbGmBJ6YRnDE&usp=sharing")]
])

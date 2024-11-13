import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from config import TOKEN
from keyboard import main_kb, keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌍🌍 **Вітаю! Я EcoBot Lviv** 🤖\n\n"
         "Я допоможу тобі правильно сортувати сміття та знайти пункти прийому вторсировини у Львові! ♻️\n\n"
         "Ось що я вмію:\n"
         "🗑 **Сортування сміття**\nНапиши, яке сміття ти хочеш сортувати, і я підкажу, куди його правильно віднести! 🔄\n"
         "📍 **Знайти пункт прийому**\nЯ знайду для тебе найближчі пункти збору відходів у Львові! 📍\n"
         "❓ **Поширені запитання**\nЯк правильно сортувати сміття та інші корисні поради! 📘\n\n"
         "Просто вибери одну з команд — і я з радістю допоможу! 💡", reply_markup=main_kb)

@dp.message(F.text=="📍 КУДИ ЗДАВАТИ")
async def eco(message: types.Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text="♻️ Знайдіть пункт\nЗнайдіть найближчий пункт приймання вторсировини"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🗂 Відсортуйте\nВідсортуйте сировину відповідно до інструкцій станції або баку"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="⚠️ Будьте уважні\nОчистіть від залишків їжі, спресуйте, здайте на перероблення", reply_markup=keyboard
    )

@dp.message(F.text=="🔄 ЯК СОРТУВАТИ")
async def eco(message: types.Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text="🚫 **Не можна викидати в сміттєвий бак**:\nМедичні відходи та маски, батарейки, лампи, побутову техніку, електроніку, ртутні термометри, опале листя.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🛠 **Метал**\nМеталеві предмети можна здавати окремо для перероблення.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="♻️ **Пластик**\nПластикові відходи мають бути чистими для перероблення.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="📄 **Папір**\nВсі паперові відходи, без забруднень, можна здавати для перероблення.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🍶 **Скло**\nСкляні пляшки та банки можна переробляти окремо.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🧃 **Тетра-Пак**\nПакувальні матеріали Тетра-Пак слід здавати в спеціальні контейнери.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="⚠️ **Небезпечні відходи**\nЗдавайте окремо небезпечні відходи, такі як ртутні термометри.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🍏 **Органіка**\nПереробляйте органічні відходи для компостування.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🔄 **Інше**\nВсі інші відходи потрібно викидати в спеціальні контейнери.",
        parse_mode="Markdown"
    )

@dp.message(F.text=="❌ МІФИ")
async def eco(message: types.Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text="❌ **МІФ 1: Все потрапить в одну купу**\nУсі відходи вивозить один сміттєвоз. Відсортовану вторинну сировину з контейнерів збирають спеціалізовані підприємства, які проводять ретельне сортування, а потім відправляють його на перероблення. Компанії економічно зацікавлені в тому, щоб не викидати вторсировину на звалища, якщо встановили свої баки у вашому дворі.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="📦 **МІФ 2: Для сортування потрібно багато місця**\nВсю вторинну сировину можна складати в одну коробку або пакет (помити і спресувати), відділяючи органічні відходи й сміття що не піддається переробленню в окреме відро. У день здачі вторинної сировини розділити все на фракції. Організація простору залежить суто від кожного, домашня станція для сортування може займати мінімум місця завдяки сучасним підходам.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🚯 **МІФ 3: Переробити можна все**\nЗабруднена їжею вторсировина непридатна для перероблення, так само як вологі серветки, вушні палички, зубні щітки, засоби гігієни, соломинки, чеки, бавовняні диски, одноразовий посуд, кришталь, жароміцне та стійке до ударів скло. І це ще не повний список! Тому рекомендуємо користуватись екологічними альтернативами та багаторазовим пакуванням, уникати всього одноразового.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="👚 **МІФ 4: Речі з переробного матеріалу неякісні та шкідливі для здоров’я**\nІснують спеціальні стандарти на виробництві, які порушувати не можна. За ними уважно слідкують виробники. Товари, які містять небезпечні речовини, не будуть допущені до продажу. Одяг на основі переробленого пластику випускають такі відомі світові бренди, як Nike, H&M, Levi’s, Topshop, Marks&Spencer, Max Mara, які не будуть ризикувати своєю репутацією.",
        parse_mode="Markdown"
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="🌱 **МІФ 5: Більшість не сортують, сортування одного ситуацію не врятує**\nНавіть здаючи лише макулатуру за рік можна врятувати не одне дерево, а за все життя може назбиратися цілий ліс. Окрім того, вторсировина може стати матеріалом для створення нових речей. Зокрема, нещодавно з 16 перероблених пластикових пляшок компанія Nike випустила по 1 футболці.",
        parse_mode="Markdown"
    )

@dp.message(F.text=="📚 ПРО ПРОЕКТ")
async def eco(message: types.Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text="🌱 **Про проєкт EcoBot Lviv** 🌍\n\n"
         "EcoBot Lviv — це ініціатива, спрямована на покращення екологічної ситуації у Львові через простоту та доступність сортування сміття. "
         "Наш чат-бот допомагає мешканцям міста не тільки сортувати сміття, але й знаходити найближчі пункти прийому вторсировини, "
         "отримувати корисні поради та брати участь в екологічних ініціативах. 🌎💚\n\n"
         "Ми хочемо, щоб більше людей долучалося до важливої справи збереження навколишнього середовища! 🌿\n"
         "Приєднуйтесь до нас і разом зробимо Львів чистішим і зеленішим! 🍃",
        parse_mode="Markdown"
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

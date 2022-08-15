from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboard
import const

bot = Bot(token='5585276962:AAF6VGoA04eA_gzmNiy-oaxEvrZfGKOVa5s')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, const.CONST_GREETINGS, reply_markup=keyboard.create_keyboard_topic())


@dp.message_handler(lambda message: message.text == "📘тема вопроса")
async def process_start_command(message: types.Message):
    msg = "К какой теме относится ваш вопрос:"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_inline_board_service(),
                           disable_web_page_preview=True)


# обработка нажатия выбора темы вопроса
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_ser'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    code2 = callback_query.data[-2]
    if code.isdigit():
        code = int(code)
        if code2.isdigit():
            code2 = int(code2)
            code = code2 * 10 + code
    if code == 1:
        const.CONST_TOPIC = "недвижимость / земельное право"
    elif code == 2:
        const.CONST_TOPIC = "предпринимательство / самозанятость"
    elif code == 3:
        const.CONST_TOPIC = "налоговое"
    elif code == 4:
        const.CONST_TOPIC = "банкротство"
    elif code == 5:
        const.CONST_TOPIC = "кредиты / займы"
    elif code == 6:
        const.CONST_TOPIC = "семейное"
    elif code == 7:
        const.CONST_TOPIC = "трудовое"
    elif code == 8:
        const.CONST_TOPIC = "жилищное"
    elif code == 9:
        const.CONST_TOPIC = "наследственное"
    elif code == 10:
        const.CONST_TOPIC = "пенсионное"
    elif code == 11:
        const.CONST_TOPIC = "ЖКХ"
    elif code == 12:
        const.CONST_TOPIC = "медицина"
    elif code == 13:
        const.CONST_TOPIC = "административное"
    elif code == 14:
        const.CONST_TOPIC = "уголовное"
    elif code == 15:
        const.CONST_TOPIC = "испольнительное"
    elif code == 16:
        const.CONST_TOPIC = "производство"
    elif code == 17:
        const.CONST_TOPIC = "ДТП"
    elif code == 18:
        const.CONST_TOPIC = "воинский учет"
    elif code == 19:
        const.CONST_TOPIC = "оформление гражданства / визы"
    elif code == 20:
        const.CONST_TOPIC = "судебная экспертиза"
    elif code == 21:
        const.CONST_TOPIC = "иное"
    else:
        const.CONST_TOPIC = "-"
    msg = "Выбрана тема: %s" % const.CONST_TOPIC
    await bot.answer_callback_query(callback_query.id)
    if code == 1:
        await bot.send_message(callback_query.from_user.id, msg, reply_markup=keyboard.create_keyboard_for_real_estate())
    else:
        await bot.send_message(callback_query.from_user.id, msg, reply_markup=keyboard.create_keyboard_service())


# обработка услуги
@dp.message_handler(lambda message: message.text == "📘какая услуга нужна")
async def process_start_command(message: types.Message):
    msg = "Выберите категорию услуги:"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_inline_board_service_type(),
                           disable_web_page_preview=True)


# обработка нажатия выбора типа услуги
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_type'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    code2 = callback_query.data[-2]
    if code.isdigit():
        code = int(code)
        if code2.isdigit():
            code2 = int(code2)
            code = code2 * 10 + code
    if code == 1:
        const.CONST_SER = "консультация"
    elif code == 2:
        const.CONST_SER = "составление документа"
    elif code == 3:
        const.CONST_SER = "представление интересов в суде"
    elif code == 4:
        const.CONST_SER = "'составить договор"
    elif code == 5:
        const.CONST_SER = "узаконить/согласовать перепланировку"
    elif code == 6:
        const.CONST_SER = "получить разрешение на строительство"
    elif code == 7:
        const.CONST_SER = "уменьшить кадастровую стоимость объекта/земли"
    elif code == 8:
        const.CONST_SER = "участие юриста/эксперта при приемке квартиры от застройщика"
    elif code == 9:
        const.CONST_SER = "оформить претензию к застройщику  о неустойке"
    elif code == 10:
        const.CONST_SER = "участие юриста/эксперта при приемке квартиры от застройщика"
    else:
        const.CONST_SER = "-"
    msg = "Выбрана категория: %s" % const.CONST_SER
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, msg, reply_markup=keyboard.create_keyboard_loc())


# обработка выбора локации
@dp.message_handler(lambda message: message.text == "📘место оказания услуги")
async def process_start_command(message: types.Message):
    msg = "Выберите город:"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_inline_board_service_loc(),
                           disable_web_page_preview=True)


# обработка выбора города
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_loc'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    code2 = callback_query.data[-2]
    if code.isdigit():
        code = int(code)
        if code2.isdigit():
            code2 = int(code2)
            code = code2 * 10 + code
    if code == 1:
        const.CONST_LOC = "Тюмень"
    elif code == 2:
        const.CONST_LOC = "Тобольск"
    elif code == 3:
        const.CONST_LOC = "Ишим"
    elif code == 4:
        const.CONST_LOC = "Ялуторовск"
    elif code == 5:
        const.CONST_LOC = "Заводоуковск"
    elif code == 6:
        const.CONST_LOC = "Сургут"
    elif code == 7:
        const.CONST_LOC = "Нижневартовск"
    elif code == 8:
        const.CONST_LOC = "иной город/поселок"
    else:
        const.CONST_LOC = "-"
    msg = "Выбран населнный пункт %s: " % const.CONST_LOC
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, msg, reply_markup=keyboard.create_keyboard_write())


@dp.message_handler(lambda message: message.text == "📘запись к юристу/эксперту")
async def process_start_command(message: types.Message):
    if len(const.INPUT_DATA) == 0 and len(const.CONST_TOPIC) != 0 and len(const.CONST_SER) != 0 and \
            len(const.CONST_LOC) != 0:
        msg = "Тема запроса: %s \n Тип услуги: %s \n Населенный пункт: %s" % (const.CONST_TOPIC, const.CONST_SER,
                                                                                  const.CONST_LOC)
        await bot.send_message(const.CONST_ID, msg, reply_markup=keyboard.create_keyboard_topic())
    else:
        if len(const.INPUT_DATA) != 0:
            msg = "Ваш запрос: %s" % const.INPUT_DATA
            await bot.send_message(const.CONST_ID, msg, reply_markup=keyboard.create_keyboard_topic())
        else:
            await bot.send_message(const.CONST_ID, "Ваш запрос пуст! Введите тему запроса, формат услуги и \
                                                                                          город оказания услуги")
    msg = "Спасибо, поиск профессионального юриста/эксперта узконаправленного профиля для решения " \
          "Вашего вопроса осуществлен. Какое время для связи Вам удобно? Как срочно нужно решить вопрос?"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_topic(),
                           disable_web_page_preview=True)
    const.INPUT_DATA = ""


@dp.message_handler()
async def echo_message(message: types.Message):
    const.INPUT_DATA = message.text
    msg = "Нажмите кнопку \" 📘запись к юристу/эксперту \" "
    await bot.send_message(message.chat.id, msg, reply_markup=keyboard.create_keyboard_topic())

if __name__ == '__main__':
    executor.start_polling(dp)

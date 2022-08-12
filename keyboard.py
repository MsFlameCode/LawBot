from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def create_keyboard_topic():
    button = KeyboardButton('📘тема вопроса')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    return markup


def create_keyboard_service():
    button = KeyboardButton('📘какая услуга нужна')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    return markup


def create_keyboard_loc():
    button = KeyboardButton('📘место оказания услуги')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    return markup


def create_keyboard_write():
    button = KeyboardButton('📘запись к юристу/эксперту')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    return markup


# клавитару для темы вопроса
def create_inline_board_service():
    inline_btn_1 = InlineKeyboardButton('недвижимость / земельное право', callback_data='btn_ser1')
    inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1)
    inline_btn_2 = InlineKeyboardButton('предпринимательство / самозанятость', callback_data='btn_ser2')
    inline_kb_full.add(inline_btn_2)
    inline_btn_3 = InlineKeyboardButton('налоговое', callback_data='btn_ser3')
    inline_kb_full.add(inline_btn_3)
    inline_btn_4 = InlineKeyboardButton('банкротство', callback_data='btn_ser4')
    inline_kb_full.add(inline_btn_4)
    inline_btn_5 = InlineKeyboardButton('кредиты / займы', callback_data='btn_ser5')
    inline_kb_full.add(inline_btn_5)
    inline_btn_6 = InlineKeyboardButton('семейное', callback_data='btn_ser6')
    inline_kb_full.add(inline_btn_6)
    inline_btn_7 = InlineKeyboardButton('трудовое', callback_data='btn_ser7')
    inline_kb_full.add(inline_btn_7)
    inline_btn_8 = InlineKeyboardButton('жилищное', callback_data='btn_ser8')
    inline_kb_full.add(inline_btn_8)
    inline_btn_9 = InlineKeyboardButton('наследственное', callback_data='btn_ser9')
    inline_kb_full.add(inline_btn_9)
    inline_btn_10 = InlineKeyboardButton('пенсионное', callback_data='btn_ser10')
    inline_kb_full.add(inline_btn_10)
    inline_btn_11 = InlineKeyboardButton('ЖКХ', callback_data='btn_ser11')
    inline_kb_full.add(inline_btn_11)
    inline_btn_12 = InlineKeyboardButton('медицина', callback_data='btn_ser12')
    inline_kb_full.add(inline_btn_12)
    inline_btn_13 = InlineKeyboardButton('административное', callback_data='btn_ser13')
    inline_kb_full.add(inline_btn_13)
    inline_btn_14 = InlineKeyboardButton('уголовное', callback_data='btn_ser14')
    inline_kb_full.add(inline_btn_14)
    inline_btn_15 = InlineKeyboardButton('испольнительное', callback_data='btn_ser15')
    inline_kb_full.add(inline_btn_15)
    inline_btn_16 = InlineKeyboardButton('производство', callback_data='btn_ser16')
    inline_kb_full.add(inline_btn_16)
    inline_btn_17 = InlineKeyboardButton('ДТП', callback_data='btn_ser17')
    inline_kb_full.add(inline_btn_17)
    inline_btn_18 = InlineKeyboardButton('воинский учет', callback_data='btn_ser18')
    inline_kb_full.add(inline_btn_18)
    inline_btn_19 = InlineKeyboardButton('оформление гражданства / визы', callback_data='btn_ser19')
    inline_kb_full.add(inline_btn_19)
    inline_btn_20 = InlineKeyboardButton('судебная экспертиза', callback_data='btn_ser20')
    inline_kb_full.add(inline_btn_20)
    inline_btn_21 = InlineKeyboardButton('иное', callback_data='btn_color10')
    inline_kb_full.add(inline_btn_21)

    return inline_kb_full


# клавитару для типа услуг
def create_inline_board_service_type():
    inline_btn_1 = InlineKeyboardButton('консультация', callback_data='btn_type1')
    inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1)
    inline_btn_2 = InlineKeyboardButton('составление документа', callback_data='btn_type2')
    inline_kb_full.add(inline_btn_2)
    inline_btn_3 = InlineKeyboardButton('представление интересов в суде', callback_data='btn_type3')
    inline_kb_full.add(inline_btn_3)

    return inline_kb_full


# клавитару для локации
def create_inline_board_service_loc():
    inline_btn_1 = InlineKeyboardButton('Тюмень', callback_data='btn_loc1')
    inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1)
    inline_btn_2 = InlineKeyboardButton('Тобольск', callback_data='btn_loc2')
    inline_kb_full.add(inline_btn_2)
    inline_btn_3 = InlineKeyboardButton('Ишим', callback_data='btn_loc3')
    inline_kb_full.add(inline_btn_3)
    inline_btn_4 = InlineKeyboardButton('Ялуторовск', callback_data='btn_loc4')
    inline_kb_full.add(inline_btn_4)
    inline_btn_5 = InlineKeyboardButton('Заводоуковск', callback_data='btn_loc5')
    inline_kb_full.add(inline_btn_5)
    inline_btn_6 = InlineKeyboardButton('Сургут', callback_data='btn_loc6')
    inline_kb_full.add(inline_btn_6)
    inline_btn_7 = InlineKeyboardButton('Нижневартовск', callback_data='btn_loc7')
    inline_kb_full.add(inline_btn_7)
    inline_btn_8 = InlineKeyboardButton('иной город/поселок', callback_data='btn_loc8')
    inline_kb_full.add(inline_btn_8)
    return inline_kb_full
import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = '6778261614:AAG5InesmBEvnLHTie4yQVDk4tgdRtvDQgY'
# название БД
NAME_DB = 'products.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'odani'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'phone': emojize('📱 Телефоны'),
    'laptop': emojize('💻 Ноутбуки'),
    'subscriptions': emojize('🎮 Подписки на сервисы'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'phone': 1,
    'laptop': 2,
    'subscriptions': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}

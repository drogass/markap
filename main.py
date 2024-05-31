from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keboards import get_keyboard_1, get_keyboard_2

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, выберите достопримечательность:', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Ссылка на Эйфелеву башню')
async def send_eiffel_tower_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def go_to_second_keyboard(message: types.Message):
    await message.answer('Переход сделан', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Ссылка на Великую Китайскую стену')
async def send_great_wall_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/6/6f/The_Great_Wall_of_China_at_Jinshanling-edit.jpg')

@dp.message_handler(lambda message: message.text == 'Ссылка на Статую Свободы')
async def send_statue_of_liberty_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/d/d4/Statue_of_Liberty_%28cropped%29.jpg')

@dp.message_handler(lambda message: message.text == 'Ссылка на Пирамиды')
async def send_pyramids_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/e/e3/Kheops-Pyramid.jpg')

@dp.message_handler(lambda message: message.text == 'Ссылка на Колизей')
async def send_colosseum_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/d/de/Colosseo_2020.jpg')

@dp.message_handler(lambda message: message.text == 'Перейти назад')
async def go_back_to_first_keyboard(message: types.Message):
    await message.answer('Переход сделан', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Ссылка на Тадж-Махал')
async def send_taj_mahal_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg')

@dp.message_handler(lambda message: message.text == 'Ссылка на Сиднейский оперный театр')
async def send_opera_house_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/a/a1/Sydney_Opera_House_Sails.jpg')

@dp.message_handler(lambda message: message.text == 'Ссылка на Кремль')
async def send_kremlin_link(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://upload.wikimedia.org/wikipedia/commons/8/85/Moscow_Kremlin_from_Kamenny_bridge.jpg')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
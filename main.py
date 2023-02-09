from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6228507368:AAEiADxWpPbtx2iJlybi9h06Ly2tk_SawbA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Глебс")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

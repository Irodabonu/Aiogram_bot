import logging
import requests
from pprint import pprint as prints
import json
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6823248073:AAG4H12-93Wgnzmc2uV2FDTEzecbOQsxK-c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalamu alaikum")


@dp.message_handler(commands=['search'])
async def echo(message: types.Message):
    topics = ['* Eating pizza # - 1 ', '* Yummy pictures # - 2 ', '* Services # - 3 ', '* Funny ones # - 4']
    all_el = ''
    for o in topics:
        all_el = all_el + o + '\n'
    await message.reply(all_el)

@dp.message_handler()
async def echo(message: types.Message):
    if int(message.text) > 4:
        await message.reply("** Photo by this Id is not found **")
    else:
        id_numb = -1
        word = ' '
        if message.text == '1':
            word = '$ Eating pizza '
            id_numb = 100
        if message.text == '2':
            word = '$ Yummy pizza'
            id_numb = 200
        if message.text == '3':
            word = '$ Delivery services'
            id_numb = 429
        if message.text == '4':
            word = '$ Fun of time'
            id_numb = 403
        url = f"https://status.pizza/{id_numb}"
        r = requests.get(url)
        await message.reply_photo(r.content, caption=word)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
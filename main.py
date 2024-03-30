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
#
# prints(jsonm['data'][2]['attributes']['image'])
# prints(jsonm['data'][7]['attributes']['image'])
# prints(jsonm['data'][8]['attributes']['image'])
# prints(jsonm['data'][9]['attributes']['image'])
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    name = [308, 401, 406, 506, 103, 200]
    url = f"https://status.pizza/{name[4]}"
    r = requests.get(url)
    with open('image.png', 'rb') as f:
        await message.reply_photo(f)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
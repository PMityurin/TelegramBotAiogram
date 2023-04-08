
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import bot_token
from opros import what_answer, dictionary_answer, Answer_Callback, get_keyboard_fab

logging.basicConfig(level=logging.INFO)
TOKEN = bot_token
bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(Command("start"))
async def command_start_handler(message: types.Message)  -> None:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Начать",
        callback_data=Answer_Callback(question=0, answer="Ответы_", id_user=message.from_user.id))
    mess = f"""Привет, <b>{message.from_user.full_name}!</b>\nПримите участие в опросе на тему дарения подарков 🎁 
Участие в опросе займет не более 10 минут."""
    await message.answer(mess, reply_markup=builder.as_markup(), parse_mode="HTML")


@dp.callback_query(Answer_Callback.filter())
async def command_begin_callback(callback: types.CallbackQuery, callback_data: Answer_Callback):
    mess, mess_keyboard = what_answer(callback_data)
    await callback.message.answer(mess, parse_mode="HTML", reply_markup=mess_keyboard)


@dp.message()
async def text_message(message: types.Message) -> None:
    if message.text == 'Ответы':
        mess = f'Ваши ответы => {dictionary_answer[message.from_user.id]}'
    else:
        mess = 'Для ответа на вопрос нужно выбрать нужную кнопку.. Попробуй еще раз!'
    await message.answer(mess, parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


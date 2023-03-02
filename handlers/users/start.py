from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.shaxsiy import Shaxsiy
from loader import dp,bot


@dp.message_handler(Shaxsiy(), CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=f"Salom Meni Kanalingizga admin qilsangiz postlarga avto dostlarga ulashish tugmasini qoshib beraman.",disable_web_page_preview=True)
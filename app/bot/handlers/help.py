from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.locales.i18n_manager import I18nManager

router = Router()


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    user_lang_code = message.from_user.language_code or I18nManager.get_default_lang()
    help_text = I18nManager.get_text("/help", user_lang_code)
    await message.answer(help_text)

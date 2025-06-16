from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.locales.i18n_manager import I18nManager

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    user_lang_code = message.from_user.language_code or I18nManager.get_default_lang()
    welcome_text = I18nManager.get_text("welcome_message", user_lang_code)
    await message.answer(welcome_text)

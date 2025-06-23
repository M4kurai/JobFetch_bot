from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.keyboards import builders
from app.locales.i18n_manager import I18nManager

router = Router()


@router.message(Command(commands="sources"))
async def process_sources_command(message: Message):
    user_lang_code = message.from_user.language_code or I18nManager.get_default_lang()
    sources_text = I18nManager.get_text("handlers.sources_message", user_lang_code)
    await message.answer(
        sources_text,
        reply_markup=builders.get_job_site_selection_keyboard(user_lang_code),
    )

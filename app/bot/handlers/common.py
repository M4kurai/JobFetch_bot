from aiogram import Router
from aiogram.types import Message

from app.locales.i18n_manager import I18nManager

router = Router()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        user_lang_code = (
            message.from_user.language_code or I18nManager.get_default_lang()
        )
        echo_text = I18nManager.get_text("no_echo", user_lang_code)
        await message.reply(echo_text)

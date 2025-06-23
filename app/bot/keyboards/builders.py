from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.locales.i18n_manager import I18nManager


def get_job_site_selection_keyboard(user_lang_code: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=I18nManager.get_text("buttons.hh_button", user_lang_code),
        callback_data="select_site:hh",
    )
    builder.button(
        text=I18nManager.get_text("buttons.habr_button", user_lang_code),
        callback_data="select_site:habr",
    )
    builder.button(
        text=I18nManager.get_text("buttons.in_button", user_lang_code),
        callback_data="select_site:linkedin",
    )
    builder.row(
        InlineKeyboardButton(
            text=I18nManager.get_text("buttons.finish_button", user_lang_code),
            callback_data="finish_site_selection",
        )
    )
    builder.adjust(3)

    return builder.as_markup()

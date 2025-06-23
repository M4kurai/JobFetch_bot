# app/bot/menu/set_main_menu.py

import logging

from aiogram import Bot
from aiogram.types import BotCommand

from app.locales.i18n_manager import I18nManager

logger = logging.getLogger(__name__)


async def set_main_menu(bot: Bot):
    commands_by_lang = {}

    try:
        supported_langs = I18nManager.supported_languages()
        if not supported_langs:
            logger.warning(
                "No supported languages found. Falling back to default language."
            )
            supported_langs = [I18nManager.get_default_lang()]

    except AttributeError:
        logger.error(
            "I18nManager.supported_languages() method not found. Using default language only."
        )
        supported_langs = [I18nManager.get_default_lang()]
    except Exception as e:
        logger.error(
            f"Error getting supported languages: {e}. Using default language only."
        )
        supported_langs = [I18nManager.get_default_lang()]

    for lang_code in supported_langs:
        menu_commands_for_lang = []

        try:
            all_commands_data = I18nManager.get_group_texts("commands", lang_code)

            if isinstance(all_commands_data, dict):
                for cmd_name, description in all_commands_data.items():
                    if isinstance(cmd_name, str) and isinstance(description, str):
                        menu_commands_for_lang.append(
                            BotCommand(command=cmd_name, description=description)
                        )
                    else:
                        logger.warning(
                            f"Invalid type for command '{cmd_name}' or description '{description}' "
                            f"in 'commands' group for language '{lang_code}'. Skipping."
                        )
            else:
                logger.error(
                    f"Expected dict for 'commands' group in language '{lang_code}', "
                    f"but got {type(all_commands_data).__name__}. No commands will be set for this language."
                )

        except Exception as e:
            logger.error(
                f"Error processing 'commands' group for language {lang_code}: {e}. "
                "No commands will be set for this language."
            )

        commands_by_lang[lang_code] = menu_commands_for_lang

    for lang_code, commands in commands_by_lang.items():
        if commands:
            await bot.set_my_commands(commands, scope=None, language_code=lang_code)
            logger.info(
                f"Main menu set for language: {lang_code} with commands: {[c.command for c in commands]}"
            )
        else:
            logger.warning(
                f"No commands to set for language: {lang_code}. Skipping menu setup for this language."
            )

    logger.info("Finished setting up main menu for all supported languages.")

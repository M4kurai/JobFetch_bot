import asyncio
import logging
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.handlers import common, help, sources, start
from app.bot.menu.set_main_menu import set_main_menu
from app.core.config import Config, load_config
from app.locales.i18n_manager import I18nManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


async def main() -> None:
    try:
        config: Config = load_config()

        bot = Bot(
            token=config.tg_bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

        dp = Dispatcher()

        dp.include_router(start.router)
        dp.include_router(help.router)
        dp.include_router(sources.router)
        dp.include_router(common.router)

        project_root = Path(__file__).parent
        logger.info(f"Корневая директория проекта: {project_root}")

        logger.info("Загрузка локализации...")
        I18nManager.load_locales(str(project_root))

        await set_main_menu(bot)

        logger.info("Удаление pending updates...")
        await bot.delete_webhook(drop_pending_updates=True)

        logger.info("Запуск polling...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        logger.error(f"Тип ошибки: {type(e).__name__}")
        import traceback

        logger.error(f"Полная трассировка: {traceback.format_exc()}")
        sys.exit(1)
    finally:
        if "bot" in locals():
            await bot.session.close()
            logger.info("Бот остановлен")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Получен сигнал остановки (Ctrl+C)")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
        sys.exit(1)

import json
from pathlib import Path
from typing import Any, Dict


class I18nManager:
    """Менеджер для работы с локализацией."""

    _locales: dict[str, dict[str, Any]] = {}
    _default_lang = "ru"

    @classmethod
    def load_locales(cls, project_root: str) -> None:
        """Загружает локализации из файлов."""
        locales_path = Path(project_root) / "app" / "locales"

        for lang_dir in locales_path.iterdir():
            if lang_dir.is_dir():
                lang_code = lang_dir.name
                strings_file = lang_dir / "strings.json"

                if strings_file.exists():
                    with open(strings_file, encoding="utf-8") as f:
                        cls._locales[lang_code] = json.load(f)

    @classmethod
    def get_text(cls, key: str, lang_code: str = None) -> str:
        """Получает локализованный текст по ключу."""
        if lang_code is None:
            lang_code = cls._default_lang

        # Если язык не найден, используем язык по умолчанию
        if lang_code not in cls._locales:
            lang_code = cls._default_lang

        # Получаем текст или возвращаем ключ, если текст не найден
        return cls._locales.get(lang_code, {}).get(key, key)

    @classmethod
    def get_default_lang(cls) -> str:
        """Возвращает язык по умолчанию."""
        return cls._default_lang

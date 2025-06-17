from pathlib import Path
from typing import Any

import yaml


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
                strings_file = lang_dir / "strings.yaml"

                if strings_file.exists():
                    with open(strings_file, encoding="utf-8") as f:
                        cls._locales[lang_code] = yaml.safe_load(f)
                else:
                    print(
                        f"Warning: strings.yaml not found for language '{lang_code}' at {strings_file}"
                    )

    @classmethod
    def get_text(cls, key: str, lang_code: str = None) -> str:
        """Получает локализованный текст по ключу.
        Если язык или ключ не найдены, возвращает ключ."""

        # Определяем язык для поиска
        effective_lang_code = cls._default_lang if lang_code is None else lang_code

        # Если запрошенный язык не загружен, пытаемся использовать язык по умолчанию
        if effective_lang_code not in cls._locales:
            print(
                f"Warning: Language '{effective_lang_code}' not loaded. Falling back to default '{cls._default_lang}'."
            )
            effective_lang_code = cls._default_lang
            if effective_lang_code not in cls._locales:
                # Если даже язык по умолчанию не загружен, выводим предупреждение и возвращаем ключ
                print(
                    f"Error: Default language '{cls._default_lang}' not loaded. Cannot retrieve text for key '{key}'."
                )
                return key

        # Получаем текст или возвращаем ключ, если текст не найден
        return cls._locales.get(effective_lang_code, {}).get(key, key)

    @classmethod
    def get_default_lang(cls) -> str:
        return cls._default_lang

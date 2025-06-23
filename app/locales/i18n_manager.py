from pathlib import Path
from typing import Any

import yaml


class I18nManager:
    _locales: dict[str, dict[str, Any]] = {}
    _default_lang = "ru"

    @classmethod
    def load_locales(cls, project_root: str) -> None:
        locales_path = Path(project_root) / "app" / "locales"

        cls._locales = {}

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
        print(f"Loaded locales for languages: {list(cls._locales.keys())}")

    @classmethod
    def get_text(cls, key: str, lang_code: str = None) -> str:
        effective_lang_code = cls._default_lang if lang_code is None else lang_code

        if effective_lang_code not in cls._locales:
            print(
                f"Warning: Language '{effective_lang_code}' not loaded. Falling back to default '{cls._default_lang}'."
            )
            effective_lang_code = cls._default_lang
            if effective_lang_code not in cls._locales:
                print(
                    f"Error: Default language '{cls._default_lang}' not loaded. Cannot retrieve text for key '{key}'."
                )
                return key
        current_locale_data = cls._locales.get(effective_lang_code, {})

        parts = key.split(".")
        text = current_locale_data
        for part in parts:
            if isinstance(text, dict):
                text = text.get(part)
            else:
                text = None
                break

        if text is None:
            print(
                f"Warning: Text for key '{key}' not found in language '{effective_lang_code}'."
            )
            return key

        return text

    @classmethod
    def get_default_lang(cls) -> str:
        return cls._default_lang

    @classmethod
    def supported_languages(cls) -> list[str]:
        return list(cls._locales.keys())

    @classmethod
    def get_group_texts(
        cls, group_name: str, lang_code: str
    ) -> dict[str, Any]:  # <-- НОВЫЙ МЕТОД
        lang_data = cls._locales.get(lang_code)
        if not lang_data:
            lang_data = cls._locales.get(cls._default_lang, {})

        group_data = lang_data.get(group_name)
        if not isinstance(group_data, dict):
            return {}

        return group_data

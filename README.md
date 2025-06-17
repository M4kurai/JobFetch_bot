# 🤖 JobFetch Bot

Telegram-бот для мониторинга вакансий: парсит сайты по заданным параметрам, фильтрует и присылает подходящие предложения прямо в Telegram.

![CI](https://github.com/M4kurai/JobFetch_bot/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

### 📌 Планы по развитию
| Статус | Функция |
|--------|---------|
| ✅     | Реакция на команды `/start`, `/help` |
| ✅     | CI/CD (GitHub Actions) |
| ✅     | Настройка через `.env` |
| ✅     | Асинхронная архитектура |
| ✅     | Поддержка локализации (i18n) |
| 🔜     | Парсинг вакансий с различных источников |
| 🔜     | Фильтры: город, должность, язык |
| 🔜     | Telegram-интерфейс на основе `aiogram 3` |
| 🔜     | Хранение истории поиска |
| 🔜     | ML: рекомендации по резюме |

---

## 📦 Стек технологий

| Компонент        | Описание |
|------------------|----------|
| Язык             | Python 3.11+ |
| Фреймворк бота   | [Aiogram 3](https://docs.aiogram.dev/en/latest/) |
| Конфигурация     | Environs + .env |
| Сборка/зависимости | Poetry |
| Линтинг/форматирование | Ruff |
| CI               | GitHub Actions |
| Локализация      | YAML + менеджер i18n |

---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/M4kurai/JobFetch_bot.git
cd JobFetch_bot
```
### 2. Установи зависимости
```bash
poetry install
```
### 3. Создай .env на основе примера
```bash
cp .env.example .env
```
#### И укажи свой Telegram Bot API токен:
```
BOT_TOKEN=your_token_here
```
### 4. Запусти бота
```bash
poetry run python main.py
```
### 🧪 CI / Проверки
Каждый коммит в main:

🔎 Проверяется линтером ruff
🧼 Проверяется форматирование (ruff format)
📦 Собирается окружение через Poetry
✅ Готов к запуску автотестов (pytest, позже)

### 🗂️ Структура проекта
```
📁 app/
├── bot/            # Telegram-логика: хендлеры и клавиатуры
│   ├── handlers/   # Команды /start, /help и т.д.
│   └── keyboards/  # Reply/Inline-кнопки
├── core/           # Конфигурация (.env, инициализация)
└── locales/        # Файлы локализации (строки интерфейса, теперь в формате YAML)

📄 main.py          # Точка входа
📄 .env             # Настройки окружения (в .gitignore)
```
### 📈 Roadmap
 Парсинг вакансий с HH и других источников

 Расписание обновлений 

 Хранение истории откликов 

 ML-модуль для приоритезации вакансий

 Админ-панель / управление подписками

 Docker-сборка и деплой

### 🔐 Лицензия
Проект распространяется под лицензией [MIT](https://github.com/M4kurai/JobFetch_bot/blob/master/LICENSE).

### 🤝 Контакты
Автор: [Dmitrii Makushin](https://github.com/M4kurai)
📧 Email: me@makurai.ru

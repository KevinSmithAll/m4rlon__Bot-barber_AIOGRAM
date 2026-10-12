# 💈 BarberBot

<p align="center">
  <b>Telegram-бот для удобной записи к барберу</b>
  <br />
  Автоматизация расписания, управление записями и взаимодействие с клиентами — прямо в Telegram.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="aiogram" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge" alt="Development" />
</p>

<p align="center">
  <a href="https://github.com/KevinSmithAll/m4rlon__Bot-barber_AIOGRAM">Репозиторий</a> •
  <a href="https://github.com/KevinSmithAll/m4rlon__Bot-barber_AIOGRAM/issues">Сообщить о проблеме</a>
</p>

---

## `$ whoami`

**BarberBot** — Telegram-бот, созданный для упрощения записи клиентов к барберу Владимиру Оболенцеву.

Проект позволяет организовать взаимодействие с клиентами, работать с расписанием и управлять записями без необходимости использовать отдельный веб-сайт.

Основная цель — сделать процесс записи удобным для клиентов и сократить количество рутинных действий для мастера.

## `$ features --list`

- 📅 **Запись на стрижку** — взаимодействие с системой записи через Telegram.
- 🗓️ **Работа с расписанием** — организация и обработка записей клиентов.
- 🔎 **Проверка записей** — предусмотрены отдельные обработчики для работы с существующими записями.
- ❌ **Управление записями** — предусмотрен функционал удаления записей.
- 🛠️ **Администрирование** — отдельный модуль обработчиков для административных задач.
- ⏰ **Автоматизация** — планировщик для выполнения периодических задач.
- 🗄️ **Хранение данных** — SQLite для работы с данными приложения.

## `$ tech-stack`

| Технология | Назначение |
|:--|:--|
| Python | Основной язык разработки |
| aiogram | Асинхронное взаимодействие с Telegram Bot API |
| SQLite | Хранение данных |
| APScheduler | Планирование периодических задач |
| asyncio | Асинхронное выполнение приложения |

## `$ tree -L 2`

```text
m4rlon__Bot-barber_AIOGRAM/
├── database/       # Работа с базой данных
├── functions/      # Вспомогательные функции
├── handlers/       # Обработчики команд и событий
├── keyboards/      # Клавиатуры и кнопки Telegram
├── states/         # Состояния диалогов
├── main.py         # Точка входа приложения
└── README.md       # Документация проекта
```

## `$ git clone`

### 1. Клонирование репозитория

```bash
git clone https://github.com/KevinSmithAll/m4rlon__Bot-barber_AIOGRAM.git
cd m4rlon__Bot-barber_AIOGRAM
```

### 2. Создание виртуального окружения

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Установка зависимостей

Если в проекте используется `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Если файла нет, установи необходимые зависимости, указанные в импортах проекта, и добавь их в `requirements.txt` для воспроизводимой установки.

### 4. Настройка конфигурации

Создай файл `.env` в корне проекта и перенеси в него токен Telegram-бота:

```env
BOT_TOKEN=your_telegram_bot_token
```

Получить новый токен можно у [@BotFather](https://t.me/BotFather).

Перед запуском необходимо настроить `main.py`, чтобы он считывал `BOT_TOKEN` из переменных окружения, а не хранил токен непосредственно в исходном коде.

### 5. Запуск

После настройки конфигурации и установки зависимостей:

```bash
python main.py
```

## `$ terminal --welcome`

```text
┌──(developer㉿barber-bot)-[~/m4rlon__Bot-barber_AIOGRAM]
└─$ python main.py

[INFO] Initializing BarberBot...
[INFO] Loading application modules...
[INFO] Starting scheduler...
[INFO] Connecting to Telegram API...
[ OK ] Bot is running.
[INFO] Waiting for incoming updates...
```

*Пример оформления терминального вывода. Фактические сообщения зависят от настроек логирования приложения.*

## `$ security --check`

- Не храни токены и пароли непосредственно в исходном коде.
- Не добавляй `.env` и файлы с секретами в Git.
- Используй `.gitignore` для исключения конфигурации и локальных файлов базы данных.
- Если токен уже попал в публичный репозиторий, отзови его и создай новый через [@BotFather](https://t.me/BotFather).
- Ограничивай доступ к административным функциям бота.

## `$ roadmap`

- [ ] Улучшение обработки ошибок и логирования.
- [ ] Расширение возможностей управления расписанием.
- [ ] Улучшение конфигурации и безопасности.
- [ ] Добавление автоматизированных тестов.
- [ ] Подготовка к развёртыванию на сервере.

## `$ contact`

**Разработчик:** [KevinSmithAll](https://github.com/KevinSmithAll)

**Email:** [kirill.marlon@yandex.ru](mailto:kirill.marlon@yandex.ru)

**Issues:** [Сообщить об ошибке или предложить улучшение](https://github.com/KevinSmithAll/m4rlon__Bot-barber_AIOGRAM/issues)

---

<p align="center">
  <b>Built with Python, aiogram and ☕</b>
  <br />
  <sub>Less routine. More style.</sub>
</p>

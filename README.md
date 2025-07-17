<<<<<<< HEAD
📡 Space Fetcher

Python-проект для автоматической загрузки космических изображений и их публикации в Telegram-канал.

🔭 Возможности:
	🚀 Скачивание фотографий последнего запуска SpaceX (через Flickr)
	🌌 Загрузка Astronomy Picture of the Day (APOD) от NASA
	🌍 Получение изображений Земли с орбиты через NASA EPIC API
	🤖 Публикация изображений из папки images/ в Telegram-канал с задержкой
	    - Публикация сначала по порядку, потом в случайном порядке
	    - Поддержка автоматического добавления новых файлов
=======
# 📡 Space Fetcher

Python-проект для автоматической загрузки космических изображений и их публикации в Telegram-канал.

🔭 Возможности:
	🚀 Скачивание фотографий последнего запуска SpaceX (через Flickr)
	🌌 Загрузка Astronomy Picture of the Day (APOD) от NASA
	🌍 Получение изображений Земли с орбиты через NASA EPIC API
	🤖 Публикация изображений из папки images/ в Telegram-канал с задержкой
	    - Публикация сначала по порядку, потом в случайном порядке
	    - Поддержка автоматического добавления новых файлов


Все изображения сохраняются в папку `images/`.

---

## 🔧 Установка

1. Склонируйте репозиторий или скопируйте файлы в свою директорию
2. Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
<<<<<<< HEAD
4. Создайте файл .env в корне проекта и добавьте в него свои ключи:

```bash
API_KEY_NASA=ваш_ключ_от_NASA_API
TELEGRAM_BOT_API=токен_бота_от_BotFather
TELEGRAM_CHAT_ID=ID_чата_или_канала
```
Получить API-ключ можно на сайте [api.nasa.gov](https://api.nasa.gov/)
Telegram API можно получить через [@BotFather](https://t.me/BotFather)
Узнать chat_id можно, отправив сообщение боту.

## ▶️ Использование

1. Скачивание изображений

- SpaceX (последний запуск):

```bash
python fetch_spacex_images.py
```

- SpaceX (по ID запуска):

```bash
python fetch_spacex_images.py <launch_id>
```

- NASA APOD:

```bash
python fetch_apod_images.py
```

- NASA EPIC:

```bash
python fetch_epic_images.py
```

2. Публикация изображений в Telegram

- Запуск с дефолтной задержкой (4 часа):

```bash
python space_img_bot.py
```

- Можно указать таймер отправки изображений через аргумент:

```bash
python space_img_bot.py 3600  # отправка каждые 60 минут
```


После выполнения скрипта в папке images/ появятся картинки с разных источников.
Если папка images/ отсутствует, она будет создана автоматически.

## 📁 Структура
- images/ — все скачанные изображения
- utils.py — вспомогательные функции
- space_img_bot.py — бот для Telegram
- fetch_spacex_images.py — загрузка SpaceX
- fetch_apod_images.py — загрузка APOD
- fetch_epic_images.py — загрузка EPIC

## 📦 Зависимости
- requests — HTTP-запросы
- python-dotenv — чтение .env-файла
- python-telegram-bot==13.15 — работа с Telegram Bot API
- os, time, argparse, random, logging — встроенные модули Python
=======
4. Создайте файл .env в корне проекта и добавьте в него свой API-ключ от NASA:
=======
4. Создайте файл .env в корне проекта и добавьте в него свои ключи:


```bash
API_KEY_NASA=ваш_ключ_от_NASA_API
TELEGRAM_BOT_API=токен_бота_от_BotFather
TELEGRAM_CHAT_ID=ID_чата_или_канала
```
Получить API-ключ можно на сайте [api.nasa.gov](https://api.nasa.gov/)
Telegram API можно получить через [@BotFather](https://t.me/BotFather)
Узнать chat_id можно, отправив сообщение боту.

## ▶️ Использование

1. Скачивание изображений

- SpaceX (последний запуск):

```bash
python fetch_spacex_images.py
```

- SpaceX (по ID запуска):

```bash
python fetch_spacex_images.py <launch_id>
```

- NASA APOD:

```bash
python fetch_apod_images.py
```

- NASA EPIC:

```bash
python fetch_epic_images.py
```

2. Публикация изображений в Telegram

- Запуск с дефолтной задержкой (4 часа):

```bash
python space_img_bot.py
```

- Можно указать таймер отправки изображений через аргумент:

```bash
python space_img_bot.py 3600  # отправка каждые 60 минут
```


После выполнения скрипта в папке images/ появятся картинки с разных источников.
Если папка images/ отсутствует, она будет создана автоматически.

## 📁 Структура
- images/ — все скачанные изображения
- utils.py — вспомогательные функции
- space_img_bot.py — бот для Telegram
- fetch_spacex_images.py — загрузка SpaceX
- fetch_apod_images.py — загрузка APOD
- fetch_epic_images.py — загрузка EPIC

<<<<<<< HEAD
- os — для работы с файловой системой
- requests — для запросов к API
- dotenv — для работы с переменными окружения
- urllib.parse — для разбора ссылок

=======
## 📦 Зависимости
- requests — HTTP-запросы
- python-dotenv — чтение .env-файла
- python-telegram-bot==13.15 — работа с Telegram Bot API
- os, time, argparse, random, logging — встроенные модули Python


## 🔗 Используемые API

- [SpaceX Launches API](https://api.spacexdata.com/v5/launches)
- [NASA APOD API](https://api.nasa.gov/planetary/apod)
- [NASA EPIC API](https://api.nasa.gov/EPIC)


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

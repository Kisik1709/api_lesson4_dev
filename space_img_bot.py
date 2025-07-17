import os
import time
import random
import logging
import argparse
import telegram
from dotenv import load_dotenv
from utils import create_folder, setup_logger
<< << << < HEAD
<< << << < HEAD
== == == =


def creat_parser():
    parser = argparse.ArgumentParser(
        description="Скрипт для автоматической загрузки изображений в телеграм канал")
    parser.add_argument("post_delay", nargs="?", type=int, default=14400,
                        help="Отсрочка таймера отправки изображений")
    return parser


<< << << < HEAD
def get_img_folder(image_dir):


== == == =


def get_images_from_dir(image_dir):

    all_images = [f for f in os.listdir(image_dir) if f.lower().endswith((
        ".jpg", ".png", ".jpeg", ".gif"))]
    if not all_images:
        return []
    return all_images


<< << << < HEAD


== == == =
== == == =


def main():
    load_dotenv()


<< << << < HEAD


<< << << < HEAD
 setup_logger()
  token = os.getenv("TELEGRAM_BOT_API")
   if not token:
== == == =
    setup_logger()
    token = os.getenv("TELEGRAM_BOT_API")
    if not token:

        print("Нет ключа Telegram")
        return

    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not chat_id:
        print("ID chat Telegram не добавлен")
        return

    parser = creat_parser()
    time_delay = parser.parse_args()
    post_delay = time_delay.post_delay

    image_dir = create_folder()
    random_mode = False

<< << << < HEAD
    all_images = get_img_folder(image_dir)
== == == =
    all_images = get_images_from_dir(image_dir)

    current_images = all_images.copy()

    bot = telegram.Bot(token=token)

    while True:
        if not current_images:
<< << << < HEAD
            fresh_list = get_img_folder(image_dir)

            if not fresh_list:
                print("В папке нет изображений")
                time.sleep(30)
                continue

            new_img = list(set(fresh_list) - set(all_images))
            all_images.extend(new_img)

            current_images = all_images.copy()
            if random_mode:
                random.shuffle(current_images)
            else:
                random_mode = True

        image = current_images.pop(0)

        try:
            with open(os.path.join(image_dir, image), "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
        except telegram.error.TelegramError:
            logging.exception("Ошибка отправки")
        time.sleep(post_delay)
== == == =
 token = os.getenv("TELEGRAM_BOT_API")
  chat_id = "@thebestspaceimg"
   bot = telegram.Bot(token=token)

    text = "Привет, я бот и я в этом канале!"
=======
            fresh_images = get_images_from_dir(image_dir)


            if not fresh_images:
                print("В папке нет изображений")
                time.sleep(30)
                continue

            fresh_images_to_add = list(set(fresh_images) - set(all_images))
            all_images.extend(fresh_images_to_add)

            current_images = all_images.copy()
            if random_mode:
                random.shuffle(current_images)
            else:
                random_mode = True

        image = current_images.pop(0)

        try:
            with open(os.path.join(image_dir, image), "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
        except telegram.error.TelegramError:
            logging.exception(f"Ошибка отправки: {image}")
        time.sleep(post_delay)


if __name__ == "__main__":
    main()

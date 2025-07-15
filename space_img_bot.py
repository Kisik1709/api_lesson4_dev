import os
import time
import random
import logging
import argparse
import telegram
from dotenv import load_dotenv
from utils import create_folder


def creat_parser():
    parser = argparse.ArgumentParser(
        description="Скрипт для автоматической загрузки изображений в телеграм канал")
    parser.add_argument("post_delay", nargs="?", type=int, default=14400,
                        help="Отсрочка таймера отправки изображений")
    return parser


def get_img_folder(image_dir):
    all_images = [f for f in os.listdir(image_dir) if f.lower().endswith((
        ".jpg", ".png", ".jpeg", ".gif"))]
    if not all_images:
        return []
    return all_images


def main():
    load_dotenv()
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

    all_images = get_img_folder(image_dir)
    current_list_img = all_images.copy()

    bot = telegram.Bot(token=token)

    while True:
        if not current_list_img:
            fresh_list = get_img_folder(image_dir)

            if not fresh_list:
                print("В папке нет изображений")
                time.sleep(30)
                continue

            new_img = list(set(fresh_list) - set(all_images))
            all_images.extend(new_img)

            current_list_img = all_images.copy()
            if random_mode:
                random.shuffle(current_list_img)
            else:
                random_mode = True

        i = current_list_img.pop(0)
        logging.getLogger(__name__)
        try:
            with open(os.path.join(image_dir, i), "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
        except Exception:
            logging.exception("Ошибка отправки")
        time.sleep(post_delay)


if __name__ == "__main__":
    main()

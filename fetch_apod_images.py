import os
import logging
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, extract_file_extension, existing_number, setup_logger


def get_links_nasa_apod(token):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    img_count = 30
    params = {
        "api_key": token,
        "count": img_count
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    apod_images = response.json()

    links = []
    for image in apod_images:
        if image.get("media_type") != "image":
            continue
        img_link = image.get("hdurl") or image.get("url")
        if not img_link:
            continue
        links.append(img_link)
    return links


def fetch_nasa_apod(links, filepath, prefix, number):
    for num, link in enumerate(links, start=number or 1):
        ext = extract_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{num}{ext}"
        load_img(link, filename, filepath)


def main():
    load_dotenv()
    setup_logger()
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return

    links = get_links_nasa_apod(token_nasa)
    if not links:
        print("Нет доступных изображений")
        return
    img_filepath = create_folder()
    prefix = "nasa_apod"
    number = existing_number(img_filepath, prefix)

    try:
        fetch_nasa_apod(links, img_filepath, prefix, number)
    except requests.exceptions.RequestException:
        logging.exception("Ошибка загрузки изображений")


if __name__ == "__main__":
    main()

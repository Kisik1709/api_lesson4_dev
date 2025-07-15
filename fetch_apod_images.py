import os
import logging
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, extract_file_extension, existing_number


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


def get_download_settings(token):
    links = get_links_nasa_apod(token)
    if not links:
        print("Нет доступных изображений")
        return
    img_filepath = create_folder()
    prefix = "nasa_apod"
    number = existing_number(img_filepath, prefix)
    return links, img_filepath, prefix, number


def fetch_nasa_apod(token):
    links, img_filepath, prefix, number = get_download_settings(token)

    for i, link in enumerate(links, start=number or 1):
        ext = extract_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{i}{ext}"
        load_img(link, filename, img_filepath)


def main():
    load_dotenv()
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
    logger = logging.getLogger(__name__)
    try:
        fetch_nasa_apod(token_nasa)
    except requests.exceptions.RequestException:
        logger.exception("Ошибка загрузки изображений")


if __name__ == "__main__":
    main()

import os
import logging
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, existing_number, setup_logger


def get_links_nasa_epic(token):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()

    links = []
    for image in epic_images[:5]:
        date = image["date"].split()[0].replace("-", "/")
        image_id = image["image"]
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png"
        links.append(img_url)
    return links, params


def fetch_nasa_epic(links, params, filepath, prefix, number):
    for num, link in enumerate(links, start=number or 1):
        filename = f"{prefix}{num}.png"
        load_img(link, filename, filepath, params)


def main():
    load_dotenv()
    setup_logger()
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return

    links, params = get_links_nasa_epic(token_nasa)
    img_filepath = create_folder()
    prefix = "nasa_epic"
    number = existing_number(img_filepath, prefix)

    try:
        fetch_nasa_epic(links, params, img_filepath, prefix, number)
    except requests.exceptions.RequestException:
        logging.exception("Ошибка загрузки изображений")


if __name__ == "__main__":
    main()

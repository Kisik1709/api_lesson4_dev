from utils import create_folder, load_img, extract_file_extension, count_next_file_index
import os
import logging
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, extract_file_extension, existing_number, setup_logger
from utils import create_folder, load_img, check_file_extension, get_next_img_number
<< << << < HEAD
<< << << < HEAD
== == == =
>>>>>> > 935d8bd(Разнес функционал по модулям, добавлена функция уникальной нумерации)
== == == =
>>>>>> > 155da4c(Refactor bot to: - Use argparse for publishing delay with fallback - Check required .env variables - Refresh image list when new files appear - Switch to random order after first cycle - Handle missing or empty image directory)


def get_links_nasa_apod(token, img_count):
    nasa_url = "https://api.nasa.gov/planetary/apod"


<< << << < HEAD
    img_count = 30
    params = {
        "api_key": token,
        "count": img_count
== == == =
    params = {
        "api_key": token,
<< << << < HEAD
        "count": 30
>> >>>> > 935d8bd(Разнес функционал по модулям, добавлена функция уникальной нумерации)
== == == =
        "count": img_count
>> >>>> > 155da4c(Refactor bot to: - Use argparse for publishing delay with fallback - Check required .env variables - Refresh image list when new files appear - Switch to random order after first cycle - Handle missing or empty image directory)
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
<< << << < HEAD
<< << << < HEAD
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
== == == =
    response_data = response.json()
== == == =
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
<< << << < HEAD
    setup_logger()
== == == =

    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
<< << << < HEAD
<< << << < HEAD

    links = get_links_nasa_apod(token_nasa)
== == == =

    img_count = 30

    links = get_links_nasa_apod(token_nasa, img_count)

    if not links:
        print("Нет доступных изображений")
        return
    img_filepath = create_folder()
    prefix = "nasa_apod"
<< << << < HEAD
    number = existing_number(img_filepath, prefix)

    try:
        fetch_nasa_apod(links, img_filepath, prefix, number)
    except requests.exceptions.RequestException:
        logging.exception("Ошибка загрузки изображений")
== == == =
    try:
        fetch_nasa_apod(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")
== == == =
    number = count_next_file_index(img_filepath, prefix)

    fetch_nasa_apod(links, img_filepath, prefix, number)




if __name__ == "__main__":
    main()

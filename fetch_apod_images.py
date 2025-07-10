from utils import create_folder, load_img, check_file_extension, get_next_img_number
from utils import create_folder, load_img, extract_file_extension, existing_number, setup_logger
from dotenv import load_dotenv
import requests
import logging
import os
<< << << < HEAD
== == == =
>>>>>> > 935d8bd(Разнес функционал по модулям, добавлена функция уникальной нумерации)


def get_links_nasa_apod(token):
    nasa_url = "https://api.nasa.gov/planetary/apod"


<< << << < HEAD
    img_count = 30
    params = {
        "api_key": token,
        "count": img_count
== == == =
    params = {
        "api_key": token,
        "count": 30
>> >>>> > 935d8bd(Разнес функционал по модулям, добавлена функция уникальной нумерации)
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
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

    links = []
    for item in response_data:
        if item.get("media_type") == "image":
            img_link = item.get("hdurl") or item.get("url")
            if img_link:
                links.append(img_link)
    return links


def fetch_nasa_apod(token):
    links = get_links_nasa_apod(token)
    if not links:
        print("Нет доступных изображений")
        return
    folder_path_img = create_folder()
    prefix = "nasa_apod"
    next_number = get_next_img_number(prefix, folder_path_img)

    for link in links:
        ext = check_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{next_number}{ext}"
        load_img(link, filename, folder_path_img)
        next_number += 1



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
== == == =
    try:
        fetch_nasa_apod(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")



if __name__ == "__main__":
    main()

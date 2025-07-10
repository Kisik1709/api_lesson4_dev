from utils import create_folder, load_img, check_file_extension, get_next_img_number
from utils import create_folder, load_img, extract_file_extension, existing_number, setup_logger
import argparse
import requests
import logging
<< << << < HEAD


def create_parser():
    parser = argparse.ArgumentParser(
        description="Скрипт для скачивания изображений с сайта SpaceX")
    parser.add_argument("launch_id", nargs="?", default=None,
                        help="ID запуска SpaceX. Если не указан, будет использован последний запуск.")
    return parser


def get_links_spacex(launch_id):
    url = "https://api.spacexdata.com/v5/launches/"
    if launch_id:
        url += launch_id

    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()

    if launch_id:
        photo_links = launches.get(
            "links", {}).get("flickr", {}).get("original", [])
        return photo_links
    else:
        for launch in reversed(launches):


== == == =


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "launch_id", nargs="?",
        help="ID запуска SpaceX. Если не указан, будет использован последний запуск.")
    return parser


def get_links_spacex(launch_id=None):
    if launch_id:
        url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/"

    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()

    if launch_id:
        photo_links = response_data.get(
            "links", {}).get("flickr", {}).get("original", [])
        return photo_links
    else:
        for launch in reversed(response_data):
            photo_links = launch.get(
                "links", {}).get("flickr", {}).get("original", [])
            if photo_links:
                return photo_links
    return []


<< << << < HEAD


def download_spacex_images(links, filepath, prefix, number):
    for num, link in enumerate(links, start=number or 1):
        ext = extract_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{num}{ext}"
        load_img(link, filename, filepath)


def main():
    setup_logger()
    parser = create_parser()
    namespace = parser.parse_args()
    launch_id = namespace.launch_id


== == == =


def download_spacex_images(launch_id):
    links = get_links_spacex(launch_id)
    if not links:
        print("Изображения не найдены")
        return


<< << << < HEAD
img_filepath = create_folder()
 prefix = "spacex_"
  number = existing_number(img_filepath, prefix)

   try:
        download_spacex_images(links, img_filepath, prefix, number)
    except requests.exceptions.RequestException:
        logging.exception("Ошибка загрузки изображений")
== == == =
folder_path_img = create_folder()
 prefix = "spacex_"
  next_number = get_next_img_number(prefix, folder_path_img)

   for link in links:
        ext = check_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{next_number}{ext}"
        load_img(link, filename, folder_path_img)
        next_number += 1


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    launch_id = namespace.id
    if not launch_id:
        launch_id = input("Введите ID запуска: ").strip()
    try:
        download_spacex_images(launch_id)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")


if __name__ == "__main__":
    main()

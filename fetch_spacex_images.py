import logging
import requests
import argparse
from utils import create_folder, load_img, extract_file_extension, existing_number


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
            photo_links = launch.get(
                "links", {}).get("flickr", {}).get("original", [])
            if photo_links:
                return photo_links
    return []


def get_download_settings(launch_id):
    links = get_links_spacex(launch_id)
    if not links:
        print("Изображения не найдены")
        return
    img_filepath = create_folder()
    prefix = "spacex_"
    number = existing_number(img_filepath, prefix)
    return links, img_filepath, prefix, number


def download_spacex_images(launch_id):

    links, img_filepath, prefix, number = get_download_settings(launch_id)

    for i, link in enumerate(links, start=number or 1):
        ext = extract_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{i}{ext}"
        load_img(link, filename, img_filepath)


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    launch_id = namespace.launch_id
    logger = logging.getLogger(__name__)
    try:
        download_spacex_images(launch_id)
    except requests.exceptions.RequestException:
        logger.exception("Ошибка загрузки изображений")


if __name__ == "__main__":
    main()

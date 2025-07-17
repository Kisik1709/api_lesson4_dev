import requests
import argparse
from utils import create_folder, load_img, extract_file_extension, count_next_file_index


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


def download_spacex_images(links, filepath, prefix, number):
    for num, link in enumerate(links, start=number or 1):
        ext = extract_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"{prefix}{num}{ext}"
        load_img(link, filename, filepath)


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    launch_id = namespace.launch_id

    links = get_links_spacex(launch_id)
    if not links:
        print("Изображения не найдены")
        return

    img_filepath = create_folder()
    prefix = "spacex_"
    number = count_next_file_index(img_filepath, prefix)

    download_spacex_images(links, img_filepath, prefix, number)


if __name__ == "__main__":
    main()

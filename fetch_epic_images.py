import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from utils import create_folder, load_img, count_next_file_index


def get_links_nasa_epic(token, img_count):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()

    links = []
    for image in epic_images[:img_count]:
        date = datetime.fromisoformat(
            image["date"]).strftime("%Y/%m/%d")

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

    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return

    img_count = 5

    links, params = get_links_nasa_epic(token_nasa, img_count)
    img_filepath = create_folder()
    prefix = "nasa_epic"
    number = count_next_file_index(img_filepath, prefix)

    fetch_nasa_epic(links, params, img_filepath, prefix, number)


if __name__ == "__main__":
    main()

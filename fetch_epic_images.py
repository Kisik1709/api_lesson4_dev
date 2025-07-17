from utils import create_folder, load_img, count_next_file_index
from datetime import datetime
import os
import logging
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, existing_number, setup_logger
from utils import create_folder, load_img, get_next_img_number
<< << << < HEAD
<< << << < HEAD
== == == =
== == == =
>>>>>> > 155da4c(Refactor bot to: - Use argparse for publishing delay with fallback - Check required .env variables - Refresh image list when new files appear - Switch to random order after first cycle - Handle missing or empty image directory)


def get_links_nasa_epic(token, img_count):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()


<< << << < HEAD


<< << << < HEAD
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


== == == =
   response_data = response.json()
== == == =
    epic_images = response.json()
>>>>>> > 155da4c(Refactor bot to: - Use argparse for publishing delay with fallback - Check required .env variables - Refresh image list when new files appear - Switch to random order after first cycle - Handle missing or empty image directory)

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


<< << << < HEAD
   setup_logger()
== == == =

   token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
<< << << < HEAD
<< << << < HEAD

   links, params = get_links_nasa_epic(token_nasa)
    img_filepath = create_folder()
    prefix = "nasa_epic"
    number = existing_number(img_filepath, prefix)

    try:
        fetch_nasa_epic(links, params, img_filepath, prefix, number)
    except requests.exceptions.RequestException:
        logging.exception("Ошибка загрузки изображений")
== == == =
   try:
        fetch_nasa_epic(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")
=======

    img_count = 5

    links, params = get_links_nasa_epic(token_nasa, img_count)
    img_filepath = create_folder()
    prefix = "nasa_epic"
    number = count_next_file_index(img_filepath, prefix)

    fetch_nasa_epic(links, params, img_filepath, prefix, number)



if __name__ == "__main__":
    main()

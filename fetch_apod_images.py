import os
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, check_file_extension, get_next_img_number


def get_links_nasa_apod(token):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": token,
        "count": 30
    }

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
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
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
    try:
        fetch_nasa_apod(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")


if __name__ == "__main__":
    main()

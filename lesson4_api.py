import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def create_folder():
    base_dir = os.path.dirname(__file__)
    folder_name_img = "images"
    folder_path_img = os.path.join(base_dir, folder_name_img)
    if not os.path.exists(folder_path_img):
        os.makedirs(folder_path_img)
    return folder_path_img


def load_img(url, filename, dir_path):
    full_path = os.path.join(dir_path, filename)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(full_path, "wb") as file:
        file.write(response.content)


def check_file_extension(img_link):
    _, ext = os.path.splitext(urlparse(img_link).path)
    return ext


def get_links_spacex():
    url = "https://api.spacexdata.com/v5/launches/"

    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()

    for launch in reversed(response_data):
        photo_links = launch["links"]["flickr"]["original"]
        if photo_links:
            return photo_links
    return []


def fetch_spacex_last_launch():
    links = get_links_spacex()
    folder_path_img = create_folder()

    for i, link in enumerate(links, start=1):
        ext = check_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"spasex_{i}{ext}"
        load_img(link, filename, folder_path_img)


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
    folder_path_img = create_folder()

    for i, link in enumerate(links, start=1):
        ext = check_file_extension(link)
        if not ext:
            ext = ".jpg"
        filename = f"nasa_apod{i}{ext}"
        load_img(link, filename, folder_path_img)


def get_links_nasa_epic(token):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    response_data = response.json()

    links = []
    for item in response_data[:5]:
        date = item["date"].split()[0].replace("-", "/")
        image = item["image"]
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={token}"
        links.append(img_url)
    return links


def fetch_nasa_epic(token):
    links = get_links_nasa_epic(token)
    folder_path_img = create_folder()

    for i, link in enumerate(links, start=1):
        filename = f"nasa_epic{i}.png"
        load_img(link, filename, folder_path_img)


def main():
    load_dotenv()
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
    try:
        fetch_spacex_last_launch()
        fetch_nasa_apod(token_nasa)
        fetch_nasa_epic(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")


if __name__ == "__main__":
    main()

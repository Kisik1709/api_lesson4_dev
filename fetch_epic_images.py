import os
import requests
from dotenv import load_dotenv
from utils import create_folder, load_img, get_next_img_number


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
    prefix = "nasa_epic"
    next_number = get_next_img_number(prefix, folder_path_img)

    for link in links:
        filename = f"{prefix}{next_number}.png"
        load_img(link, filename, folder_path_img)
        next_number += 1


def main():
    load_dotenv()
    token_nasa = os.getenv("API_KEY_NASA")
    if not token_nasa:
        print("Ошибка API ключа для сайта NASA")
        return
    try:
        fetch_nasa_epic(token_nasa)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки: {e}")


if __name__ == "__main__":
    main()

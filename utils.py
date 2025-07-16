import os
import logging
import requests
from urllib.parse import urlparse


def setup_logger():
    logging.basicConfig(level=logging.INFO, filename="app.log", filemode="a")


def create_folder():
    base_dir = os.path.dirname(__file__)
    img_filename = "images"
    img_filepath = os.path.join(base_dir, img_filename)
    os.makedirs(img_filepath, exist_ok=True)
    return img_filepath


def load_img(url, filename, dir_path, params=None):
    full_path = os.path.join(dir_path, filename)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    with open(full_path, "wb") as file:
        file.write(response.content)


def extract_file_extension(img_link):
    _, ext = os.path.splitext(urlparse(img_link).path)
    return ext


def existing_number(filepath, prefix):
    return sum(1 for f in os.listdir(filepath) if f.startswith(prefix)) + 1

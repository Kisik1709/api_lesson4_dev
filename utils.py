from urllib.parse import urlparse
import requests
import logging
import os
<< << << < HEAD
== == == =


<< << << < HEAD


def setup_logger():
    logging.basicConfig(level=logging.INFO, filename="app.log", filemode="a")


def create_folder():
    base_dir = os.path.dirname(__file__)
    img_filename = "images"
    img_filepath = os.path.join(base_dir, img_filename)
    os.makedirs(img_filepath, exist_ok=True)
    return img_filepath


def load_img(url, filename, dir_path, params=None):


== == == =


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


<< << << < HEAD
response = requests.get(url, params=params, headers=headers)
== == == =
response = requests.get(url, headers=headers)

response.raise_for_status()

with open(full_path, "wb") as file:
    file.write(response.content)


<< << << < HEAD
def extract_file_extension(img_link):


== == == =


def check_file_extension(img_link):

    _, ext = os.path.splitext(urlparse(img_link).path)
    return ext


<< << << < HEAD


def existing_number(filepath, prefix):
    return sum(1 for f in os.listdir(filepath) if f.startswith(prefix)) + 1


== == == =


def get_next_img_number(prefix, folder_path_img):
    exist_num = [
        int(f.replace(prefix, "").split(".")[0])
        for f in os.listdir(folder_path_img)
        if f.startswith(prefix) and f.replace(prefix, "").split(".")[0].isdigit()
    ]

    next_number = max(exist_num, default=0) + 1
    return next_number

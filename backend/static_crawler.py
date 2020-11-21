"""This file crawl Kaggle and ISIC API before serving to client."""
from json import dump
from utils import get_isic_full


def download_isic():
    """Download 100 ISIC images and save the metadata."""
    full_data = get_isic_full(10)
    with open('isic.json', 'w') as f:
        dump(full_data, f)


if __name__ == '__main__':
    download_isic()

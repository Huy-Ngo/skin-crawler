"""This file crawl Kaggle and ISIC API before serving to client."""
from json import dump
from utils import get_isic_full


def download_isic(num_images):
    """Download ISIC images and save the metadata."""
    full_data = get_isic_full(num_images)
    with open('isic.json', 'w') as f:
        dump(full_data, f)


if __name__ == '__main__':
    download_isic(100)

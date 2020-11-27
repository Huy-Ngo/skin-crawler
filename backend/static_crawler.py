from json import dump
from pathlib import Path

from isic import ISIC_getdata
from kaggle import download, validate, SkinCancerMnist
from wikimedia import wikimedia_crawl
from yandex import yandex_crawler


def get_kaggle_full():
    """Download data from Kaggle."""
    full_data = []

    if validate():
        dataset = 'dinhanhx/skin-cancer-mnist-ham10000'
        path = Path('./static/kaggle')
        dataset_path = download(dataset, path)
        scm = SkinCancerMnist(dataset_path)
        for i in range(scm.get_len_dataset()):
            full_data.append(scm.get_img_metadata(i))

    return full_data


if __name__ == '__main__':
    full_kaggle = get_kaggle_full()
    full_isic = ISIC_getdata(100, 100)
    full_wiki = wikimedia_crawl(500)
    full_yandex = yandex_crawler(20)
    with open('data.json', 'w') as f:
        dump({
            'kaggle': full_kaggle,
            'isic': full_isic,
            'wiki': full_wiki,
            'yandex': full_yandex
        }, f)

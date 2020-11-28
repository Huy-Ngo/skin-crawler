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


def add_host(data, host):
    """Make the image path absolute for those served by the server."""
    for i in range(len(data)):
        data[i]['image'] = f'http://{host}/{data[i]["image"]}'
    return data


if __name__ == '__main__':
    host = 'localhost:5000'
    full_kaggle = get_kaggle_full()
    full_isic = ISIC_getdata(300, 300)
    full_wiki = wikimedia_crawl(500)
    full_yandex = yandex_crawler(20)
    print('Crawled:')
    print(len(full_kaggle), 'image(s) from Kaggle')
    print(len(full_isic), 'image(s) from ISIC')
    print(len(full_wiki), 'image(s) from Wikimedia')
    print(len(full_yandex), 'image(s) from Yandex Image')
    with open('data.json', 'w') as f:
        dump({
            'kaggle': add_host(full_kaggle, host),
            'isic': add_host(full_isic, host),
            'wiki': full_wiki,
            'yandex': full_yandex
        }, f)

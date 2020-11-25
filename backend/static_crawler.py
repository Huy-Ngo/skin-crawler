from json import dump, dumps
from pathlib import Path

from isic import ISIC_getdata
from kaggle import download, validate, SkinCancerMnist
from wikimedia import wikimedia_crawl


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


def get_isic_full(n_images):
    """Download data from ISIC."""
    retrieved_data = ISIC_getdata(n_images, n_images)
    full_data = []
    for img in retrieved_data:
        img_full = {
            'path': f'static/isic/{img["Name"]}.jpg',
            'original_host': 'ISIC API',
            'original_link': 'https://isic-archive.com/api/v1/',
            'caption': f'ISIC {img["Caption"]}'
        }
        full_data.append(img_full)
    return full_data


def get_wiki(n_images):
    unformatted_data = wikimedia_crawl(n_images)
    data = []
    for entry in unformatted_data:
        new_entry = {
            'path': entry['Image source'],
            'original_host': entry['Host'],
            'original_link': entry['Origin URL'],
            'caption': entry['Title']
        }
        data.append(new_entry)
    return data


if __name__ == '__main__':
    full_kaggle = get_kaggle_full()
    print(dumps(full_kaggle, indent=2))
    full_isic = get_isic_full(100)
    print(dumps(full_isic, indent=2))
    full_wiki = get_wiki(500)
    with open('downloaded.json', 'w') as f:
        dump({
            'kaggle': full_kaggle,
            'isic': full_isic,
            'wiki': full_wiki
        }, f)

from json import load, dump, dumps
from pathlib import Path

from kaggle import download, validate, SkinCancerMnist
from isic import ISIC_getdata

with open('config.json', 'r') as f:
    data = load(f)
    host = data['host']


def get_kaggle_full(n_images):
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


if __name__ == '__main__':
    full_kaggle = get_kaggle_full(10)
    print(dumps(full_kaggle, indent=2))
    full_isic = get_isic_full(10)
    print(dumps(full_isic, indent=2))
    with open('downloaded.json', 'w') as f:
        dump({
            'kaggle': full_kaggle,
            'isic': full_isic
        }, f)

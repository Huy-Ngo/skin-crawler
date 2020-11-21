# from kaggle import download, validate, SkinCancerMnist
from isic import ISIC_getdata
from json import load

with open('config.json', 'r') as f:
    data = load(f)
    host = data['host']


def get_isic_full(n_images):
    retrieved_data = ISIC_getdata(n_images, n_images)
    full_data = []
    for img in retrieved_data:
        img_full = {
            'path': f'images/{img["Name"]}.jpg',
            'original_host': 'ISIC API',
            'original_link': 'https://isic-archive.com/api/v1/',
            'caption': f'ISIC {img["Caption"]}'
        }
        full_data.append(img_full)
    return full_data


if __name__ == '__main__':
    from json import dumps
    print(dumps(get_isic_full(20), indent=2))

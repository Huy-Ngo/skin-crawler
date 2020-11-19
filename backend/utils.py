from kaggle import download, validate, SkinCancerMnist
from isic import ISIC_getdata


def get_isic_full(n_images):
    retrieved_data = ISIC_getdata(n_images, n_images)
    full_data = []
    for img in retrieved_data:
        img_full = {
            'path': f'isic/Image/{img["Name"]}.jpg',
            'ext_path': False,
            'original_host': 'ISIC API',
            'original_link': 'https://isic-archive.com/api/v1/',
            'caption': f'ISIC {img["Caption"]}'
        }
        full_data.append(img_full)
    return full_data



if __name__ == '__main__':
    from json import dumps
    print(dumps(get_isic_full(20), indent=2))


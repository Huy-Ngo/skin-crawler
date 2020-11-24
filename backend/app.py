from json import load
from random import shuffle

from flask import Flask

from wikimedia import wikimedia_crawl

with open('downloaded.json', 'r') as f:
    data = load(f)
    kaggle_data = data['kaggle']
    isic_data = data['isic']

app = Flask(__name__)


def fetch_wiki(num_img):
    unformatted_data = wikimedia_crawl(num_img)
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


@app.route('/kaggle/<int:num_img>')
def get_kaggle(num_img):
    """Get `num_img` images from Kaggle API."""
    data = kaggle_data
    if len(data) > num_img:
        shuffle(data)
        data = data[:num_img]
    return {'data': data}


@app.route('/isic/<int:num_img>')
def get_isic(num_img):
    """Get `num_img` images from ISIC API."""
    data = isic_data
    if len(data) > num_img:
        shuffle(data)
        data = data[:num_img]
    return {'data': data}


@app.route('/wiki/<int:num_img>')
def get_wiki(num_img):
    """Get `num_img` images from WikiMedia."""
    return {'data': fetch_wiki(num_img)}


@app.route('/all/<int:num_img>')
def get_all(num_img):
    """Get `num_img` images from all sources."""
    data = kaggle_data + isic_data
    data += fetch_wiki(100)
    if len(data) > num_img:
        shuffle(data)
        data = data[:num_img]
    return {'data': data}

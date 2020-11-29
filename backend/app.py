from json import load
from random import shuffle

from flask import Flask

with open('data.json', 'r') as f:
    data = load(f)
    kaggle_data = data['kaggle']
    isic_data = data['isic']
    wiki_data = data['wiki']
    yandex_data = data['yandex']
    data = kaggle_data + isic_data + wiki_data + yandex_data
    shuffle(data)

app = Flask(__name__)


def get_page(data, page):
    """Get nth page of a data, with each page having 20 entries."""
    begin = page * 20
    end = page * 20 + 20
    if begin >= len(data):
        return []
    elif end >= len(data):
        return data[begin:]
    else:
        return data[begin:end]


@app.route('/kaggle/<int:page>')
def get_kaggle(page):
    """Get a page of 20 images from Kaggle API."""
    return {'data': get_page(kaggle_data, page)}


@app.route('/isic/<int:page>')
def get_isic(page):
    """Get a page of 20 images from ISIC API."""
    return {'data': get_page(isic_data, page)}


@app.route('/wiki/<int:page>')
def get_wiki(page):
    """Get a page of 20 images from WikiMedia."""
    return {'data': get_page(wiki_data, page)}


@app.route('/yandex/<int:page>')
def get_yandex(page):
    """Get a page of 20 images from WikiMedia."""
    return {'data': get_page(yandex_data, page)}


@app.route('/all/<int:page>')
def get_all(page):
    """Get a page of 20 images from all sources."""
    return {'data': get_page(data, page)}

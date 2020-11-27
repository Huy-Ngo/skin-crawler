from json import load
from random import shuffle

from flask import Flask

with open('downloaded.json', 'r') as f:
    data = load(f)
    kaggle_data = data['kaggle']
    isic_data = data['isic']
    wiki_data = data['wiki']
    yandex_data = data['yandex']

app = Flask(__name__)


def randomize(data, n_images):
    """Get randomly `n_images` from data.

    Return the unchanged data
    if the data size is smaller or equal to `n_images`.
    """
    if len(data) > n_images:
        shuffle(data)
        data = data[:n_images]
    return data


@app.route('/kaggle/<int:n_images>')
def get_kaggle(n_images):
    """Get `n_images` images from Kaggle API."""
    return {'data': randomize(kaggle_data, n_images)}


@app.route('/isic/<int:n_images>')
def get_isic(n_images):
    """Get `n_images` images from ISIC API."""
    return {'data': randomize(isic_data, n_images)}


@app.route('/wiki/<int:n_images>')
def get_wiki(n_images):
    """Get `n_images` images from WikiMedia."""
    return {'data': randomize(wiki_data, n_images)}


@app.route('/wiki/<int:n_images>')
def get_yandex(n_images):
    """Get `n_images` images from WikiMedia."""
    return {'data': randomize(yandex_data, n_images)}


@app.route('/all/<int:n_images>')
def get_all(n_images):
    """Get `n_images` images from all sources."""
    data = kaggle_data + isic_data + wiki_data + yandex_data
    if len(data) > n_images:
        shuffle(data)
        data = data[:n_images]
    return {'data': data}

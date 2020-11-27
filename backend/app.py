from json import load
from random import shuffle

from flask import Flask

with open('data.json', 'r') as f:
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


@app.route('/yandex/<int:n_images>')
def get_yandex(n_images):
    """Get `n_images` images from WikiMedia."""
    return {'data': randomize(yandex_data, n_images)}


@app.route('/all/<int:n_images>')
def get_all(n_images):
    """Get `n_images` images from all sources."""
    data = kaggle_data + isic_data + wiki_data + yandex_data
    return {'data': randomize(data, n_images)}


@app.route('/kaggle')
def get_kaggle_full():
    """Get `n_images` images from Kaggle API."""
    return {'data': kaggle_data}


@app.route('/isic')
def get_isic_full():
    """Get `n_images` images from ISIC API."""
    return {'data': isic_data}


@app.route('/wiki')
def get_wiki_full():
    """Get `n_images` images from WikiMedia."""
    return {'data': wiki_data}


@app.route('/yandex')
def get_yandex_full():
    """Get `n_images` images from WikiMedia."""
    return {'data': yandex_data}


@app.route('/all')
def get_all_full():
    """Get `n_images` images from all sources."""
    data = kaggle_data + isic_data + wiki_data + yandex_data
    return {'data': data}

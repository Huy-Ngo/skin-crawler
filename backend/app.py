from json import load
from random import shuffle

from flask import Flask

with open('downloaded.json', 'r') as f:
    data = load(f)
    kaggle_data = data['kaggle']
    isic_data = data['isic']

app = Flask(__name__)


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


@app.route('/all/<int:num_img>')
def get_all(num_img):
    """Get `num_img` images from all sources."""
    data = kaggle_data + isic_data
    if len(data) > num_img:
        shuffle(data)
        data = data[:num_img]
    return {'data': data}

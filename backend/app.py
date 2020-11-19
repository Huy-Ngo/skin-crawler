from flask import Flask
from utils import get_isic_full

app = Flask(__name__)


@app.route('/images/<name>')
def get_image(name):
    """Serve images in the image folder."""
    pass


@app.route('/kaggle/<int:num_img>')
def get_kaggle(num_img):
    """Get `num_img` images from Kaggle API."""
    pass


@app.route('/isic/<int:num_img>')
def get_isic(num_img):
    """Get `num_img` images from ISIC API."""
    full_data = get_isic_full(num_img)
    return {'data': full_data}


@app.route('/all/<int:num_img>')
def get_all(num_img):
    """Get `num_img` images from all sources."""
    pass

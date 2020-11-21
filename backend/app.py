from flask import Flask

app = Flask(__name__)


@app.route('/kaggle/<int:num_img>')
def get_kaggle(num_img):
    """Get `num_img` images from Kaggle API."""
    pass


@app.route('/all/<int:num_img>')
def get_all(num_img):
    """Get `num_img` images from all sources."""
    pass

# Crawler for skin cancer images

This project attempts to create a crawler for dermoscopic images of skin cancer.
This includes both frontend and backend.

The backend consists of packages to crawl images from websites and a web server
to collect them and serve the images as an API.

The frontend consumes the API and displays information to the user.

## How to run

### Backend

- Add Kaggle API token at `~/.kaggle/kaggle.json`
- In `backend/`, run `static_crawler.py`, since we use some sources that forces us to download the images
- Run Flask server:

```bash
EXPORT FLASK_APP=app.py
EXPORT FLASK_ENV=development
flask run
```

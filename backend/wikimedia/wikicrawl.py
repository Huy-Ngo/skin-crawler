import requests
from bs4 import BeautifulSoup
import urllib.request
import json


def wikimedia_crawl(page=100):
	"""To get images from wikimedia when search for skin cancer.

	Parameters
		page : int.

	Returns:
		A list of dictionaries.
		Each dictionary has
			- Image source: an url
			- Host: "Wikimedia"
			- Original URL: an url
			- Title: "Wikimedia <number>"
	"""
	url = f"https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=\
	{page}&offset=0&profile=default&search=Basal-cell+carcinoma\
	&advancedSearch-current={{}}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"

	response = requests.get(url)
	soup = BeautifulSoup(response.content, "lxml")
	images = soup.find_all("img")

	number = 0
	data_list = []
	for image in images:
		image_src = image["src"]
		title = "Wikimedia "+str(number)
		number += 1
		data = {}
		data['Image source'] = image_src
		data['Host'] = "Wikimedia"
		data['Origin URL'] = url
		data['Title'] = title
		data_list.append(data)

	return data_list

if __name__ == '__main__':
	wikimedia_crawl(100)

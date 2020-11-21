import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://commons.wikimedia.org/w/index.php?search=Basal-cell+carcinoma&title=Special:Search&go=Go&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

images = soup.find_all("img")

number = 0

for image in images:
	image_src = image["src"]
	print(image_src)
	urllib.request.urlretrieve(image_src, str(number))
	number +=1
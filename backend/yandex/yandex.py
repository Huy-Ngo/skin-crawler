import requests
from bs4 import BeautifulSoup

def spider(max_pic_num):
    url="https://yandex.com/images/search?text=skin%20cancer%20dermoscopy"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    counter = 0
    for link in soup.findAll('a', {"class": "serp-item__link"}):
        href = "https://yandex.com" + link.get('href')
        print(href)
        counter = counter + 1 
        if (counter == max_pic_num):
            break

spider(3)
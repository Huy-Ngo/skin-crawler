import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('yandex'):
    os.mkdir('yandex')
  
def download_images(url,i):
    img_data = requests.get(url).content
    with open("yandex/"+str(i)+'.jpg','wb+') as f:
        f.write(img_data)
    f.close()

def to_dict(index,sauce,img_sauce):
 table={
     "source" : sauce,
     "img_link" : img_sauce,
     "tittle":"yandex"+str(index)
 }   
 return table

def spider(max_pic_num):
    url="https://yandex.com/images/search?text=skin%20cancer%20dermoscopy"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    counter = 1
    for link in soup.findAll('a', {"class": "serp-item__link"}):
        #get link
        href = link.get('href')
        #printing image link
        string = href.split("img_url=")[1]
        convert = string.replace("%2F","/")
        convert2= convert.replace("%3A",":")
        og_link=convert2.split('&text')[0]
        print(og_link)
        
        #printing source
        newstring = string.split('%3A%2F%2F')[1]
        source = newstring.split('%2F')[0]
        print(source)

        #download image
        download_images(og_link,counter)

        #create dict
        #create dict
        vars()["table"+str(counter)]=to_dict(counter,source,og_link)
        print(vars()["table"+str(counter)])

        if (counter == max_pic_num):
            break
        else:
            counter = counter + 1

spider(3)

import requests
from bs4 import BeautifulSoup

def get_single_item(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for item_name in soup.findAll('div',{"class":"MMOrganicSnippet-Text"}):
        print (item_name.string)
    for og_link in soup.findAll('a',{"class":"Link Link_theme_outer Path-Item"}):
        print(og_link.get('href'))
    for image_og_link in soup.findAll('img',{"class":"MMImage-Origin"}):
        print(image_og_link['src'])

url = "https://yandex.com/images/search?text=skin%20cancer%20dermoscopy&pos=0&img_url=http%3A%2F%2Fwww.betterfamilyhealth.org%2Fimages%2F483xNxbenign-mole1.jpg.pagespeed.ic.-E8egXuWvx.jpg&rpt=simage"

get_single_item(url)
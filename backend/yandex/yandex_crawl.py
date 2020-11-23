import requests
from bs4 import BeautifulSoup


def to_dict(index, sauce, img_sauce):
    table = {
         "img_link": img_sauce,
         "source": sauce,
         "host": "Yandex",
         "tittle": "yandex"+str(index)
         }
    return table


def spider(max_pic_num):
    url = "https://yandex.com/images/search?text=skin%20cancer%20dermoscopy"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    counter = 1
    data_list = []
    for link in soup.findAll('a', {"class": "serp-item__link"}):
        # get link
        href = link.get('href')
        # getimage link
        string = href.split("img_url=")[1]
        convert = string.replace("%2F", "/")
        convert2 = convert.replace("%3A", ":")
        og_link = convert2.split('&text')[0]
        # get source
        newstring = string.split('%3A%2F%2F')[1]
        source = newstring.split('%2F')[0]
        # adding dict
        data = {}
        data['Image source'] = source
        data['Host'] = "Yandex"
        data['Origin URL'] = og_link
        data['Title'] = "Yandex" + str(counter)
        data_list.append(data)

        if (counter == max_pic_num):
            break
        else:
            counter = counter + 1
    return data_list


if __name__ == "__main__":
    spider(5)

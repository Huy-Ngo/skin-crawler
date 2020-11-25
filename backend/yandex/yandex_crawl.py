import requests
from bs4 import BeautifulSoup


def yandex_crawler(max_pic_num):
    """To get images from Yandex when search for skin cancer dermoscopy.
    Parameters
        max_pic_num : int.
    Returns:
        A list of dictionaries.
        Each dictionary has
            - Image source: The image address
            - Host: "Yandex"
            - Original URL: URL to the web page where the image is found
            - Title: The title of the image
    """
    url = "https://yandex.com/images/search?text=skin%20cancer%20dermoscopy"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    counter = 1
    data_list = []
    for link in soup.findAll('a', {"class": "serp-item__link"}):
        # get link
        href = link.get('href')
        yandex_link="https://yandex.com/" + href
        # getimage link
        string = href.split("img_url=")[1]
        convert = string.replace("%2F", "/")
        convert2 = convert.replace("%3A", ":")
        og_link = convert2.split('&text')[0]
        # adding dict
        data = {}
        data['Image source'] = og_link
        data['Host'] = "Yandex"
        data['Origin URL'] = yandex_link
        data['Title'] = "\n".join([img['alt'] for img in link.findChildren("img", alt = True)])
        data_list.append(data)

        if (counter == max_pic_num):
            break
        else:
            counter = counter + 1
    return data_list


if __name__ == "__main__":
    yandex_crawler(5)

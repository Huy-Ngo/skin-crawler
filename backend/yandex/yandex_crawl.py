import requests
from bs4 import BeautifulSoup


def yandex_crawler(max_pic_num):
    """ To get images from Yandex when search for skin cancer dermoscopy.


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
    url = 'https://yandex.com/images/search?text=skin%20cancer%20dermoscopy'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    counter = 1
    data_list = []
    for link in soup.findAll('a', {'class': 'serp-item__link'}):
        # get link
        href = link.get('href')
        # getimage link
        img_link = href.split('img_url=')[1]
        img_link = img_link.replace('%2F', '/')
        img_link = img_link.replace('%3A', ':')
        img_link = img_link.split('&text')[0]
        # adding dict
        data = {}
        data['image source'] = img_link
        data['host'] = 'Searched via Yandex'
        data['origin URL'] = 'none'
        data['title'] = '\n'.join([img['alt'] for img in link.findChildren(
            'img', alt=True)])
        data_list.append(data)

        if (counter == max_pic_num):
            break
        else:
            counter += 1
    return data_list


if __name__ == '__main__':
    yandex_crawler(5)

import requests
from bs4 import BeautifulSoup


def wikimedia_crawl(result=100):
    """Get images from wikimedia when search for skin cancer.
    Parameters:
        result : int.

    Returns:
        A list of dictionaries.
        Each dictionary has
            - image: The image address
            - host: "Wikimedia"
            - original: URL to the web page where the image is found
            - title: the title of the image
    """
    url = f"https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=\
    {result}&offset=0&profile=default&search=Basal-cell+carcinoma\
    &advancedSearch-current={{}}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    infos = soup.find_all("a", "image")
    data_list = []
    for info in infos:
        title = info["href"].replace("/wiki/", "")
        origin_url = "https://commons.wikimedia.org" + info["href"]
        data = {}
        # request to origin url to get full image
        res = requests.get(origin_url)
        sp = BeautifulSoup(res.content, "html.parser")
        image = sp.find("img")
        data['host'] = "Wikimedia"
        data['original'] = origin_url
        data['title'] = title
        data['image'] = image["src"]
        data_list.append(data)

    return data_list


if __name__ == '__main__':
    wikimedia_crawl(100)

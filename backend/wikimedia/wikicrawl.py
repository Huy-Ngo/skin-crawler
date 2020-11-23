import requests
from bs4 import BeautifulSoup


def wikimedia_crawl(result=100):
    """To get images from wikimedia when search for skin cancer.

    Parameters
        result : int.

    Returns:
        A list of dictionaries.
        Each dictionary has
            - Image source: an url
            - Host: "Wikimedia"
            - Original URL: an url
            - Title: "Title"
    """
    url = f"https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=\
    {result}&offset=0&profile=default&search=Basal-cell+carcinoma\
    &advancedSearch-current={{}}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    infos = soup.find_all("a", "image")
    data_list = []
    for info in infos:
        title = info["href"].replace("/wiki/", "")
        origin_url = "mediawiki.org" + info["href"]
        data = {}
        # request to origin url to get full image
        res = requests.get("http://" + origin_url)
        sp = BeautifulSoup(res.content, "lxml")
        image = sp.find("img")
        data['Host'] = "Wikimedia"
        data['Origin URL'] = origin_url
        data['Title'] = title
        data['Image source'] = image["src"]
        data_list.append(data)

    return data_list


if __name__ == '__main__':
    wikimedia_crawl(100)

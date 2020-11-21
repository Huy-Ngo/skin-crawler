import requests
import os
from io import BytesIO
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


"""A module to fetch data from International Skin Imaging Collaboration API
For further information about the API: https://isic-archive.com/api/v1/
"""


def ISIC_request(response, num=100):
    """Fetching the metadata from images in ISIC archive by sending a HTTP
    request to the ISIC's REST API.
    Parameters:
        num(int): Number of the images you get from the archive,default is 100
    Returns:
        Json: Response metadata in JSON format
    """
    start_url = f'https://isic-archive.com/api/v1/image?limit={num} \
                  &sort=name&sortdir=1&detail=true'
    headers = {'Accept': 'application/json'}
    r = requests.get(start_url, headers=headers)
    data = r.json()
    return data


def check_dermoscopic(meta):
    """Checking if a image is acquired through dermoscopy by ISIC's API.
    Parameter:
    meta: The metadata of the image getting through the API
    Return:
    True if the image is acquired through dermoscopy, False if it isn't
    """

    if "image_type" not in meta["meta"]["acquisition"]:
        return False
    elif not str(meta["meta"]["acquisition"]["image_type"]) == "dermoscopic":
        return False
    return True


def check_melanoma(metadata):
    """Checking if a image is confirmed melanocytic by ISIC's API.
    Parameter:
        metadata: The metadata of the image getting through the API
    Return:
        True if the image is confirmed melanocytic, False if it isn't
    """
    if "melanocytic" not in metadata["meta"]["clinical"]:
        return False
    elif not metadata["meta"]["clinical"]["melanocytic"]:
        return False
    return True


def ISIC_getdata(numjson=20, numimage=20,
                 dermo_filter=False,
                 melano_filter=False,
                 path=os.getcwd()):
    """Download images of dermoscopic images and return their metadata.
    Parameters:
        numjson(int): Number of datasets of images from ISIC_request().
        numimage(int): Number of images you want from the dataset.
            Should be more than numjson.
        dermo_filter(bool): Get only want images acquired by dermoscopy
        melano_filter(bool): Get you only want images confirmed melanocytic
    Return: List of the metadata of the images downloaded
    """
    if (numjson < numimage):
        print("Invalid parameters")
    else:
        dataset = ISIC_request(numjson)
        image_data = {}
        datalist = []
        i = 0
        dir = path+"/static/isic/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        for set in dataset:
            if(dermo_filter is False or check_dermoscopic(set) and
                    melano_filter is False or check_melanoma(set)):
                image_data['Name'] = str(set['name'])
                image_data['Caption'] = str(set['_id'])
                if not os.path.exists(dir+image_data['Name']+'.jpg'):
                    headers = {
                        'Accept': 'application/json'
                    }
                    r = requests.get("https://isic-archive.com/api/v1/image/" +
                                     str(set['_id'])+"/download",
                                     headers=headers)
                    img = Image.open(BytesIO(r.content))
                    img.save(dir+image_data['Name']+'.jpg')
                datalist.append(image_data.copy())
                i += 1
                if(i == numimage):
                    break
        return datalist

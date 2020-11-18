import requests
import pandas as pd
import pathlib
import os
from io import BytesIO
from PIL import Image

"""A module to fetch data from International Skin Imaging Collaboration API"""
"""For further information about the API: https://isic-archive.com/api/v1/ """


def ISIC_request(response, num=100):
    """Fetching the metadata from images in ISIC archive by sending a HTTP
    request to the ISIC's REST API.

    Parameters:
        num(int): Number of the images you get from the archive,default is 100

    Returns:
        Json: Response metadata in JSON format
    """
    start_url = f'https://isic-archive.com/api/v1/image?limit={num} \
                  &sort=name&sortdir=-1&detail=true'
    headers = { 'Accept': 'application/json' }
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


def ISIC_getdata(numjson=200, numimage=20,
                 dermo_filter=True,
                 melano_filter=True,
                 export=True):
    """Download images of dermoscopic images and return their metadata.

    Parameters:
        numjson(int): Number of datasets of images from ISIC_request().
            Default is 100
        numimage(int): Number of images you want from the dataset.
            Should be more than numjson. Default is 20
        dermo_filter(bool): Checking if you only want images acquired by dermoscopy
            Default is `True`.
        melano_filter(bool): Checking if you only want images confirmed melanocytic
            Default is True
        export(bool): Option to choose if you want to export the metadata as a CSV
            file. Default is True

    Return: List of the metadata of the images downloaded
    """
    if (numjson < numimage or not
            isinstance(numjson, int) or not
            isinstance(numimage, int) or not
            isinstance(dermo_filter, bool) or not
            isinstance(melano_filter, bool) or not
            isinstance(export, bool)):
        print("Invalid parameters")
    else:
        dataset = ISIC_request(numjson)
        output = {}
        output2 = []
        i = 0
        for set in dataset:
            if(dermo_filter is False or check_dermoscopic(set) and
                    melano_filter is False or check_melanoma(set)):
                output['Id'] = str(set['_id'])
                output['Name'] = str(set['name'])
                if 'age_approx' in set['meta']['clinical']:
                    output['Age'] = str(set['meta']['clinical']['age_approx'])
                else:
                    output['Age'] = "Not known"
                if 'anatom_site_general' in set['meta']['clinical']:
                    output['General Anatomy Site'] = str(
                        set['meta']['clinical']['anatom_site_general'])
                else:
                    output['General Anatomy Site'] = "Not known"
                output['Description'] = str(set['dataset']['description'])
                if 'diagnosis' in set['meta']['clinical']:
                    output['Diagnosis'] = str(
                        set['meta']['clinical']['diagnosis'])
                else:
                    output['Diagnosis'] = "Not known"
                if 'sex' in set['meta']['clinical']:
                    output['Sex'] = str(set['meta']['clinical']['sex'])
                else:
                    output['Sex'] = "Not known"
                if melano_filter:
                    output['Confirmed Diagnosis'] = str(
                        set['meta']['clinical']['diagnosis_confirm_type'])
                headers = {
                    'Accept': 'application/json'
                }
                r = requests.get("https://isic-archive.com/api/v1/image/" +
                                 output['Id']+"/download", headers=headers)
                if not os.path.exists("Image"):
                    os.makedirs("Image")
                path = str(pathlib.Path(__file__).parent.absolute())
                img = Image.open(BytesIO(r.content))
                img.save(path+"/Image/"+str(output['Name'])+'.jpg')
                output2.append(output)
                i += 1
                if(i == numimage):
                    break
        if export:
            df = pd.DataFrame.from_dict(output2)
            df.to_csv(r''+str(pathlib.Path(__file__).parent.absolute()) +
                      '/Metadata.csv', index=False, header=True)
    return output2


if __name__ == "__main__":
    ISIC_getdata()

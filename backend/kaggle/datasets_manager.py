import os
import csv
from os import path
from pathlib import Path

DEFAULT_DOWNLOAD_PATH = path.join(Path.home(), Path('.kaggle/'))


def download(dataset, download_path=DEFAULT_DOWNLOAD_PATH):
    """Download a dataset from kaggle then save it to a directory.
    Parameters:
        dataset : a string.
        download_path : a string or any Path object.

    Return:
        dataset_path : full folder path where dataset is downloaded.

    Example:
        This is a link to a kaggle dataset:
        https://www.kaggle.com/dinhanhx/skin-cancer-mnist-ham10000

        dataset = 'dinhanhx/skin-cancer-mnist-ham10000'
        download_path = '~/.kaggle/'
        dataset_path = download(dataset, download_path)

        dataset_path = '~/.kaggle/dinhanhx/skin-cancer-mnist-ham10000/'
    """
    dataset_path = path.join(download_path, Path(dataset))
    try:
        os.mkdir(path.join(download_path, Path(dataset.split('/')[0])))
        os.mkdir(dataset_path)
    except FileExistsError:
        print(f'{dataset_path} already exists.')
        return dataset_path

    os.system(f'kaggle datasets download {dataset} -p {dataset_path} --unzip')
    return dataset_path


class SkinCancerMnist:
    """Make an object manipulating dataset skin-cancer-minist-ham10000
    only from dinhanhx

    A SkinCancerMnist object has
        attributes:
            __dataset_url : a string
            __dataset_path : a Path object
            __metadata_path : a Path object
            __img_metadata_list : a list of tuples.
                Each tuple has two elements.
                First element (Path object) is a path to an image
                Second element (Dict object) is a metadata of an image
        functions:
            get_img_metadata()
            get_dataset_url()
            get_len_dataset()
    """
    def __init__(self, dataset_path, full_path=False):
        """
        Parameters:
            dataset_path : a string or any Path object.
            full_path : if True then is non-relative path.
        """
        self.__dataset_url = 'https://www.kaggle.com/' \
                             'dinhanhx/skin-cancer-mnist-ham10000'

        self.__dataset_path = Path(dataset_path)
        if full_path:
            self.__dataset_path = self.__dataset_path.resolve()

        self.__metadata_path = path.join(self.__dataset_path,
                                         'HAM10000_metadata.csv')

        img_fpath_list = [path.join(self.__dataset_path, f)
                          for f in os.listdir(self.__dataset_path)
                          if '.csv' not in f]

        metadata_list = []
        with open(self.__metadata_path, 'r') as f:
            for line in csv.DictReader(f):
                metadata_list.append(dict(line))

        self.__img_metadata_list = []
        for img_fpath in img_fpath_list:
            img_id = Path(img_fpath).name.split('.')[0]
            for metada in metadata_list:
                if metada['image_id'] == img_id:
                    self.__img_metadata_list.append((img_fpath, metada))

    # def get_img_metadata_list(self):
    #     return self.__img_metadata_list

    def get_len_dataset(self):
        return len(self.__img_metadata_list)

    def get_img_metadata(self, index=0, title_style='HAM'):
        """Get an image and it's info from self.__img_metadata_list
        Parameters:
            index : an int.
            title_style : a str.
        Returns:
            a dictionary has
                - 'image'
                - 'host'
                - 'original'
                - 'title'
        """
        img_metadata = self.__img_metadata_list[index]
        if title_style == 'HAM':
            return {'image': img_metadata[0],
                    'host': 'Kaggle',
                    'original': self.__dataset_url,
                    'title': img_metadata[1]['lesion_id']}
        else:
            return {'image': img_metadata[0],
                    'host': 'Kaggle',
                    'original': self.__dataset_url,
                    'title': img_metadata[1]['image_id']}

    def get_dataset_url(self):
        return self.__dataset_url


if __name__ == '__main__':
    dataset_path = download('dinhanhx/skin-cancer-mnist-ham10000')
    scm = SkinCancerMnist(dataset_path)
    for i in range(scm.get_len_dataset()):
        print(scm.get_img_metadata(i))

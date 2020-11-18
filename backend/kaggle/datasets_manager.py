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
        None : if dataset is already existed in download path.

    Example:
        This is a link to a kaggle dataset:
        https://www.kaggle.com/aungpyaeap/tictactoe-endgame-dataset-uci

        dataset = 'aungpyaeap/tictactoe-endgame-dataset-uci'
        download_path = '~/.kaggle/'
        dataset_path = download(dataset, download_path)

        dataset_path = '~/.kaggle/aungpyaeap/tictactoe-endgame-dataset-uci/'
    """
    try:
        os.mkdir(path.join(download_path, Path(dataset.split('/')[0])))
        dataset_path = path.join(download_path, Path(dataset))
        os.mkdir(dataset_path)

    except FileExistsError:
        return None

    os.system(f'kaggle datasets download {dataset} -p {dataset_path} --unzip')
    return dataset_path


class SkinCancerMnist:
    """Make an object manipulating dataset skin-cancer-minist-ham10000
    from kmader

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
            get_img_metadata_list()
            get_dataset_url()
    """
    def __init__(self, dataset_path, full_path=False):
        """
        Parameters:
            dataset_path : a string or any Path object.
            full_path : if True then is non-relative path.
        """
        self.__dataset_url = 'https://www.kaggle.com/' \
                             'kmader/skin-cancer-mnist-ham10000'

        self.__dataset_path = Path(dataset_path)
        if full_path:
            self.__dataset_path = self.__dataset_path.resolve()

        self.__metadata_path = path.join(self.__dataset_path,
                                         'HAM10000_metadata.csv')

        img_fpath_list = [path.join(self.__dataset_path, f)
                          for f in os.listdir(path.join(self.__dataset_path,
                                                        'HAM10000_images_part_1/'))]  # noqa: E501

        img_fpath_list += [path.join(self.__dataset_path, f)
                           for f in os.listdir(path.join(self.__dataset_path,
                                                         'HAM10000_images_part_2/'))]  # noqa: E501

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

    def get_img_metadata_list(self):
        return self.__img_metadata_list

    def get_dataset_url(self):
        return self.__dataset_url


if __name__ == '__main__':
    dataset_path = 'data/kmader/skin-cancer-mnist-ham10000/'
    scm = SkinCancerMnist(dataset_path)
    print(*scm.get_img_metadata_list(), sep='\n')

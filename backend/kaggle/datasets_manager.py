import os
from pathlib import Path

DEFAULT_DOWNLOAD_PATH = os.path.join(Path.home(), Path('.kaggle/'))


def download(dataset, download_path=DEFAULT_DOWNLOAD_PATH):
    '''
    Parameters:
        dataset : a string.
        download_path : a string or any Path object/

    Abilities:
        To download a dataset from kaggle then save it to a directory.

    Returns:
        dataset_path : full folder path where dataset is downloaded.
        None : if dataset is already existed in download path.

    Example:
        This is a link to a kaggle dataset:
        https://www.kaggle.com/aungpyaeap/tictactoe-endgame-dataset-uci

        dataset = 'aungpyaeap/tictactoe-endgame-dataset-uci'
        download_path = '~/.kaggle/'
        dataset_path = download(dataset, download_path)

        dataset_path = '~/.kaggle/aungpyaeap/tictactoe-endgame-dataset-uci/'
    '''
    try:
        os.mkdir(os.path.join(download_path, Path(dataset.split('/')[0])))
        dataset_path = os.path.join(download_path, Path(dataset))
        os.mkdir(dataset_path)

    except FileExistsError:
        return None

    os.system(f'kaggle datasets download {dataset} -p {dataset_path} --unzip')
    return dataset_path


if __name__ == '__main__':
    download('aungpyaeap/tictactoe-endgame-dataset-uci')

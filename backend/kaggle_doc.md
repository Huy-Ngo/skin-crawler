# kaggle documentation

```Python
import kaggle
```

## Setup validation

```Python
kaggle.validate()
```

`validate()` checks for the existence of package kaggle and api token file.

Api token file is expected to have this path ~/.kaggle/kaggle.json

Package kaggle is expected to install with pip

This also prints what is missing to stdout.

Returns:
  - `True` if package kaggle and api token file exit.

## Download a dataset

```Python
dataset = 'aungpyaeap/tictactoe-endgame-dataset-uci'
dataset_path = kaggle.download(dataset)
```

`download()` downloads a dataset from kaggle then save it to a directory.

Parameters:
  - `dataset` : a string.
  - `download_path` : a string or any Path object.

Returns:
  - `dataset_path` : full folder path where dataset is downloaded.
  - `None` : if dataset is already existed in download path.

## Class skin_cancer_mnist

```Python
scm = skin_cancer_mnist(dataset_path)
print(*scm.get_img_metadata_list(), sep='\n')
```

`class skin_cancer_mnist` makes an object manipulating dataset skin-cancer-minist-ham10000 from kmader

A skin_cancer_mnist object has
  - attributes:
    - `__dataset_url` : a string
    - `__dataset_path` : a Path object
    - `__metadata_path` : a Path object
    - `__img_metadata_list` : a list of tuples. Each tuple has two elements. `First element` (Path object) is a path to an image. `Second element` (Dict object) is a metadata of an image
  - functions:
    - `get_img_metadata_list()`
    - `get_dataset_url()`

`__init__()`

Parameters:
  - `dataset_path` : a string or any Path object.
  - `full_path` : if True then is non-relative path.

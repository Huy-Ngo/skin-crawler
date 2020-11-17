# Kaggle documentation

```Python
import kaggle
```

## User documentation

## Get data from [skin cancer mnist](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)

```Python
if kaggle.validate():
  dataset = 'kmader/skin-cancer-mnist-ham10000'
  dataset_path = kaggle.download(dataset)
  scm = kaggle.skin_cancer_mnist(dataset_path)
  for img_metadata in scm.get_img_metadata_list():
    print('Image path: ', img_metadata[0])  # type(img_metadata[0]) returns str
    print('Image info: ', img_metadata[1])  # type(img_metadata[1]) returns dict
    print('===')
```

Firstly, it checks for kaggle api and kaggle package. Then it downloads the dataset then save it this directory `~/.kaggle/kmader/skin-cancer-mnist-ham10000`. For Windows, it's `YourUserName/.kaggle/kmader/skin-cancer-mnist-ham10000`. Secondly, it creates an object to manipulate the dataset. Finally it prints to stdout what that object has.

## Module documentation

### Setup validation

```Python
kaggle.validate()
```

`validate()` checks for the existence of package kaggle and api token file.

Api token file is expected to have this path `~/.kaggle/kaggle.json`

Package kaggle is expected to install with `pip install kaggle`

This also prints what is missing to stdout.

Returns:
  - `True` if package kaggle and api token file exit.

### Download a dataset

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

### Class skin_cancer_mnist

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

`get_dataset_url()`

Returns:
  - `self.__dataset_url`

`get_img_metadata_list()`

Returns
  - `self.__img_metadata_list`

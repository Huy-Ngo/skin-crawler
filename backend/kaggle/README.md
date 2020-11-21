# Kaggle documentation

```Python
import kaggle
```

## User documentation

## Get data from [skin cancer mnist](https://www.kaggle.com/dinhanhx/skin-cancer-mnist-ham10000)

```Python
if kaggle.validate():
    dataset = 'dinhanhx/skin-cancer-mnist-ham10000'
    dataset_path = kaggle.download(dataset)
    scm = kaggle.SkinCancerMnist(dataset_path)
    for i in range(scm.get_len_dataset()):
        print(scm.get_img_metadata(i))

```

Firstly, it checks for kaggle api and kaggle package. Then it downloads the dataset then save it to directory `~/.kaggle/dinhanhx/skin-cancer-mnist-ham10000`. For Windows, it's `YourUserName/.kaggle/dinhanhx/skin-cancer-mnist-ham10000`. Secondly, it creates an object to manipulate the dataset. Finally it prints to stdout what that object has.

## Module documentation

### Setup validation

```Python
validate()
```

`validate()` checks for the existence of package kaggle and api token file.

Api token file is expected to have this path `~/.kaggle/kaggle.json`

Package kaggle is expected to install with `pip install kaggle`

This also prints what is missing to stdout.

Returns:
  - `True` if package kaggle and api token file exit.

### Download a dataset

```Python
dataset = 'dinhanhx/skin-cancer-mnist-ham10000'
dataset_path = download(dataset)
```

`download()` downloads a dataset from kaggle then save it to a directory.

Parameters:
  - `dataset` : a string.
  - `download_path` : a string or any Path object.

Returns:
  - `dataset_path` : full folder path where dataset is downloaded.

### Class SkinCancerMnist

```Python
scm = SkinCancerMnist(dataset_path)
```

`class SkinCancerMnist` makes an object manipulating dataset skin-cancer-minist-ham10000 from dinhanhx

A SkinCancerMnist object has
  - attributes:
    - `__dataset_url` : a string
    - `__dataset_path` : a Path object
    - `__metadata_path` : a Path object
    - `__img_metadata_list` : a list of tuples. Each tuple has two elements. `First element` (Path object) is a path to an image. `Second element` (Dict object) is a metadata of an image
  - functions:
    - `get_img_metadata()`
    - `get_dataset_url()`
    - `get_len_dataset()`

`__init__()`

Parameters:
  - `dataset_path` : a string or any Path object.
  - `full_path` : if True then is non-relative path.


`get_img_metadata()`
Get an image and it's info from `self.__img_metadata_list`

Parameters:
  - `index` : an int.
  - `caption_style` : a str.

Returns:
  - a dictionary has
    - 'Image path' : full path to image
    - 'Host' : name of host
    - 'Original url' : orignal url
    - 'Caption' : image id

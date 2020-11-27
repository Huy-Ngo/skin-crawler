# Yandex documentation

## User guide

```Python
import json
from yandex import yandex_crawler
data_list = yandex_crawler(10)
for data in data_list:
    print(json.dumps(data, indent=4))
```

## Module documentation

### yandex_crawler

```Python
yandex_crawler(10)
```
Get images from Yandex when search for skin cancer dermoscopy.

Parameters:
- `max_pic_num` : int.

Returns:
A list of dictionaries.
Each dictionary has
- `image`: image address can be file path or url.
- `host`: "Yandex"
- `original`: URL to the web page where the image is found
- `title`: the title of the image

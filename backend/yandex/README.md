# Wikimedia documentation

## User guide

```Python
import json
from yandex import yandex_crawler
data_list = yandex_crawler(10)
for data in data_list:
    print(json.dumps(data, indent=2))
```

## Module documentation

### yandex_crawler

```Python
yandex_crawler(10)
```
To get images from Yandex when search for skin cancer dermoscopy.

Parameters:
- `max_pic_num` : int.

Returns:
A list of dictionaries.
Each dictionary has
- `Image source`: The image address
- `Host`: "Yandex"
- `Original URL`: URL to the web page where the image is found
- `Title`: The title of the image

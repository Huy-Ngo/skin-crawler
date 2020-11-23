# Wikimedia documentation

## User guide

```Python
import json
from yandex import spider
data_list = spider(10)
for data in data_list:
    print(json.dumps(data, indent=2))
```


## Module documentation

### wikimedia_crawl

```Python
spider(10)
```
To get images from Yandex when search for skin cancer dermoscopy.

Parameters:
- `max_pic_num` : int.

Returns:
A list of dictionaries.
Each dictionary has
- `Image source`: an url
- `Host`: "Yandex"
- `Original URL`: an url
- `Title`: "Yandex" + the order of current picture

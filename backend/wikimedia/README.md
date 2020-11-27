# Wikimedia documentation

## User guide

```Python
import json
from wikimedia import wikimedia_crawl
data_list = wikimedia_crawl(result=10)
for data in data_list:
    print(json.dumps(data, indent=4))
```


## Module documentation

### wikimedia_crawl

```Python
wikimedia_crawl(result=10)
```
To get images from wikimedia when search for skin cancer.

Parameters:
- `result` : int.

Returns:
A list of dictionaries.
Each dictionary has
- `image`: The image address
- `host`: "Wikimedia"
- `original`: URL to the web page where the image is found
- `title`: the title of the image

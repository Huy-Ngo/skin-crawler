# Wikimedia documentation

## User guide

```Python
import json
from wikimedia import wikimedia_crawl
data_list = wikimedia_crawl(page=10)
for data in data_list:
    print(json.dumps(data, indent=2))
```


## Module documentation

### wikimedia_crawl

```Python
wikimedia_crawl(page=10)
```
To get images from wikimedia when search for skin cancer.

Parameters:
- `page` : int.

Returns:
A list of dictionaries.
Each dictionary has
- `Image source`: an url
- `Host`: "Wikimedia"
- `Original URL`: an url
- `Title`: "Wikimedia <number>"

To use the module from terminal,run:

```shell script
$python isic-crawler.py --numjson $val1 --numimage $val2 --dermo $bool1 --melano $bool2
```

This module download images from API and keep it in "/Image" folder of the directory.

It will download $val2 images out of $val1 json responses.Be sure that $val1 is larger than or equal to $val2 at all times

If $val1 is larger than $val2 it might take more time to download metadata .By default both are set to 20

--dermo filters out image that is not acquired by dermoscopic. Default set to False

--melano filters out image that is not deemed "melanocytic" in the metadata. Default set to False

If you want to set any of those two filters one be sure that $val1 is a lot larger than $val2


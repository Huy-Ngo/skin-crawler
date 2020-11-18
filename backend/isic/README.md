To use the module from terminal,run:

```shell script
$python isic-crawler.py --numjson $json --numimage $img --dermo_filter $bool1 --melanoma_filter $bool2
```

This module download images from API and keep it in "/Image" folder of the directory.

It will download $img images out of $json json responses.Be sure that $json is larger than or equal to $img at all times

If $json is larger than $img it might take more time to download metadata .By default $json is set to 200 and $img 20

Dermo_filter filters out image that is not acquired by dermoscopic. Default set to False

Melano_filter filters out image that is not deemed "melanocytic" in the metadata. Default set to False

If you want to set any of those two filters one be sure that $numjson is a lot larger than $img


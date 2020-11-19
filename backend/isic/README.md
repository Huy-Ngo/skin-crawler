# Instruction
To use the module from terminal,run:

```shell script
$python isic-crawler.py --numjson $val1 --numimage $val2 --dermo $bool1 --melano $bool2
```

To call it as a function,go:

```shell script
isic-crawler(numjson = 20,numimage = 20,dermo_filter = False,melano_filter = False)
```

## Output

This module download images from API and keep it in "/Image" folder of the directory.

## Input

It will download $val2 images out of $val1 json responses.Be sure that $val1 is larger than or equal to $val2 at all times

- If $val1 is larger than $val2 it might take more time to download metadata .By default both are set to 20

- dermo_filter (or --dermo if you call in in termnial) filters out image that is not acquired by dermoscopic. Default set to False

- melano_filter (or --melano if you call it in terminal_   filters out image that is not deemed "melanocytic" in the metadata. Default set to False

If you want to set any of those two filters one be sure that $val1 is a lot larger than $val2


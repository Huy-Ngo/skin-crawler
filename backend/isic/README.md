# Instruction
To call it as a function,go:

```python
ISIC_getdata(numjson = 20,numimage = 20,dermo_filter = False,melano_filter = False,path = os.getcwd())
```

## Output

It will download numimage images out of numjson json responses.Be sure that numjson is larger than or equal to numimage at all times

This module download images from API and keep it in  "path/static/isic" folder of the directory,with path default being the current directory from where it is run from

## Input

- If numjson is much larger than numimage it might take more time to download metadata .By default both are set to 20

- dermo_filter (or --dermo if you call in in termnial) filters out image that is not acquired by dermoscopic. Default set to False

- melano_filter (or --melano if you call it in terminal_   filters out image that is not deemed "melanocytic" in the metadata. Default set to False


- path is the folder where it will create a static/isic folder that hold all of the image in it. Default is the directory where it is run from

If you want to set any of those two filters one be sure that numjson is a lot larger than numimage


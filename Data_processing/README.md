# Data Preprocessing
## Info
* Since the data used in this code needs to be in NRRD format, if we only have data files in other formats like DCM or MHD, we should convert the data before performing model segmentation.
## Inspect the nrrd data
* We convert the NRRD data into an MP4 file to ensure that the data is correct.
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ pip install pynrrd
u5453836@bechl2ctr1733907726803-rsl4p:~$ python inspect_nrrd.mp4
```


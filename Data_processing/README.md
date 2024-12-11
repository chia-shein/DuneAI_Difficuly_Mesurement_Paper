# Data Preprocessing
## Info
* Since the data used in this code needs to be in NRRD format, if we only have data files in other formats like DCM or MHD, we should convert the data before performing model segmentation.
![](https://github.com/chia-shein/DuneAI_Difficuly_Mesurement_Paper/blob/main/Data_processing/patient1_data.mp4)
## Inspect the nrrd data
* We convert the NRRD data into an MP4 file to ensure that the data is correct.\
“The script **inspect_nrrd.py** is used to check the data provided by the paper’s author.”\
“The script **inspect_nrrd_one.py** is used to check the data that our code has transformed.”
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ pip install pynrrd
u5453836@bechl2ctr1733907726803-rsl4p:~$ python inspect_nrrd.py
```

## Transfer mhd data to nrrd data
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ python mhd2nrrd.py
```

# Data Preprocessing
## Info
* Since the data used in this code needs to be in NRRD format, if we only have data files in other formats like DCM or MHD, we should convert the data before performing model segmentation.\
![patient1_data](https://github.com/user-attachments/assets/6656caaa-d89c-4b34-b87e-8afd5770e83f)

## Inspect the nrrd data
* We convert the NRRD data into an MP4 file to ensure that the data is correct.\
“The script **inspect_nrrd.py** is used to check the data provided by the paper’s author.”\
“The script **inspect_nrrd_one.py** is used to check the data that our code has transformed.”
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ pip install pynrrd
u5453836@bechl2ctr1733907726803-rsl4p:~$ python inspect_nrrd.py
```

## Transfer mhd data to nrrd data
* Ensure the nrrd file **data type** is **int16**.
* Ensure the nrrd file **data.min()** and **data.max()** are **-1000** and **3071**, respectively.
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ python mhd2nrrd.py
```

![image](https://github.com/user-attachments/assets/d0f15626-6986-4c46-929f-11f149d257ca)

## Compare the differences between the transferred data and the data provided in the paper.
* Sizes: CT images are all 512x512, but the number of slices is different. (No impact)
* Space directions: The resolution of the images. (No impact)
* Space origin: The coordinate origin. (Uncertain if there is any impact)

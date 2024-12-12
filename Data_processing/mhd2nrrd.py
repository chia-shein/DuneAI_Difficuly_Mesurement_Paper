import SimpleITK as sitk
import numpy as np
import os
import glob

input_dir = '/work/u5453836/LUNA_Data'
output_dir = '/work/u5453836/LUNA_Data_nrrd'
os.makedirs(output_dir, exist_ok=True)

for file_path in glob.glob(os.path.join(input_dir, '*.mhd')):
    input_image = sitk.ReadImage(file_path)
    image_array = sitk.GetArrayFromImage(input_image)

    # data.min() and data.max() constraint
    current_min = image_array.min()
    current_max = image_array.max()
    rescaled_array = (image_array - current_min) / (current_max - current_min) * (3071 + 1000) - 1000

    # data type constraint
    int16_array = rescaled_array.astype(np.int16)
    rescaled_image = sitk.GetImageFromArray(int16_array)
    rescaled_image.CopyInformation(input_image)
    
    file_name = os.path.basename(file_path).replace('.mhd', '.nrrd')
    output_file = os.path.join(output_dir, file_name)
    sitk.WriteImage(rescaled_image, output_file)

import os
import SimpleITK as sitk
input_dir = '/work/u5453836/LUNA_Data'
output_dir = '/work/u5453836/LUNA_Data_nrrd'
os.makedirs(output_dir, exist_ok=True)


for filename in os.listdir(input_dir):
    if filename.endswith('.mhd'):
        input_path = os.path.join(input_dir, filename)
        input_image = sitk.ReadImage(input_path)
        output_filename = os.path.splitext(filename)[0] + '.nrrd'
        output_path = os.path.join(output_dir, output_filename)
        sitk.WriteImage(input_image, output_path)
print("Conversion completed.")
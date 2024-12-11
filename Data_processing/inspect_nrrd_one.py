import nrrd
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = '/work/u5453836/LUNA_Data/1.3.6.1.4.1.14519.5.2.1.6279.6001.997611074084993415992563148335.nrrd'
data, header = nrrd.read(filename)

height, width, num_slices = data.shape
output_filename = 'output_video.mp4'

fps = 10
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
for slice_index in range(num_slices):
    slice_image = data[:, :, slice_index]
    slice_image = cv2.normalize(slice_image, None, 0, 255, cv2.NORM_MINMAX)
    slice_image = slice_image.astype(np.uint8)
    slice_image = cv2.cvtColor(slice_image, cv2.COLOR_GRAY2BGR)
    video_writer.write(slice_image)
video_writer.release()
print(f"The P4 file has been saved at: {output_filename}")
import nrrd
import cv2
import numpy as np

filenames = [
    '/home/u5453836/DuneAI/Software for qualitative assesment/test_data/pat1/image.nrrd',
    '/home/u5453836/DuneAI/Software for qualitative assesment/test_data/pat1/DR_mask.nrrd',
    '/home/u5453836/DuneAI/Software for qualitative assesment/test_data/pat1/DL_mask.nrrd'
]
data_list = [nrrd.read(filename)[0] for filename in filenames]

num_slices = data_list[0].shape[2]
assert all(data.shape[2] == num_slices for data in data_list), "All files must have the same number of slices."
height, width = data_list[0].shape[:2]
output_filename = 'combined_output_video.mp4'

fps = 10

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (height * 3, width))  # Note: swapped width and height
for slice_index in range(num_slices):
    slices = []
    for data in data_list:
        slice_image = data[:, :, slice_index]
        slice_image = cv2.normalize(slice_image, None, 0, 255, cv2.NORM_MINMAX)
        slice_image = slice_image.astype(np.uint8)
        slice_image = cv2.cvtColor(slice_image, cv2.COLOR_GRAY2BGR)
        slice_image = cv2.rotate(slice_image, cv2.ROTATE_90_CLOCKWISE)
        slices.append(slice_image)
    combined_slice = np.hstack(slices)
    video_writer.write(combined_slice)
video_writer.release()

print(f"The P4 file has been saved at: {output_filename}")

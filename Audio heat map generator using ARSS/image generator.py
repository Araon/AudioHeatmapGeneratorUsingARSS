import os
from PIL import Image
def audio_to_image():
#importing the sound files from the directory
	os.chdir("E:/Python stuff/arss")
	os.system("Start arss  sherlock.wav -q output.bmp --min-freq 55 -max 16000 --pps 100 -r 44100 -f 16 -b 12 ")

audio_to_image()


def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)
crop_areas = [(0, 0, 100, 100), (100, 0, 200, 100),(200, 0, 300, 100),(300, 0, 400, 100),(400, 0, 500, 100),(500, 0, 600, 100),(600, 0, 700, 100),(700, 0, 800, 100),(800, 0, 900, 100),(900, 0, 1000, 100),]

image_name = 'output.bmp'
img = Image.open(image_name)

# Loops through the "crop_areas" list and crops the image based on the coordinates in the list
for i, crop_area in enumerate(crop_areas):
    filename = os.path.splitext(image_name)[0]
    ext = os.path.splitext(image_name)[1]
    new_filename = filename + '_cropped' + str(i+1) + ext

    crop_image(img, crop_area, new_filename)

# Loops through the cropped images to determine each pixel values


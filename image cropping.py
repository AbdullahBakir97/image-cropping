import os
from PIL import Image

# crooping size
width = input('Enter Cropping width : ')
height = input('Enter Cropping height : ')


# open folder
os.chdir('images')


# putput folder
output_folder = input('Enter Folder Name : ')
os.makedirs(output_folder, exist_ok=True)


# loob over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.jpg','.jpeg')):
        im = image.open(image)
        width , height = im.size

        if width > height :
            height = int((fit_size/width)*height)
            width = fit_size
            
        else :
            width = int((fit_size/height)*width)
            height = fit_size
        
        im1 = im.resize(( width, height))
        im1.save(f"{output_folder}/{image}")




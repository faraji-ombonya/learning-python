import os
from sys import argv
from PIL import Image

path = argv[1]
destination = argv[2]
images = os.listdir(path)
os.mkdir(destination)

def convert(path, image, destination):
    '''
    convert image from jpg to png
    '''
    infile = f"{path}\{image}"
    outfile = f"{destination}\{image[:-4]}.png"
    img_jpg = Image.open(infile)
    img_jpg.save(outfile,"png")
    return None

for image in images:
    convert(path, image, destination)
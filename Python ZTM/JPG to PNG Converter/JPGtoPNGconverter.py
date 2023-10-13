import os
from sys import argv
from PIL import Image

path = argv[1]
destination = argv[2]

try:
    images = os.listdir(path)
except:
    print("Oops")
    print("Usage:   JPGtoPNGconverter.py path destination")
    exit()

try:
    os.mkdir(destination)
except FileExistsError:
    pass
except FileNotFoundError:
    print("Usage:   JPGtoPNGconverter.py path destination")
    print("Invalid path. Exiting program..")
    exit()
except:
    print("Ooops. Something went wrong.")
    exit()
    

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
    if image[-3:] != "jpg":
        continue
    convert(path, image, destination)
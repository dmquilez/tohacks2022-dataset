#!/usr/bin/python
from PIL import Image
import os, sys
#introducir fuente y destino
path = sys.argv[1]
path_dst = sys.argv[2]
dirs = os.listdir( path )
print(path.join("hola"))

def resize():
    for item in dirs:
        print(item)

        
        im = Image.open(path+"/"+item)
        f, e = os.path.splitext(path+"/"+item)
        imResize = im.resize((128,128), Image.ANTIALIAS)
        print(path_dst + "/" + ' resized.jpg')
        imResize.convert('RGB').save(path_dst + "/" + item +'resized.jpg', 
'JPEG', 
quality=90)
        print("conversion hecha")

resize()
print("hecho")

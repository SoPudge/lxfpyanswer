# -*- coding: utf-8 -*-
from PIL import Image
im = Image.open('a.jpg')
print(im.format,im.size,im.mode)

import numpy as np
import pandas as pd
import re
import pytesseract as pt
import cv2
import matplotlib.pyplot as plt
import os
from PIL import Image
from PIL.ExifTags import TAGS


def pan_num(path):
    im = Image.open(path)
    orientation = 1
    if orientation == 1:
        im

    if orientation == 3:
        im = im.rotate(180)

    if orientation == 6:
        im = im.rotate(270)

    if orientation == 8:
        im = im.rotate(90)

    im.save(path)

    text = pt.image_to_string(im, lang='eng')
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    num = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')

    if len(num.findall(text)) == 0:
        print("Blurry image mf!!!")
    else:
        print("Pan Card number = ", num.findall(text)[0])


path = os.path.abspath('')+'\\archive\\pan1.png'
pan_num(path)
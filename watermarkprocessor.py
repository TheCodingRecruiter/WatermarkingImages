# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import sys

try:
    watermarkimage = Image.open("C:\\Desktop\\Python Projects\\myimage.jpg")
except:
    print('Unable to load')
    sys.exit(1)

idraw = ImageDraw.Draw(watermarkimage)

text = 'TheCodingRecruiter'

font = ImageFont.truetype("arial.ttf", size=300)

idraw.text((10,10), text, font=font)

watermarkimage.save("C:\\Desktop\\Python Projects\\myimage_watermark.jpg")

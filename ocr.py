import easyocr
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

font_path = "C:/Windows/Fonts/NanumGothic.ttf"
font_size = 15

reader = easyocr.Reader(['ja', 'en'], gpu = True) #ja, ko, en
result = reader.readtext('hi.jpg')
img    = cv2.imread('hi.jpg')
img = Image.fromarray(img)

font = ImageFont.truetype(font_path, font_size)
draw = ImageDraw.Draw(img)
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(256, 3),dtype="uint8")

for i in result :
    x = i[0][0][0] 
    y = i[0][0][1] 
    w = i[0][1][0] - i[0][0][0] 
    h = i[0][2][1] - i[0][1][1]

    color_idx = random.randint(0,255)
    color = [int(c) for c in COLORS[color_idx]]

    draw.rectangle(((x, y), (x+w, y+h)), outline=tuple(color), width=2)
    draw.text((int((x + x + w) / 2) , y-2),str(i[1]), font=font, fill=tuple(color),)
    #draw.text((int((x + x + w) / 2) , y-2), str(i[1]).encode('utf-8'), font=font, fill=tuple(color),)
    print(f"{i[1]}",end="")

plt.figure(figsize=(50,50))
plt.imshow(img)
plt.show()

#!/usr/bin/env python
# coding: utf-8

# Uploaded by ElStickman; Used on Jupyter Computers

# In[1]:

!pip install pyqrcode 
!pip install pypng
!pip install Pillow

# in[2]
import pyqrcode
from PIL import Image
#Open background
img_bg = Image.open('background.png')
#Create QR
url = pyqrcode.QRCode('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#Save QR as png
url.png('New_QR.png', scale = 2)
#Open QR as a variable
img_qr = Image.open('New_QR.png')
#if we want to touch the corner this should be 0 then.
pixels_away_from_corner = 10
#Calculate position to place the qr acording to qr size and background size.
pos = (img_bg.size[0] - img_qr.size[0] - pixels_away_from_corner, img_bg.size[1] - img_qr.size[1] - pixels_away_from_corner)
#We create the png
img_bg.paste(img_qr, pos)
#We save the png
img_bg.save('export.png')


# In[3]:

from IPython.display import Image
#Open our new PNG
Image(filename='export.png') 


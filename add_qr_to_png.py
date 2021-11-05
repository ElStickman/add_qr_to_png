#!/usr/bin/env python
# coding: utf-8

# Uploaded by ElStickman; Used on Jupyter Computers

# In[1]:

#WE NEED 2 PNGS
import pyqrcode
from PIL import Image

img_bg = Image.open('BACKGROUND.png')

url = pyqrcode.QRCode('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
url.png('FRESH-QR.png', scale = 2)

img_qr = Image.open('FRESH-QR.png')

pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

img_bg.paste(img_qr, pos)
img_bg.save('export-2.png')


# In[2]:


from IPython.display import Image
Image(filename='export-2.png') 


# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:09:53 2019

@author: Aakriti
"""


from PIL import Image

img = Image.open("sample.jpg")

img.show()

#rotate
img_rotate = img.transpose(Image.ROTATE_90)

img_rotate.show()

img_rotate.save("sample1.jpg")
#crop
crop_im = img_rotate.crop(150,160)
img = Image.open("sample.jpg")

crop_im = img.crop(box=(340,20,160,204))

crop_im.save('crop_sample.jpg')
crop_im.show()
#thumbnail

img = Image.open("sample.jpg")
img.thumbnail((75,75))
print(img.width, img.height)
img.save('thumb_sample.jpg')



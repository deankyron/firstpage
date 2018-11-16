#
#prettyface.py
#
import matplotlib.pyplot as plt

from scipy import ndimage
from scipy import misc
# misc.face(gray=True)
face = image.open("E:\Google Drive\TC website\Trying stuff\images\kalgoorlie.JPG")
shifted_face = ndimage.shift(face, (50,50))
rotated_face = ndimage.rotate(face,30)
cropped_face = face[100:-100,100:-100]

plt.imshow(face)
plt.show()
plt.imshow(face, cmap=plt.cm.gray)
plt.show()
plt.imshow(shifted_face)
plt.show()
plt.imshow(rotated_face)
plt.show()
plt.imshow(cropped_face)
plt.show()



pixel_face = face[::10,::10]
pixel_face2 = face[::50,::50]
plt.imshow(pixel_face)
plt.show()
plt.imshow(pixel_face2)
plt.show()

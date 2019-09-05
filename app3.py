from PIL import Image, ImageFilter, ImageEnhance

img = Image.open('Images/new.jpg')
# img.show()
#Applying a filter to the image
img_sharpend = img.filter(ImageFilter.SHARPEN)
# img_sharpend2 = img_sharpend.filter(ImageFilter.SHARPEN)
img_sharpend.save('Images/new2.jpg' )
# exif_data = img._getexif()
# print exif_data
# enhancer = ImageEnhance.Sharpness(img)

# for i in range(8):
#     factor = i / 4.0
#     enhancer.enhance(factor).show()
   # enhancer.save('Images\pillow ' + str(factor) + '.jpg')
   # print('Images\pillow ' + str(factor) + '.jpg saved')
#img_sharpend.show()

# print img
# print img.size
# print img.format
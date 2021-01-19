from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')

print(img.size)
print(img.info)
print(img.format)

blurImg = img.filter(ImageFilter.BLUR)
greyImg = img.convert('L')
rotateImg = img.rotate(180)
resizeImg = img.resize((300, 300))

# cropping image
box = (100, 100, 400, 400)
croppedImg = img.crop(box)

blurImg.save("blur_pickachu.png", 'png')
greyImg.save("grey_pickachu.png", 'png')
croppedImg.save("cropped_pickachu.png", 'png')
croppedImg.show()
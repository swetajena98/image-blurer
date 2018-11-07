from PIL import Image, ImageFilter
image = Image.open('/home/bablee/Downloads/pexels-photo-257840.jpeg')
image.show()
cropped_image = image.crop((223,78,480,321))
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=20))
image.paste(blurred_image,(223,78,480,321))
image.show()

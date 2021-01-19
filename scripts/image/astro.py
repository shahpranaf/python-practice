from PIL import Image

astro_img = Image.open("./astro.jpg")
print(astro_img.size)

# resize without loosing aspect ratio
astro_img.thumbnail((400, 400)) # Please note we have to pass tuple

astro_img.save("astro_thumb.jpg")
print(astro_img.size)
from turtle import width
from PIL import Image

image_principal = Image.open("beach.jpg")
image_background = Image.open("cactus.jpg")
image_new = Image.new("RGB", image_principal.size)

width, height = image_principal.size

pixels_principal = image_principal.load()
pixels_background = image_background.load()
pixels_new = image_new.load()

r, g, b = pixels_principal[225, 225, 225]
print(r, g, b)

for x in range(1, 800):
    for y in range(1, 600):
        r,g,b = pixels_principal[x,y]
        
        if r < 160 and g > 220 and b < 160:
            pixels_new[x,y] = pixels_background[x,y]
            
        else: 
            pixels_new[x,y] = pixels_background[x,y]
            
image_new.show()
image_new.save("photo.jpg")

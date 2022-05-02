from turtle import width
from PIL import Image
#print("Import worked successfully")

image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")

print(image_beach.size)
print(image_beach.format)

image_combined = Image.new("image_cactus", "image_beach")

(width, height) = image_beach.size

print(f"Width: {width}")
print(f"Height: {height}")
      


pixels_beach = image_beach.load()

print(pixels_beach[200,100]) #Red/Green/Blue - RGB

#pixels_beach[200,100] = (255, 0, 255)

for y in range(100, 500):
    for x in range(0, 300):
        #pixels_beach[x , 100] = (255,0,255)
        (r, g, b) = pixels_beach[x, y]
        
        pixels_beach[x, y] = (r, g, 255)
        
        
        #pixels_beach[x, y] = (255,0,255)

image_combined.show()

image_beach.save("beach_blue_square.jpg")
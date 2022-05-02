from PIL import Image

img1 = Image.open(r"beach.jpg")
img2 = Image.open(r"cactus.jpg")

img1.paste(img2, (400,300))

img1.show()
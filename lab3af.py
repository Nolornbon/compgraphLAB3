from PIL import Image, ImageDraw
import math 
image = Image.new('RGBA', (960, 960), (255, 255, 255))
angle = math.radians(50)
draw = ImageDraw.Draw(image)

with open("D:\datasets\DS1.txt", "r") as file:
    for line in file:
        dotslist = line.split()
        i = int(dotslist[0]) - 480
        j = int(dotslist[1]) - 480
        x = math.cos(angle) * i - math.sin(angle) * j
        y = math.sin(angle) * i + math.cos(angle) * j
        draw.line((x+480, y+480, x+481, y+481),
            fill = (200, 190, 255))

image.show()
image.save('datasetf.png')


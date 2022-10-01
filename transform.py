# use this simple script to
# modify the image resources from
# https://www.gnome-look.org/p/1805336

from PIL import Image
import os

path = __file__.split("/")
path = path[:len(path) - 1]
path.append("voidx")
dr = "/".join(path)

files = os.listdir(dr)

tg = []
for i in files:
    if "animation" in i or "progress" in i:
        tg.append(i)

pro = Image.open("prototype.png")
box = (0, 0, 264, 168)

# test = Image.open("animation-test.png")
region = pro.crop(box)

# test.paste(region, box)
# test.show()

for i in tg:
    im = Image.open(i)
    im.paste(region, box)
    im.save(i)


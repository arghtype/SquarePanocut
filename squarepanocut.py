import sys
from PIL import Image

if (len(sys.argv) != 2 and len(sys.argv) != 3):
    print("SquarePanocut allows to cut panorama into squares. This is helpful for creating Instagram swipeable posts. \n\nUsage: \n python3 squarepanocut.py panorama.jpg\n python3 squarepanocut.py panorama.jpg left|right|center \nLast parameter defines which part of original panorama will be covered by resulting parts. Default value is 'left'. Total loss will be less than 1 image height.")
    exit()

filename = sys.argv[1]
print("Working with " + filename)

image  = Image.open(filename)
width, height = image.size

offset = 0

if (len(sys.argv) == 3):
    mode = sys.argv[2]
    if ("left" == mode):
        offset = 0
    else:
        reminder = width
        while reminder >= height:
            reminder -= height
        if ("right" == mode):
            offset = reminder
        if ("center" == mode):
            offset = reminder // 2

count = width // height
i = 0

while i < count:
    left = offset + i * height
    top = 0
    right = offset + height + i * height
    low = height
    print("Cropping Part " + str(i) + ":   " +str(left) + ", " +str(top) + ", " +str(right) + ", " + str(low))
    area = (left, top, right, low)
    part = image.crop(area)
    part.save("part" + str(i) + ".jpg", quality = 100)
    i += 1
print("Success!")

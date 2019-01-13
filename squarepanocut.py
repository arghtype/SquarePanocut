import sys
from PIL import Image

args_length = len(sys.argv)
if 2 > args_length > 4:
    print("SquarePanocut allows to cut panorama into 1x1 squares or 4x5 portraits. "
          "\n\nUsage: "
          "\n python3 squarepanocut.py panorama.jpg"
          "\n python3 squarepanocut.py panorama.jpg left|right|center"
          "\n python3 squarepanocut.py panorama.jpg left|right|center p")
    exit()

filename = sys.argv[1]
image = Image.open(filename)
width, height = image.size
step = height
offset = 0

if args_length == 4:
    step = step * 4 // 5
if args_length >= 3:
    mode = sys.argv[2]
    if "left" == mode:
        offset = 0
    else:
        reminder = width
        while reminder >= step:
            reminder -= step
        if "right" == mode:
            offset = reminder
        if "center" == mode:
            offset = reminder // 2
count = width // step
i = 0

print("Working with " + filename + " of size " + str(width) + "x" + str(height))
print("Slicing into " + str(count) + " parts of size " + str(step) + "x" + str(height))

while i < count:
    left = offset + i * step
    top = 0
    right = offset + step + i * step
    low = height
    output_name = "part" + str(i) + ".jpg"
    print("Part " + str(i) + ":\t" +str(left) + ",\t" +str(top) + ",\t" +str(right) + ",\t" + str(low) + "\t> " + output_name)
    area = (left, top, right, low)
    part = image.crop(area)
    part.save(output_name, quality=100)
    i += 1
print("Success!")
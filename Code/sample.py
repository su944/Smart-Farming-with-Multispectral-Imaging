from PIL import Image
from PIL.TiffTags import TAGS

img =  Image.open('/Users/sunnygali/Documents/Acads/projects/ProjectCourse/dataset 2/05.01.2024/IMG_240105_090523_0016_GRE.TIF')
# print(img.save("/Users/sunnygali/Documents/1.jpeg"))

exif = {}
print(type(img))
exifdata =  img.getexif().items()
for tag, value in exifdata:
    for tag in TAGS:
        exif[TAGS[tag]] = value


print(exif)
print(img.__dir__())
print(img.info)
print(img.tag)
print()





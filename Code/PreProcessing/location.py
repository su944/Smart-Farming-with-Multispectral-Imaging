from pprint import pprint
from PIL import Image
import piexif

codec = 'ISO-8859-1'  # or latin-1

def exif_to_tag(exif_dict):
    exif_tag_dict = {}
    thumbnail = exif_dict.pop('thumbnail')
    exif_tag_dict['thumbnail'] = thumbnail.decode(codec)

    for ifd in exif_dict:
        exif_tag_dict[ifd] = {}
        for tag in exif_dict[ifd]:
            try:
                element = exif_dict[ifd][tag].decode(codec)

            except AttributeError:
                element = exif_dict[ifd][tag]

            exif_tag_dict[ifd][piexif.TAGS[ifd][tag]["name"]] = element

    return exif_tag_dict

def main():
    filename = '/Users/sunnygali/Documents/Acads/projects/ProjectCourse/dataset 2/05.01.2024/IMG_240105_090523_0016_GRE.TIF'  # obviously one of your own pictures
    im = Image.open(filename)

    exif_dict = piexif.load(im.info.get('exif'))
    exif_dict = exif_to_tag(exif_dict)

    pprint(exif_dict['GPS'])

if __name__ == '__main__':
   main()
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def NDVI(img1, img2):
    #change the datatype of the image to float
    num = img1 - img2
    Den = img1 + img2 + 0.0000001
    NDVI = np.divide(num,Den)
    return NDVI


def read_tiff_to_numpy(path):
    img = cv2.imread(path,0).astype('float')
    return img

# Paths to the NIR and RED TIFF images
path1 = "/Users/sunnygali/Documents/Acads/projects/ProjectCourse/dataset 2/05.01.2024/IMG_240105_090524_0017_NIR.TIF"
path2 = "/Users/sunnygali/Documents/Acads/projects/ProjectCourse/dataset 2/05.01.2024/IMG_240105_090524_0017_RED.TIF"


# Read TIFF images into NumPy arrays
nir_img = read_tiff_to_numpy(path1)
red_img = read_tiff_to_numpy(path2)

# Calculate NDVI
ndvi = NDVI(nir_img, red_img)
color_map =  mcolors.LinearSegmentedColormap.from_list('ndvi', ['#926829', 'white', 'green'])
plt.imshow(ndvi,cmap=color_map,vmin=-1, vmax=1)
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.colorbar()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()








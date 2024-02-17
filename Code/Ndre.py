import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import matplotlib.colors as mcolors


def NDRE(img1, img2):
    # change the datatype of the image to float
    num = img1 - img2
    Den = img1 + img2 + 0.0000001
    NDVI = np.divide(num, Den)
    return NDVI


def read_image(path):
    img = cv2.imread(path, 0).astype('float')
    return img




metric  = "ndre"
img1  = "NIR"
img2 =  "REG"
data = "05.01.2024"
directory = f"/Users/sunnygali/Documents/Acads/projects/ProjectCourse/preprocessed_images/{data}"

dirs = os.listdir(directory)
if '.DS_Store' in dirs:
    dirs.remove('.DS_Store')
print(len(dirs))
os.makedirs(f'/Users/sunnygali/Documents/Acads/projects/ProjectCourse/{metric}_images/{data}', exist_ok=True)
for dir in dirs:
    path1 = directory + '/' + dir + '/' + dir + f'_{img1}.TIF'
    path2 = directory + '/' + dir + '/' + dir + f'_{img2}.TIF'
    print(path1)
    print(path2)
    nir_img = read_image(path1)
    red_img = read_image(path2)
    ndre = np.array(NDRE(nir_img, red_img))
    color_map = mcolors.LinearSegmentedColormap.from_list('ndre', ['#926829', 'white', '#00FF00'])
    plt.figure()
    plt.imshow(ndre, cmap=color_map, vmin=-1, vmax=1)
    plt.colorbar()
    plt.title('Normalized Difference Red Edge Index (NDRE)')
    plt.savefig(f'/Users/sunnygali/Documents/Acads/projects/ProjectCourse/{metric}_images/{data}/' + dir + '_NDRE.png')
    plt.close()

print('NDRE images saved')



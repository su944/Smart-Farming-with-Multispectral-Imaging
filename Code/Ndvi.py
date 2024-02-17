import numpy as np
import os
import matplotlib.pyplot as plt
import cv2 
import matplotlib.colors as mcolors


def NDVI(img1, img2):
    #change the datatype of the image to float
    num = img1 - img2
    Den = img1 + img2 + 0.0000001
    NDVI = np.divide(num,Den)
    return NDVI

def read_image(path):
    img = cv2.imread(path,0).astype('float')
    return img



directory =  "/Users/sunnygali/Documents/Acads/projects/ProjectCourse/preprocessed_images/11.12.2023"

dirs  = os.listdir(directory)
if '.DS_Store' in dirs:
    dirs.remove('.DS_Store')
print(len(dirs))
os.makedirs('/Users/sunnygali/Documents/Acads/projects/ProjectCourse/ndvi_images/11.12.2023',exist_ok=True)
for dir in dirs:
    path1 = directory+'/'+dir+'/'+dir+'_NIR.TIF'
    path2 = directory+'/'+dir+'/'+dir+'_RED.TIF'
    print(path1)
    print(path2)
    nir_img = read_image(path1)
    red_img = read_image(path2)
    ndvi = np.array(NDVI(nir_img, red_img))
    color_map =  mcolors.LinearSegmentedColormap.from_list('ndvi', ['#926829', 'white', '#00FF00'])
    plt.figure()
    plt.imshow(ndvi,cmap=color_map,vmin=-1, vmax=1)
    plt.colorbar()
    plt.title('Normalized Difference Vegetation Index (NDVI)')
    plt.savefig('/Users/sunnygali/Documents/Acads/projects/ProjectCourse/ndvi_images/11.12.2023/'+dir+'_NDVI.png')
    plt.close()
   
print('NDVI images saved')
    
    

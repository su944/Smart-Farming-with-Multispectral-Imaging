
import os 
import numpy as np
import cv2
import shutil

def  preprocess_images(source,destination):
    os.makedirs(destination,exist_ok=True)
    images = os.listdir(source)
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    images = [i[:-8] for i in images]
    print(len(images))
    print(len(set(images)))
    x = set(images)
    img_types = ["NIR.TIF","RED.TIF","REG.TIF","GRE.TIF"]
    for img in x:
        os.makedirs(destination+'/'+img,exist_ok=True)
        for im_typ in img_types:
            try:
                shutil.copy2(source+'/'+img+'_'+im_typ,destination+'/'+img+'/'+img+'_'+im_typ)
            except shutil.SameFileError:
                 print('File already exists')
            except FileNotFoundError:
                print('File not found')
            except Exception as e:
                print(e)   
    print('Preprocessing done')
preprocess_images('/Users/sunnygali/Documents/Acads/projects/ProjectCourse/dataset 2/11.12.2023','/Users/sunnygali/Documents/Acads/projects/ProjectCourse/preprocessed_images/11.12.2023')
        
       
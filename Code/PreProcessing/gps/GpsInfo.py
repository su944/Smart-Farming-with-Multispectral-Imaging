import os

from PIL import Image, ExifTags
import pandas as pd




def get_gps_data(gps_info,tag):
    try:
        return gps_info[tag]
    except (KeyError, TypeError):
        print("No GPS data")
        return "-------"



# List to store data
data = []

# List of image file paths
image_path = "/dataset 2/11.12.2023"
gps_data = []
directory = os.listdir(image_path)

gps_csv_file_name = 'gps_data_11.12.2023.csv'
for image in directory:
    
        #check if the file is an image
        
    if image.endswith('.TIF'):
        img = Image.open(image_path + '/' + image)
        exifdata = img.getexif()
        gps_info = exifdata.get_ifd(ExifTags.IFD.GPSInfo)
        # Extract and print GPS information
        
        latitude_ref = get_gps_data(gps_info,1)
        latitude = '.'.join(str(coord) for coord in get_gps_data(gps_info,2))
        longitude_ref = get_gps_data(gps_info,3)
        longitude = '.'.join(str(coord) for coord in get_gps_data(gps_info,4))
        #add the data to the list
        #also store the image name 
        gps_data.append([image,latitude_ref,latitude,longitude_ref,longitude])#store the data in a csv file
df = pd.DataFrame(gps_data, columns = ['Image Name','Latitude Ref','Latitude','Longitude Ref','Longitude'])
df.to_csv("/Users/sunnygali/Documents/Acads/projects/ProjectCourse/GPS_INFO/"+gps_csv_file_name, index=True,header=True)


        
           
            
            
            
            
         
         

import pandas as pd

# Load the two CSV files into DataFrames
df1 = pd.read_csv('/GPS_INFO/gps_data_05.01.2024.csv')  # Replace 'csv1.csv' with the actual filename of the first CSV file
df2 = pd.read_csv('/GPS_INFO/gps_data_11.12.2023.csv')  # Replace 'csv2.csv' with the actual filename of the second CSV file

# Merge the DataFrames based on latitude and longitude columns
merged_df = pd.merge(df1, df2, on=['Latitude', 'Longitude'], how='inner')

# Print the image names where latitude and longitude match
print("Images with matching latitude and longitude:")
print("Matching images with lattidue and longitude: "+str(merged_df.size))
 # Assuming 'Image Path' is the column name for image names in both CSVs

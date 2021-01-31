## imports 
from dateutil.parser import parse
import os 
import pprint
import pandas as pd

## get list of images to process

current_dir = os.getcwd()

image_dir = 'images-jan-2021'
image_dir_path = os.path.join(current_dir,image_dir)

image_names = os.listdir(image_dir_path)

data_dict = {}
final = {}

for image_name in image_names:

    current_image_name = os.path.basename(image_name)
    name_blob_list = current_image_name.split('_')

    if len(name_blob_list) == 4:
        date_day = ' '.join(name_blob_list[:2])

        data_dict[date_day] = {}

for image_name in image_names:

    current_image_name = os.path.basename(image_name)
    name_blob_list = current_image_name.split('_')

    if len(name_blob_list) == 4:

        date_day = ' '.join(name_blob_list[:2])

        time = name_blob_list[2]
        amount = name_blob_list[3].split(".")[0]
 
        data_dict[date_day][time] = amount
            
        
# for entry in data_dict:
#     print("Before: ", data_dict[entry])
#     print(data_dict[entry].sort(key = lambda x:x, reverse=False))

# pprint.pprint(data_dict)

data_frame = pd.DataFrame.from_dict(data_dict, orient='index').to_csv(image_dir+'.csv')
# print(data_frame.columns)
# print(data_frame.head())




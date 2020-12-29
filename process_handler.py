## imports 
import os 
import cv2

# try:
#     from PIL import Image
# except ImportError:
#     import Image

import pytesseract
import pprint


## get list of images to process

current_dir = os.getcwd()
# print('\nList of Folders in Script Directory: \n----------------------------------')
# pprint.pprint(os.listdir(current_dir))

# image_dir = input('\nPaste name of folder containing images: ')
image_dir = 'images-nov-2020'
image_dir_path = os.path.join(current_dir,image_dir)
# pprint.pprint(os.listdir(image_dir_path))
image_names = os.listdir(image_dir_path)

image_paths_list = [  os.path.join(image_dir_path,image_name) for image_name in image_names] 
# pprint.pprint(image_paths_list)

## create function to handle each file 
def image_to_data(image_path):

    image_file_name = os.path.basename(image_path)
    image_file_extension = os.path.splitext(image_path)[1]

    image_cv = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

    ## check file extension
    if image_file_extension == '.png' or image_file_extension == '.jpg':

        image_string = pytesseract.image_to_string(image_rgb)

        image_string_list = image_string.split('\n')

        ## parse date 
        image_date_raw = image_string_list[0]


        ## parse amount 
        for line in image_string_list:
            if line.find('Total Bill') != -1:
                image_price_raw = line

        return image_file_name,image_date_raw,image_price_raw

pprint.pprint( [ (index,image_to_data(image_path)) for index, image_path in enumerate(image_paths_list) ] )
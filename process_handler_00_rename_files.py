## imports 
import os 
import cv2

import pytesseract
import pprint

import re

## get list of images to process

current_dir = os.getcwd()

image_dir = 'images-jan-2021'
image_dir_path = os.path.join(current_dir,image_dir)

image_names = os.listdir(image_dir_path)
image_paths_list = [  os.path.join(image_dir_path,image_name) for image_name in image_names] 


## create function to handle each file 
def image_to_data(image_path):

    image_file_name = os.path.basename(image_path)
    image_file_extension = os.path.splitext(image_path)[1]

    ## check file extension
    if image_file_extension == '.png' or image_file_extension == '.jpg':

        # load and preprocess image
        image_cv = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        image_thresholding = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        # convert image to string
        image_string = pytesseract.image_to_string(image_thresholding)

        # list of lines in string 
        image_string_list = image_string.split('\n')

        ## parse date 
        image_date_raw = image_string_list[0]
        image_date_regex_list = "".join(re.findall('[A-Za-z0-9,]',image_date_raw)).split(',')

        if len(image_date_regex_list) == 3:

            if image_date_regex_list[2].endswith('AM'):
                image_date_time = 'Morning'
            elif image_date_regex_list[2].endswith('PM'):
                image_date_time = 'Night'

            image_date = '_'.join([ image_date_regex_list[1].strip(),image_date_regex_list[0].strip(),image_date_time ])

        else:
            image_date = '_'.join(image_date_regex_list)


        ## parse amount 
        for line in image_string_list:
            if line.find('Total Bill') != -1:
                image_price_regex = "".join(re.findall('[0-9]',line))

                try:
                    if int(image_price_regex) > 150:
                        image_price = '_<--->'
                    else:
                        image_price = '_'+ image_price_regex
                except ValueError:
                    image_price = '_<--->'

        ## rename file
        current_image_file_name = os.path.join(image_dir_path,image_file_name)
        new_file_name = os.path.join(image_dir_path,image_date + image_price + image_file_extension)
        # print('\nold: ',os.path.basename(current_image_file_name),'\nnew: ',os.path.basename(new_file_name))
        os.rename(current_image_file_name,new_file_name)

        # final function return
        return image_file_name,image_date,image_price

# apply function to all images in folder
pprint.pprint( [ (index,image_to_data(image_path)) for index, image_path in enumerate(image_paths_list) ] )
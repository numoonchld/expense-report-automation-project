## imports 
from dateutil.parser import parse
import os 
import pprint

## get list of images to process

current_dir = os.getcwd()

image_dir = 'images-dec-2020'
image_dir_path = os.path.join(current_dir,image_dir)

image_names = os.listdir(image_dir_path)

pprint.pprint(image_names)
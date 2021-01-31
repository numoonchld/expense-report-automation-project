# OCR for daily travel expense report generation 

- there are two scripts 
    - `process_handler_00_rename_files.py`: image file renamer
        - renames the image file according to the date, time-of-day and fare in the image


    - `process_handler_01_create_csv.py`: image file name to csv 
        - extracts the information in the file names into a csv 

- after running the first script, ensure image file names do not have `<--->` in their file names, by filling in the appropriate details
- after running the second script, open the `.csv.` file output at the end of it, and sort by the first column
    - rearrange the night and morning columns as necessary to match the final document

### step 1

- collect all the screenshots from `OLA App > My Rides` for the month in a directory within the root directory 
- name the directory containing the images in the following pattern 
    - `images-[month-name]-[year]`
    - this name will be used in **step 2** and **step 4**


### step 2

- in file `process_handler_00_rename_files.py`, set the `image_dir` variable to the above directory name 

- run `python process_handler_00_rename_files.py`

- this will rename the image files with the date, day, time-of-day and fare in the filename

- zip this folder and put it up on google drive 

### step 3 

- manual cleanup
    - not all files will be renamed correctly

- file names that need attention will have `<--->` in the file name 
    - open the image file and rename it with the correct details by observing the details from the image

### step 4

- in file `process_handler_01_create_csv.py`, set the `image_dir` variable to the same above directory name 

- run `python process_handler_01_create_csv.py`

- open the `.csv` file generated using a spreadsheet editor and sort the sheet by the first column, which has the date and day 
    - rearrange the `night` and `morning` columns to match the final report template 

## Troubleshooting

- `pip install -r requirements.txt`
    - installs the requirements in the virtual environment

- if this install fails with `Errno 13`:
    - delete the `bin` and the `lib` folder and recreate a virtual environment 
    - then run `pip install -r requirements.txt`

- if it still complains, upgrade `pip` and then install from requirements
    - `pip install --upgrade pip`
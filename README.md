# et3-tasks
A solution to the problems given for the tasks in the technical challenge (NOTE: the code for all the problems is in the et3Test.ipynb notebook where I ran and tested the code many times) 

# Regarding the problem 2.1 (copy_all_images.py):
## How it works
Run the python file and type the source_folder input path and the destination_folder output path as instructed in the terminal.
## Work approach 
I used the functionalities of the os libirary in python to get all the images in the folders and sub-folders, then grouped them into a variable, then copied all the images paths using shutil library


# Regarding the problem 2.2 (rename_images.py):
## How it works
Run the python file and type the image_folder input path as instructed in the terminal.
## Work approach 
I used the functionalities of the os libirary in python to list all the files in the specified directory, then I splitted their names and renamed them. 
One problem was that most of the images names were similar so I initiated a counter to be added before each image name to prevent the fileAlreadyExists error.


# Regarding the problem 2.3 (get_images_info.py):
## How it works
Run the python file and type the image_folder input path, the csv_file output path, and the destination_folder output path as instructed in the terminal.
## Work approach 
I used the functionalities of the os libirary in python especially (os.path) to get all the images information for each image in the directory, then using csv library, I saved all the results in a csv file that the user specifies at first. Also, I copied all the images in a new folder that the user specifies as requested in the pdf, Although, I Found that redundant but I followed this instruction from the pdf file (Output: extracted images to one folder, a csv file (report) that specify the following:...)


# Regarding the problem 3 (convert_annotations.py):
## How it works
Run the python file and type the yolo_annot_file input path and the json_out_file output path as instructed in the terminal.
## Work approach 
I used the functionalities of the os and json libiraries in python to read the text file and split each value in each line and to dump the resulted data in a json file.
One problem was I didn't have the image's width and height which it was critical to be able to convert the annotations format from yolo to COCO/json, but I found that the widths and heights in the image1.json file was multiplied by a 100 so with this information I was able to know the width and height of the whole image then I calculated x, y, width, and height values as the following formulas:
1- COCO_w = image_width * yolo_width
2- COCO_h = image_height * yolo_height
3- COCO_x = (yolo_x * image_width) - (COCO_w / 2)
4- COCO_y = (yolo_y * image_height) - (COCO_h / 2)
Then I rounded them, and made sure that the json file was the same format as the provided image1.json file.
Second problem was because of the same reason as the first problem and it resulted in copying the same image path into the "data" key value.

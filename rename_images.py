## Problem 2.2 solution

import os
from tqdm import tqdm

def rename_images(image_folder):
    
    """
    args*:
    image_folder: The path for the input dataset folder
    
    """

    # Initializing a counter to add to the images names because the images had similar names  
    counter = 1
    
    # Checking if the input folder is correct
    if not os.path.isdir(image_folder):
        print("Please provide the correct path for the input folder")
    else:

        # Looping through each image in the directory 
        for file in tqdm(os.listdir(image_folder)):
            # Get the full path for the images
            old_Name = os.path.join(image_folder, file)

            # Get the full directory path 
            dir_Name = os.path.dirname(old_Name)

            # Add the counter to each image name while splitting its prefix
            modified_name = '{}_'.format(counter) + file.split('-')[-1]

            # Get the full path for the files after name modification
            new_Name = os.path.join(dirName, modified_name)

            # Rename the old images names with the new one 
            os.rename(old_Name, new_Name)

            # Increment the counter to avoid similarity 
            counter += 1

#### example input #### 

# image_folder = D:\et3\images_dataset

if __name__ == "__main__":

    rename_images(image_folder=str(input("please provide the path for the image dataset folder: ")))
    print("Done Processing")
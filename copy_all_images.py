## Problem 2.1 solution

import os
import shutil
from tqdm import tqdm

def copy_all_images(source_folder, destination_folder):
    
    """
    args*:
    source_folder: The path for the input dataset source folder
    destination_folder: The path for the extracted images new folder
    
    """
    
    # Checking if the input folder is correct
    if not os.path.isdir(source_folder):
        print("Please provide the correct path for the input folder")
    else:

        # Create a destination folder if doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # Loop through all the files in source folder using os.walk
        for root, dirs, files in tqdm(os.walk(source_folder)):

            for file in files:

                # Check if the file is an image
                if file.lower().endswith((".jpg", ".jpeg", ".png")):

                    # Get the full path of the source file
                    source_file = os.path.join(root, file)

                    # Copy the file to the destination folder
                    shutil.copy(source_file, destination_folder)

                    
#### example inputs #### 

# source_folder = D:/et3/problem1/dairies
# destination_folder = D:/et3/images_dataset

if __name__ == "__main__":

    copy_all_images(source_folder=str(input("please provide the path for the image dataset source folder: "))
                    , destination_folder=str(input("please provide the path for the extracted images output folder: ")))
    print("Done Processing")
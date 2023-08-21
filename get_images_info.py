## Problem 2.3 solution

import os
from pathlib import Path
import csv
import datetime
from tqdm import tqdm

def get_images_info(image_folder, csv_file, destination_folder):

    """
    args*:
    image_folder: The path for the input dataset folder
    csv_file: The path for the output csv file
    destination_folder: The path for the extracted images new folder
    
    """
    
    # Checking if the input folder is correct
    if not os.path.isdir(image_folder):
        print("Please provide the correct path for the input folder")
    else:

        # Checking if the folder exists and if not then make one
        os.makedirs(destination_folder, exist_ok=True)

        # Checking if the CSV file exists and if not then make one
        filepath1 = Path(csv_file)
        filepath1.parent.mkdir(parents=True, exist_ok=True)

        # Open the CSV file in write mode
        with open(filepath1, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Image", "Image Size", "Image Modification data"])

            # Loop through all the files in the image folder
            for file in tqdm(os.listdir(image_folder)):

                # Get the full path of the file
                file_path = os.path.join(image_folder, file)

                # Check if the file is an image
                if file.lower().endswith((".jpg", ".jpeg", ".png")):
                    # Get the file size
                    file_size = round(os.path.getsize(file_path) * 0.001, 2) 
                    file_size = str(file_size) + ' MB'

                    # Get the date of last image content modification
                    modification_time = os.path.getmtime(file_path)
                    modification_date = datetime.datetime.fromtimestamp(modification_time)

                    # Write the image details to the CSV file
                    writer.writerow([file, file_size, modification_date])

                    # Copy the extracted files to the destination folder as required in the pdf
                    shutil.copy(file_path, destination_folder)


#### example inputs ####                

# image_folder = D:/et3/images_dataset
# csv_file = D:/et3/images_dataset2/output.csv
# destination_folder = D:/et3/images_dataset2

if __name__ == "__main__":

    get_images_info(image_folder=str(input("please provide the path for the image dataset folder: "))
                    , csv_file=str(input("please provide the path for the result csv file with .csv extension: "))
                    , destination_folder=str(input("please provide the path for the extracted images output folder: ")))
    print("Done Processing")

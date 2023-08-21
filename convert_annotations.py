## Problem 3 solution

import json
import os
from tqdm import tqdm


def convert_yolo_to_json(yolo_annot_file, json_out_file):

    """
    args*:
    yolo_annot_file: The path for the input text file
    json_out_file: The path for the output json file 
    
    """
    
    if not os.path.isfile(yolo_annot_file):
        print("Please provide the correct path for the input file")
    else:


        # Read the text file
        with open(yolo_annot_file, 'r') as file:
            lines = file.readlines()

        result = []

        # specifying image width and height depending on the result of the json file "w" and "h" that were multiplied by 100
        imgWidth, imgHeight = 100, 100

        # Process each line in the text file

        for line in tqdm(lines):
            data = line.strip().split(' ')
            obj = data[0]
            x = round((float(data[1]) * imgWidth) - (float(data[3]) * imgWidth / 2), 6) 
            y = round((float(data[2]) * imgHeight) - (float(data[4]) * imgHeight / 2), 6) 
            width = round(float(data[3]) * imgWidth, 6)
            height = round(float(data[4]) * imgHeight, 6)

            annotation = {
                        "image_rotation": 0,
                        "value": {
                            "x": x,
                            "y": y,
                            "width": width,
                            "height": height,
                            "rotation": 0,
                            "rectanglelabels": [
                                "object"
                            ]
                        }
                    }



            result.append(annotation)

        # Create the JSON object
        annotations = {"result": result}

        # providing the data parameter as a default because I did not have the original image
        data = {"image": "\/data\/upload\/image1.jpg"}

        json_data = {"annotations": [annotations], "data": data}

        # Write the JSON data to a file specified 
        with open(json_out_file, 'w') as file:
            json.dump(json_data, file, indent=4)

        
##### example input #####

# yolo_annot_file = D:/et3/problem2/image1.txt
# json_out_file = D:/et3/problem2/output.json

if __name__ == "__main__":

    convert_yolo_to_json(yolo_annot_file=str(input("please provide the path for annotation.txt input file: "))
                        , json_out_file=str(input("please provide the path for annotation.json output file: ")))
    print("Done Processing")

import json
import os
import csv
import ast

# reformat data for given filename to appropriate format
from_filename = "dc_power_csv.csv"
to_filename = "dc power_images.csv"


def writeCSV(filename, data):
    print(filename)
    print(data)

    if os.path.isfile(filename):
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    else:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)


row_count = 0
with open(from_filename, 'r+') as f:
    reader = csv.reader(f)
    for row in reader:
        # row is a list of strings
        # use string.join to put them together
        # ['filename', 'file_size', 'file_attributes', 'region_count', 'region_id', 'region_shape_attributes', 'region_attributes']
        # ['filename', 'starting x-coord', 'starting y-coord', 'ending x-coord', 'ending y-coord', 'class label']

        # ignores header
        if row_count > 0 and row[5] != "{}":
            image_filename = row[0]

            region_info = ast.literal_eval(row[5])
            region_type = region_info["name"]

            class_type = row[6][1:-1].split(",")[0].split(":")[1][1:-1].strip().strip('\\n')

            # determine what type of region
            if region_type == "circle":
                cx = region_info["cx"]
                cy = region_info["cy"]
                r = region_info["r"]

                x = int(cx) - r
                y = int(cy) - r
                x1 = x + r
                x2 = y + r

                writeCSV(str(class_type+"_images.csv"), [image_filename, x, y, x1, x2, class_type])
            elif region_type == "rect":
                print(region_info)
                x = region_info["x"]
                y = region_info["y"]
                x1 = x+region_info["width"]
                y1 = y+region_info["height"]

                writeCSV(str(class_type+"_images.csv"), [image_filename, x, y, x1, y1, class_type])
        row_count += 1

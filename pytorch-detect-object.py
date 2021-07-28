import os
import random

# weight locations
weights = "pth_models/Yolov4_epoch50.pth"
test_dir = "roboflow/test/_classes.txt"

# grab a random image from test dataset
test_images = [f for f in os.listdir('roboflow/test') if f.endswith('.jpg')]

img_path = "roboflow/test/" + random.choice(test_images);
print(img_path)

# run our model with the weights
print("python pytorch-YOLOv4/models.py 4 " + weights + " " + img_path + " " + test_dir)
os.system("python pytorch-YOLOv4/models.py 4 " + weights + " " + img_path + " " + test_dir)
# visualize inference

# from IPython.display import Image/

# Image('predictions.jpg')

from imageai.Detection.Custom import CustomObjectDetection
import os

model_name = "ports/models/detection_model-ex-012--loss-0009.301.h5"
execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, model_name))
detector.setJsonPath(os.path.join(execution_path, "ports/json/detection_config.json"))
detector.loadModel()

filepath = "dataset/images/test/"
filename = "files.txt"

# read list of files
imagePaths = open(filepath + filename).read().strip().split("\n")

for imagePath in imagePaths:
    test_img = imagePath
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, filepath + test_img),
                                                 output_image_path=os.path.join(execution_path,
                                                filepath+"/result/" + test_img),
                                                 minimum_percentage_probability=50)
    print(imagePath)
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

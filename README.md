# SatelliteSim
Neural networks to localize satellites and port components.

## File Structures
### CubeSat
* Contains 3d models of 1U CubeSat
* Contains fbx files for Unreal Engine 4 mesh
### dataset
* Contains the dataset for R-CNN Satellite object detection
### Pannel
* Contains files necessary for YOLOv3 training and detection
* dataset will contain the annotations and images
### pth_models
* Stores all the pth models for YOLOv4 PyTorch object detection
* Yolov4_epoch50.pth is the most accurate object detection model so far
### pytorch-YOLOv4
* Cloned git repository from Roboflow, that contains the necessary files to train and utilize model
### Roboflow
* Contains the annotation and images for training, validation, and testing 70-20-10 split respectively
### satellites
* Contains dataset for R-CNN image detection

## How to Run Models
### R-CNN

> python3 detect_object_rcc.py -i <file/path/to/image>


This is an adjusted detector from DatTran's raccoon detector. I changed the dataset to look for satellites instead.

You may need to check the config.py to see if your files are in the right directories

### YOLOv3
You must use Python 3.7

> python yolo_predict.py

### YOLOv4
Python 3.9 is recommended for best performance.

> python3 pytorch-detect-object.py

All the customization for image input is in the file. Image output is handled by pytorch-YOLOv4/models.py file.


## How to Train Models
### R-CNN
> python3 fine_tune_rcnn.py

This will train the rcnn against the settings preset in the config.py file.

### YOLOv3
> python3 pannel/train.py 

Use python 3.7, dependencies require python 3.7

This will train the model with the settings in config.py file.


### YOLOv4
> python3 pytorch-YOLOv4/train.py <config.cfg> <Yolov4.conv.137.pth>

This will train the model given the configurations in the cfg file with a pretrained model from pretrained mode.conv.137


## Annotating Datasets
[LabelImg tool](https://github.com/tzutalin/labelImg)

* run python labelImg.py
* Upload directory of images
* draw bounding boxes and save annotations

## Roboflow
Very useful image augmentations, preprocessing, and can provide dataset health checks.


## Helpful Links
[R-CNN](https://www.pyimagesearch.com/2020/07/13/r-cnn-object-detection-with-keras-tensorflow-and-deep-learning/)

[Multi-Class Object Detection](https://www.pyimagesearch.com/2020/10/12/multi-class-object-detection-and-bounding-box-regression-with-keras-tensorflow-and-deep-learning/)

[YOLOv3](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/)

[YOLOv4](https://blog.roboflow.com/training-yolov4-on-a-custom-dataset/)

[Roboflow Models](https://models.roboflow.com/)
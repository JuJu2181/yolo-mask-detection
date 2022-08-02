# YOLO Mask Detection System
## About
A system capable of detecting masks developed using YOLOv3 Darknet. This system can detect mask in image, video or in live webcam.

## Dataset Link:
[Kaggle Dataset](https://www.kaggle.com/datasets/aditya276/face-mask-dataset-yolo-format)

## Model Training File:
> yolov3-mask-detection-final.ipynb

## How to run?
1. Install Python 3.8.6 from [Python3.8](https://www.python.org/downloads/release/python-386/)

2. Install all requirements using:
```
pip install -r requirements.txt 
```
Better make a virtual environment before installing.  

3. Download the weight from this link: [YOLO Weights](https://drive.google.com/file/d/1DhDbirmjl3-NbTwV4dYCHkS-uUyKGrH2/view?usp=sharing)  

4. To detect in image:
```
py test_on_photo.py
```  

5. To detect in live video:
```
py test_on_video.py
```

## Outputs

### Detections in Image

![Output1](op1.jpg)
![Output2](op2.jpg)

### Detections in Video

https://user-images.githubusercontent.com/43902648/182372223-fd613893-73d2-4d94-9a31-b6582fccccc4.mp4



import cv2
import numpy as np 
import sys

cap = cv2.VideoCapture(0)

#loading Deep Neural Network for Yolo weights and yolo config file with classes name specified and finally outputlayer connected.
net = cv2.dnn.readNet("yolov3_training_best.weights", "yolov3_training.cfg")
classes = ["no_mask",'mask']
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

# print(layer_names)
# print('---------------------')
# print(output_layers)
# sys.exit(0)


while True: 
    ret,img=cap.read()
    # Resize helps in faster computation
    img = cv2.resize(img, None, fx=0.6, fy=0.6)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for out in outs:
        for detection in out:
            # print(detection)
            # [6.6084099e-01 2.0349213e-01 4.3849885e-02 5.2078888e-02 1.5960613e-070.0000000e+00 0.0000000e+00]
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence>=0.65:
                obj_name=classes[class_id] #Get obj name from classes list with class id index
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                if class_id == 0:
                    color = (0,0,255)
                elif class_id == 1:
                    color = (0,255,0)
                else:
                    color = (255,0,0)
                img=cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                img = cv2.putText(img,obj_name,(x-5,y-5), font,1.5, color, 2)            
        imS = cv2.resize(img, (800, 600))
        cv2.imshow('output',imS)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
path = (r"C:\Users\GURMEET SINGH\Documents\GitHub\object_detection\people.jpg")
cap = cv2.imread(path)
whT = 320
confThreshold = 0.4
nmsThreshold = 0.1

classesFile = 'coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)
# print(len(classNames))

modelConfiguration = 'yolov3-tiny.cfg'
modelWeights = 'yolov3-tiny.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs, img):
    hT, wT, _ = img.shape
    bbox = []
    global classIds
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3]*hT)
                x, y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
                
    
    # print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    for i in indices:

        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)


img = cap

blob = cv2.dnn.blobFromImage(cap, 1/255, (whT, whT), [0, 0, 0], crop=False)
# resized_image=cv2.resize(cap)
net.setInput(blob)

layerNames = net.getLayerNames()
outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

outputs = net.forward(outputNames)
findObjects(outputs, img)

cv2.imshow('output', cap)
cv2.waitKey()

def obj_list():
    global arr
    arr=[]
    for i in classIds:
        arr+=[classNames[i]]
        print(arr)
    return arr


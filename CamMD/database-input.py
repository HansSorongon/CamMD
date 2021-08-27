import cv2
import numpy as np
import time
import sqlite3

connect = sqlite3.connect('CamMDtest.db')
cursor = connect.cursor()

#create table for database
cursor.execute("""CREATE TABLE IF NOT EXISTS CamMD(
   wound TEXT NOT NULL,
   recommendation TEXT NOT NULL
   )""")





def captureandrecognize():
    # initialize yolo
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

    classes = []
    with open("coco.names", "r") as f:
        classes = f.read().splitlines()

    capture = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(100, 3))

    # video capture&boxes
    while True:
        s, frame = capture.read()
        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)
        label_list=[]
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                label_list.append(label)
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label + " " + confidence, (x, y + 20), font, 2, (255, 255, 255), 2)

        cv2.imshow('Image', frame)
        key = cv2.waitKey(1)
        if key == 27:  # maybe instead of esc key press do button?
            time.sleep(5)
            break
    capture.release()
    cv2.destroyAllWindows
    return label_list



def recommend(wound):
    for i in wound:
        cursor.execute("SELECT recommendation FROM CamMD WHERE wound = ?", (i,))
        recommendation=cursor.fetchmany(2)
        for j in recommendation:#send reccomendation to user
            print(j[0])

wounds=captureandrecognize()
print(wounds)
print(recommend(wounds))

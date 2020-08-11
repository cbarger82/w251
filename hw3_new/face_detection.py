# Import dependencies and load cascade
import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
face_cascade = cv.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

# MQTT host/port and topic IDs
LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw03"

def on_connect(client, userdata, result):
    print("Connected with result code {0}".format(str(result)))

mqttclient=mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# Capture using the USB camera
cap = cv.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #print("face detected ",face.dtype)
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        result_png = cv.imencode(".png", face_gray)[1]

        #msg = jpg.tobytes()
        mqttclient.publish(LOCAL_MQTT_TOPIC, payload=result_png.tobytes(), qos=2, retain=False)

    cv.imshow('frame', frame)

# Capture, send, then remove
cap.release()
cv.destroyAllWindows()

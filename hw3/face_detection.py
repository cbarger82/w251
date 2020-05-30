import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
face_cascade = cv.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

# MQTT host/port and topic IDs
MQTT_HOST="172.18.0.2"
MQTT_PORT=1883
MQTT_TOPIC="hw03"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc))) 

mqttclient=mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST,MQTT_PORT,60)

# Capture using the USB camera
cap = cv.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h,x:x+w]
        print("face detected ",face.dtype)
        rc,jpg = cv.imencode(".png",face)
        msg = jpg.tobytes()
        mqttclient.publish(MQTT_TOPIC,payload=msg,qos=2,retain=False)
    
# Capture, send, then remove
video_capture.release()
cv.destroyAllWindows()

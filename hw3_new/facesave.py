# Import dependencies
import paho.mqtt.client as mqtt
import random
import os
import numpy as np

bk_path = '/data/w251/hw3/mntbucket'

LOCAL_MQTT_HOST="cloud_mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw03"

def on_connect(client, userdata, flags, rc):
    print("connected to cloud broker with result code " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    print("on message received from cloud broker")
    num = random.randint(1,1001)

    path = bk_path + str(num) +'.png'
    imagefile = open(path, 'wb')
    imagefile.write(msg.payload)
    imagefile.close()


mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect 
mqttclient.on_message = on_message 

mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
#mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)

# Loop
mqttclient.loop_forever()


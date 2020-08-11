import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw03"

CLOUD_MQTT_HOST="169.61.16.130"
CLOUD_MQTT_PORT=1883
CLOUD_MQTT_TOPIC="hw03"

def on_connect(client, userdata, flags, rc):
    print("Connected to jetson with result: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_cloud(client, userdata, flags, rc):
    print("Connected to cloud with result: " + str(rc))

def on_message(client, userdata, msg):
    print("on message received")
    cloudmqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg.payload, qos=2, retain=False)

cloudmqttclient = mqtt.Client()
cloudmqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)
cloudmqttclient.on_connect = on_connect_cloud 

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect 
mqttclient.on_message = on_message 

mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
#mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)

# Loop
mqttclient.loop_forever()

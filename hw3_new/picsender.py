import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw03"

CLOUD_MQTT_HOST="52.116.6.89"
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
cloudmqttclient.on_connect = on_connect_cloud 
cloudmqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
mqttclient.on_message = on_message 



# Loop
mqttclient.loop_forever()


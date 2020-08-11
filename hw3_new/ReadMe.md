Steps for HW3:

Set up a bridge network via: docker network create --driver bridge hw03

Set up JETSON containers:
1. Face Detection Container
--Set up face detection docker image:
 ---- Dockerfile.fd - This container publishes messages to the Jetson MQTT Broker
 ---- face_detection.py - This is the python file used by the MQTT message forwarder that will push messages to the Cloud Broker
#BUILD CONTAINER: docker build -t facedetector -f Dockerfile.fd .
#Set permissions: xhost +
#START CONTAINER: docker run --privileged -it --rm --name=facedetector --network hw03 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix --volume $PWD:/home/w251/hw3_new facedetector:latest bash
  --Once in container, run face_detection.py


2. MQTT Broker Container
  --Used to listen for messages from the face detector (aka image info))
  ----Dockerfile.mqttbk
#BUILD CONTAINER: docker build -t mqttbk -f Dockerfile.mqttbk .
#START CONTAINER: docker run --name mosquitto --network hw03 -p 1883:1883 -ti mqttbk:latest /bin/ash
  --Once in container, do a mosquitto -v 

OUTPUT:
/home/w251/hw3_new # mosquitto -v
1597174738: mosquitto version 1.6.9 starting
1597174738: Using default config.
1597174738: Opening ipv4 listen socket on port 1883.
1597174738: Opening ipv6 listen socket on port 1883.
1597174969: New connection from 172.18.0.3 on port 1883.
1597174969: New client connected from 172.18.0.3 as auto-6910BFA5-A599-C9D6-157B-5A4F422AC99A (p2, c1, k60).
1597174969: No will message specified.
1597174969: Sending CONNACK to auto-6910BFA5-A599-C9D6-157B-5A4F422AC99A (0, 0)
1597174969: Received SUBSCRIBE from auto-6910BFA5-A599-C9D6-157B-5A4F422AC99A
1597174969: 	hw03 (QoS 0)

3. MQTT Forwarder Container
--Recieves messages from local broker and sends them to the cloud broker
----Dockerfile.mqttfwd
----picsender.py
#BUILD CONTAINER: docker build -t forwarder -f Dockerfile.mqttfwd .
#START CONTAINER: docker run --name forwarder --network hw03 -v /tmp/.X11-unix/:/tmp/.X11-unix --volume $PWD:/home/w251/hw3_new -ti forwarder:latest /bin/ash
  --Once in container, run python forwarder.py
#Forwarder is subscribing messages for the topic face_detect from the detector with QoS 2, which means to send the message exactly ONCE, and publishing messages to MQTTbroker

################################################################################

Set up CLOUD containers:
1. Set up a bridge network via: docker network create --driver bridge hw03

2. MQTT CLOUD Broker Container
  --Used to listen for messages from the face detector (aka image info), and then send the msgs to the image processor in the cloud.
  ----Dockerfile.cloudbk
#BUILD CONTAINER: docker build -t cloudbk -f Dockerfile.cloudbk .
#START CONTAINER: docker run --name cloud_mosquitto --network hw03 -p 1883:1883 -ti cloudbk:latest /bin/ash
  --Once in container, do a mosquitto -v 

3. Image processor on Cloud with volume mounted
  -- Image processor receives msgs from cloud broker and runs python file so images can be processed
  ----Dockerfile.imager
  ----imager.py - read msg, convert to bytes, process to image, save to cloud bucket storage location
#BUILD CONTAINER: docker build -t imager -f Dockerfile.imager .
#START CONTAINER: docker run --name cloud_imager --network hw03 -ti -v "$PWD":/home/w251/hw3_new -v "/mnt/mybucket":/home/w251/hw3_new/mntbucket imager:latest bash
  --mntbucket needs to be mapped to present working container so images sent to correct cloud storage


Object Storage URL: 

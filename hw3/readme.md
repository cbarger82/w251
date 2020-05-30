Attempted Flow for HW3:

1. Face Detection Container (Jetson)
--Set up face detection docker image to capture on Jetson using the data inside the following two files:
 ---- Dockerfile.fd (named docker image "face_detect")
 ---- face_detection.py
BUILD CONTAINER: docker build -t detector -f Dockerfile.fd .
START THIRD CONTAINER: docker run --name detector --network hw03 -e DISPLAY=$DISPLAY --privileged -v /home/cbarger/Documents/hw3/:/home/cbarger/Documents/hw3/ --rm -ti detector

This container is for the publishing of faces to broker in cloud using network hw03 as provided in hw file

*** Getting errors when try to run the container - not sure if python versions are the issue? Or if is an issue with how I am trying to set up the connection? Traceback (most recent call last):
  File "face_detection.py", line 16, in <module>
    mqttclient.connect(MQTT_HOST,MQTT_PORT,60)
  File "/usr/local/lib/python3.8/dist-packages/paho/mqtt/client.py", line 937, in connect
    return self.reconnect()
  File "/usr/local/lib/python3.8/dist-packages/paho/mqtt/client.py", line 1071, in reconnect
    sock = self._create_socket_connection()
  File "/usr/local/lib/python3.8/dist-packages/paho/mqtt/client.py", line 3522, in _create_socket_connection
    return socket.create_connection(addr, source_address=source, timeout=self._keepalive)
  File "/usr/lib/python3.8/socket.py", line 808, in create_connection
    raise err
  File "/usr/lib/python3.8/socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused



2. MQTT Container (Jetson)
--Set up container to setup mosquitto on Jetson
 ----Dockerfile.bug
BUILD CONTAINER: docker build -t mosquitto -f Dockerfile.bug .
START SECOND CONTAINER: docker run --name mosquitto --network hw03 -p 1883:1883 --rm -ti mosquitto

3. MQTT Capture Forwarding (Jetson)
--Set up container to send from Jetson to Cloud broker
 ----Dockerfile.picsend
 ----picsender.py
BUILD CONTAINER: docker build -t forwarder -f Dockerfile.picsend .
START FIRST CONTAINER: docker run --name forwarder --network hw03 -ti forwarder


Forwarder is subscribing messages for the topic face_detect from the detector with QoS 2, which 
means to send the message exactly ONCE, and publishing messages to MQTTbroker

4. MQTT broker Container (Cloud)
BUILD CONTAINER: docker build -t mosquitto -f Dockerfile.bug .
RUN CONTAINER: docker run --name mosquitto --network hw03 -p 1883:1883 --rm -ti mosquitto

5. (Cloud) Image processor on Jetson to Cloud with attempted volume mounted at /mnt/w251 
BUILD CONTAINER: docker build -t saver -f Dockerfile.filesave .
RUN CONTAINER: docker run --name saver -v /mnt/w251/:/mnt/w251/ --network hw03 --rm -ti saver
 
The image processor is supposed to subscribe to the messages for the face_detect topic and then save the face images in an object storage bucket, which I named w251.

Location of images: Erroring... 
 
Other: Object storage
cmd (running as root): s3fs w251 /mnt/w251 -o passwd_file=$HOME/.cos_creds -o use_path_request_style -o url=http://s3.us-east.cloud-object-storage.appdomain.cloud



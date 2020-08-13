1. Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?
* Attempted to use the face_recognition software found here: https://github.com/ageitgey/face_recognition
* Modified their included Dockerfile to add mqtt info
* Modified their python file - but the file I used needs opencv dependencies and even though I added to the Dockerfile, it still wouldn't recognize the 'import cv2' in the actual python file so the code wouldn't run.

Note: I found another walk through here: https://machinelearningmastery.com/how-to-perform-face-detection-with-classical-and-deep-learning-methods-in-python-with-keras/ that I would try next, but I was really hoping to get the original method to work out.

2. Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?

3. What framerate does this method achieve on the Jetson? Where is the bottleneck?

4. Which is a better quality detector: the OpenCV or yours?

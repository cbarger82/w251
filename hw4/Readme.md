# Homework 4: DL 101

#### 1. Classification of a 2D dataset using ConvnetJS
ConvnetJS is a very simple yet powerful JavaScript library for Convolutional Neural Networks created by Andrei Karpathy, previously a Graduate Student at Stanford (under Fei-Fei Li) 
and now the leader of the Autonomous Driving project at Tesla.  The library runs directly in the browser and uses the CPU of your computer for training (just one core, so it will be woefully slow on large networks).  It is highly interactive, however, and enables you to rapidly experiment with small nets. You can read more about ConvNetJs and its api at http://cs.stanford.edu/people/karpathy/convnetjs/
Our first lab aligns with the 2D classification example available here: http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html
Once you hit this page, the network starts running.  
* Add a few red dots in previously green areas by clicking the left mouse button.  Is the network able to adjust and correctly predict the color now? --- Yes, as long as the additions are not in the middle of the green area
* Add a few green dots in previously red areas by clicking the shift left mouse button.  Can the network adapt? --- Again, yes, as long as the additions are added to areas that make sense - it is interesting to see the changes to the network as it adapts to additions.
* Review the network structure in the text box.  Can you name the layers and explain what they do?

layer_defs = [];

layer_defs.push({type:'input', out_sx:1, out_sy:1, out_depth:2}); -- this is the INPUT layer, which is a dummy layer that declares the size of input volume and must be the first layer defined. In this case, we are declaring 2-Dimensional input points


layer_defs.push({type:'fc', num_neurons:6, activation: 'tanh'}); -- this is the FULLY CONNECTED layer. The job of these layers is to declare a layer of neurons that perform weighted addition of all inputs and pass them through a non-linearity. This line specifically is creating a layer of SIX neurons that use the 'tan h(x)' activation function

layer_defs.push({type:'fc', num_neurons:2, activation: 'tanh'}); -- This line is creating a layer of two neurons that also use the 'tan h(x)' activation function
layer_defs.push({type:'softmax', num_classes:2}); -- The bit identifies the classifier aka LOSS layer. This type of layer is used when we want to predict a set of discrete classes for our data. In this line of code, we are using type SOFTMAX, whose outputs are probabilities that sum to 1. Setting the number of classes to 2 means you have a binary classification, where your class is either 0 or 1.

* Reduce the number of neurons in the conv layers and see how the network responds. Does it become less accurate? --- If the number of neurons is small, then the network becomes much less accurate. Even at 5 neurons, the network seems to be able to make a good fit of the data.
* Increase the number of neurons and layers and cause an overfit.  Make sure you understand the concept --- Increasing the number of neurons and layers makes the network fit to every single dot, even those that seem a bit erroneous. Based on what the picture shows once the model is done fitting, it would be hard to think that if a completely different set of data was input, that the algorithm would correctly identify. 
* Play with activation functions.. -- relu vs sigmoid vs tanh... Do you see a difference ? Relu is supposed to be faster but less accurate. --- Looking at different types of data on the page, when I clicked 'simple data', the relu actually seemed to take longer to classify than the tanh did. Lowering down to 2 neuron layers leveled the playing field and now both relu and tanh seem to be quick, but less accurate than tanh with 5 nueron layers.

#### 2. ConvnetJS MNIST demo
In this lab, we will look at the processing of the MNIST data set using ConvnetJS.  This demo uses this page: http://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html
The MNIST data set consists of 28x28 black and white images of hand written digits and the goal is to correctly classify them.  Once you load the page, the network starts running and you can see the loss and predictions change in real time.  Try the following:
* Name all the layers in the network, describe what they do. ---- Code snippet from page:

layer_defs.push({type:'input', out_sx:24, out_sy:24, out_depth:1}); --- Input layer to define the size of the input volume. In this case, we see that the input is a 24x24 RGB image

layer_defs.push({type:'conv', sx:5, filters:8, stride:1, pad:2, activation:'relu'}); --- This is a CONVOLUTION layer, which are mainly used when training CNNs on images. A convolution layer is similar to the FC layer from the previous example in that it creates neuron layers with the difference being that these layers are only connected locally, meaning they are not connected to every neuron in the network below; they are connected to only a few and their parameters are shared. These layers take in three parameter inputs; 'filter size' (sx), 'number of filters' (filters), and the 'stride' at which they are applied in the input volume (stride). The activation parameter works similarly to the fc input and the 'pad' paramter is used to automatically pad the input by some amount of pixels with zeros. Specific to this line of code, 8 5x5 filters will be convolved with the input using a padding of 2 and an activation function of ReLu.

layer_defs.push({type:'pool', sx:2, stride:2}); --- The POOLING layer provides max pooling on every input layer without going through the activation step. In this case, we are saying we want to perform max pooling in 2x2 non-overlapping neighborhoods

layer_defs.push({type:'conv', sx:5, filters:16, stride:1, pad:2, activation:'relu'}); --- Similar to above, but with 16 5x5 filters instead of 8

layer_defs.push({type:'pool', sx:3, stride:3}); --- Similar to above, but we now want to perform max pooling in 3x3 non-overlapping neighborhoods

layer_defs.push({type:'softmax', num_classes:10}); --- Using softmax, so will output probabilities, with number of classes, k equal to 10. 

* Experiment with the number and size of filters in each layer.  Does it improve the accuracy? Lowering the number of filters decreases accuracy, as does making the size of the filters smaller. Increasing both seems to increase the accuracy quite a bit. Decreasing the number of filters to 2 decreased the accuracy quite a lot!
* Remove the pooling layers.  Does it impact the accuracy? Removing the pooling appears to allow the model to get to a higher training accuracy faster than when the pooling layers are present.
* Add one more conv layer.  Does it help with accuracy? -- Adding another conv layer actually seems to hurt the model. Two conv layers seemed to produce results faster and more accurately than when a third layer was added. Training accuracies using three conv layers seemed to peak out at around 97-98% whereas with two layers only and allowing the model to run for less time, I noticed a few 99-100% peaks during training.
* Increase the batch size.  What impact does it have? --- Increasing the batch size seems to help the accuracy of the model, which I would expect since more data is trained/tested with each iteration. Increasing it too much (like, 5000) seemed a detriment to both the computational power and the accuracy.
* What is the best accuracy you can achieve? Are you over 99%? 99.5%? Using 2 conv layers with 4 5x5 and 8 5x5 filters, I can achieve above 99% accuracy. My batch size is set to 50.

#### 3. Build your own model in Keras
The [Conversation AI](https://conversationai.github.io/) team, a research initiative founded by [Jigsaw](https://jigsaw.google.com/) and Google (both a part of Alphabet) are working on tools to help improve online conversation. One area of focus is the study of negative online behaviors, like toxic comments (i.e. comments that are rude, disrespectful or otherwise likely to make someone leave a discussion).   
  
Kaggle are currently hosting their [second competition](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge#description) on this research. The challenge is to create a model that is capable of detecting different types of of toxicity like threats, obscenity, insults, and identity-based hate better than Perspective’s current models. The competitions use a dataset of comments from Wikipedia’s talk page edits. Improvements to the current model will hopefully help online discussion become more productive and respectful.

We shall be using this dataset to benchmark a number of ML models. 
*Disclaimer: the dataset used contains text that may be considered profane, vulgar, or offensive.*

##### a. Running on your Jetson
Your Jetson is quite powerful; let's start a keras / tensorflow - enabled jupyter notebook on it:
```
docker run --rm --privileged -p 8888:8888 -d  w251/tensorflow_hw04:dev-tx2-4.3_b132
# once you run this command, it will print the id of the container, e.g.
# root@dima-desktop:~/v2/backup/keras# docker run --rm --privileged -p 8888:8888 -d  w251/tensorflow_hw04:dev-tx2-4.3_b132 
7d783a4b0feb89fe91072c0d6934a000471fa101cf9e5b6c09b4b8d881291903

# Now, get the token from docker logs:
root@dima-desktop:~/v2/backup/keras# docker logs 7d783a4b0feb89fe91072c0d6934a000471fa101cf9e5b6c09b4b8d881291903
[I 16:11:29.070 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 16:11:30.208 NotebookApp] Serving notebooks from local directory: /notebooks
[I 16:11:30.208 NotebookApp] The Jupyter Notebook is running at:
[I 16:11:30.208 NotebookApp] http://7d783a4b0feb:8888/?token=0cebf472b557f2e871de6be4e0717ff35cdd30b013b0d7e5
[I 16:11:30.209 NotebookApp]  or http://127.0.0.1:8888/?token=0cebf472b557f2e871de6be4e0717ff35cdd30b013b0d7e5
[I 16:11:30.209 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation)
```
Now, point your browser to http://yourjetsonip:8888?token=yourtoken

##### b. Running in the Cloud
Set up a CPU based VM to run your models. We shall use sparse matrices which are better suited to CPU than GPU. 
I set the VM up like below, you may need to change the `datacenter` and `domain`.
```
ibmcloud sl vs create --datacenter=lon06 --hostname=hw04cpu --domain=darragh.com --os=UBUNTU_16_64 --flavor C1_8X8X100 --billing=hourly --san --disk=100 --disk=2000 --network 1000  --key=1418191
```
As before check the VM is created with `ibmcloud sl vs list`  
Login like `ssh -i /home/darragh/.ssh/id_rsa 158.176.93.70 -l root` or `ssh root@158.176.93.70`. You may need to wait a couple of minutes before logging in for the VM to br created. 

Once logged into the VM as `root` user, **Install docker**:
```
# Validate these at https://docs.docker.com/install/linux/docker-ce/ubuntu/
apt-get update
apt install apt-transport-https ca-certificates 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test" 
apt update 
apt install docker-ce
# Validated 09/14/19 - Darragh
# Test if docker hello world is working
docker run hello-world
```

Now we pull the image and start our jupyter notebook. 
```
docker run --rm -it -p 8888:8888 w251/tensorflow_hw04:latest
```

You will have an output of the location of the book running line below
```
[I 11:47:41.840 NotebookApp] The Jupyter Notebook is running at:
[I 11:47:41.841 NotebookApp] http://(5ebf32ea4e17 or 127.0.0.1):8888/?token=ffbb6d6b3a9b2e24fb8e0cc7eb8eb0657e1f58fa5595c5d4
```
Replace the domain name of the URL with your servers, public IP. For example for the above output I would go to URL. 
```
http://158.176.93.70:8888/?token=ffbb6d6b3a9b2e24fb8e0cc7eb8eb0657e1f58fa5595c5d4
```
Now open the notebook and run. And fill in the codes blocks marked for filling in and monitor your AUC. 
For the Logistic regression model you should be getting circa `0.88` AUC and `0.93` or more for the MLP. 

#### Submission:
Please submit answers to #2, and a html download of your completed Jupyter notebook. A link to a github repo is a great way to submit.
 

PLEASE CANCEL YOUR VM ONCE YOU ARE DONE!!!

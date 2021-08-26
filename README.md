# raspberry-image-classification-for-dummies

Image classfication on the Raspberry cannot be more simple! 

### Hardware:
- Raspberry Pi 4 (or 3 maybe). I have one with 4 GB RAM. 
- Raspicam

### Software:
Clone the repository

Per the [https://www.tensorflow.org/lite/guide/python] , install tensorflow lite on the Raspberry:\
`echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list`

`curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -`

`sudo apt-get update`

`sudo apt-get install python3-tflite-runtime`

### How to use:
Hold an (image of) a fruit in front of the camera and run the script.
The model is also trained with a class 'idle' in case there is no fruit.

### Train your own!
Use Google's Teachable Machine to train your own ML model: [https://teachablemachine.withgoogle.com] 

First train a model, export it in Tensorflow lite format. Copy the files to your raspberry and rename them (or edit the script). 
Have fun!

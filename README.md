# raspberry-image-classification-for-dummies

Image classfication on the Raspberry cannot be more simple! 

## Hardware:
- Raspberry Pi 4 (or 3 maybe). I have one with 4 GB RAM. 
- Raspicam

## Software:
Clone the repository

Per the [https://www.tensorflow.org/lite/guide/python instructions], install tensorflow lite on the Raspberry:
$ echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
$ curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install python3-tflite-runtime

Instruction:
hold an (image of) a fruit in front of the camera and run the script.

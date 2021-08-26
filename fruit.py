#!user/bin/python3

# script by Michiel Bontenbal twitter: @mpbontenbal www.github.com/MichielBbal
# based on a script by Rob Lauer www.github.com/rdlauer

# Run tensorflow lite on a raspberry Pi 4 with Picam
# Create your own models teachablemachine.withgoogle.com

import time
import numpy as np
import picamera
from PIL import Image
from tflite_runtime.interpreter import Interpreter

# init Raspberry Pi Camera
camera = picamera.PiCamera()
camera.resolution = (224, 224)  # ML model expects 224x224 image

# specify paths to local file assets
path_to_labels = "fruit-labels.txt"
path_to_model = "fruit-model.tflite"
path_to_image = "fruit.jpg"

# confidence threshold at which you want to be notified of a new bird
prob_threshold = 0.5


def main():
    #""" check to see if PIR sensor has been triggered """
    #if pir_sensor.value:
    time.sleep(10)  # only check for motion every 30 seconds!
    check_for_bird()


def check_for_bird():
    """ is there a bird at the feeder? """
    labels = load_labels()
    interpreter = Interpreter(path_to_model)
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']

    camera.start_preview()
    time.sleep(2)  # give the camera 2 seconds to adjust light balance
    camera.capture(path_to_image)
    image = Image.open(path_to_image)
    results = classify_image(interpreter, image)
    label_id, prob = results[0]
    print("classification: " + labels[label_id])
    print("probability: " + str(prob))
    camera.stop_preview()

def load_labels():
    """ load labels for the ML model from the file specified """
    with open(path_to_labels, 'r') as f:
        return {i: line.strip() for i, line in enumerate(f.readlines())}


def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
    """ return a sorted array of classification results """
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))

    # if model is quantized (uint8 data), then dequantize the results
    if output_details['dtype'] == np.uint8:
        scale, zero_point = output_details['quantization']
        output = scale * (output - zero_point)

    ordered = np.argpartition(-output, top_k)
    return [(i, output[i]) for i in ordered[:top_k]]

while True:
    main()

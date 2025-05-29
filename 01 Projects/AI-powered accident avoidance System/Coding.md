---
id: Coding
aliases: []
tags: []
---

## Install the Libs

```bash
pip install ultralytics

```

_note that after some time i have to reinstall ultralytics_

## Pi to ESP i2c 


```c
// source : https://dronebotworkshop.com/i2c-arduino-raspberry-pi/ 
const int ledPin = 13; 
 
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  
  // Setup pin 13 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
void loop() {
  delay(100);
}
```



## Coding

### PI Code 

**Sources** : https://www.instructables.com/Autonomous-Lane-Keeping-Car-Using-Raspberry-Pi-and/

```python
import cv2

video = cv2.VideoCapture(0)

while True:
  ret,frame = video.read()
  frame = cv2.flip(frame,-1) # used to flip the image vertically
  cv2.imshow('original',frame)
  cv2.imwrite('original.jpg',frame)

  key = cv2.waitKey(1)
  if key == 27:
     break

video.release()
cv2.destroyAllWindows()
```

<details> <summmary></summary> </details>

### Using YOLO

- Trainer Kit

```python
from multiprocessing import freeze_support
from ultralytics import YOLO
def main():
    # Load the YOLOv5n model (small version of YOLOv5)
    model = YOLO("yolov5nu.pt")  # Use YOLOv5n model

    # Train the model using the custom dataset
    model.train(
        data="./datasets/data.yaml",  # Path to your dataset YAML file
        epochs=1,  # Number of training epochs (adjust as needed)
        imgsz=640,  # Input image size (adjust based on your dataset)
        batch=8,  # Batch size for training (adjust if needed)
        name="model",  # Name of the experiment/logs folder
        device="cpu",  # Use 'cpu' if no GPU is available (for Raspberry Pi)
        workers=4,  # Adjust based on your system's capabilities
    )

if __name__ == "__main__":
    freeze_support()  # For Windows-based systems, ensuring proper multiprocessing
    main()
```

- Model run

```python
import cv2
import numpy as np
from ultralytics import YOLO
import time

# Load the YOLOv8 model from the provided path
model = YOLO('/home/pi/best.onnx', task='detect')

# Function to perform object detection on a frame
def detect_objects(frame):
    results = model(frame)
    annotated_frame = results[0].plot()  # Get the annotated frame with bounding boxes and labels
    return annotated_frame

# Start video capture from USB camera
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform object detection on the frame
    detected_frame = detect_objects(frame)

    # Display the detected frame
    cv2.imshow("Detected PPE Objects", detected_frame)

    # Add a sleep time to manage frame rate
    time.sleep(0.03)  # Adjust to control the speed

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
```

- Convert.py

```python
from ultralytics import YOLO

# Load the YOLO11 model
# model = YOLO(r"C:\Users\FEBY DAS K Y\Desktop\working models\best.pt")
model = YOLO(r"./yolov5nu.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'yolo11n.onnx'

# Load the exported ONNX model
onnx_model = YOLO("fireppe.onnx")
```


### Microcontroller Code 

#### Lane Departure Warning
- It uses ir sensor 
```c
#include "ir_sensor.h"
#include <Arduino.h>
IR_Sensor::IR_Sensor(uint8_t pin) {
	_pin = pin;
	pinMode(_pin, INPUT);
}
bool IR_Sensor::is_lane() {
	return digitalRead(_pin);
}
```
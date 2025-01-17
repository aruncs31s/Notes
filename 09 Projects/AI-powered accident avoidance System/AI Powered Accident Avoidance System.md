---
id: 18-01-25-Project
aliases:
  - AI Car
tags:
  - project,
Date:
  Started: "18-01-2025"
  Starting: NILL
  Target: "13-02-2025"
GithubLink: https://github.com/aruncs31s/AI-Based-Accident-Avoidance-System-AI-BAAS
Status:
  Completed: false
  Working_ON: true
cssclasses:
  - wide-page
dg-publish: true
---

# APAAS

## Components

| Components                                   | Qty | Cost        |
| -------------------------------------------- | --- | ----------- |
| [Raspberry Pi 5](https://amzn.in/d/30wDSem)  | 1   | 8250/-      |
| [Pi Cam](https://amzn.in/d/gbrcEMg)          | 1   | 361/-       |
| 18650 Battery 3.7V                           | 4   | 210/-       |
| [Car Chassis](https://amzn.in/d/c0FgwMO)     | 1   | 678/-       |
| [Boost Converter](https://amzn.in/d/dno182p) | 1   | 296/-       |
| Miscellaneous                                |     | 300/-       |
| Total                                        | -   | 10095/-<br> |
## Case Study 

#### Problem Statement 
Accidents involving vehicles often occur due to blind spots, lack of pedestrian awareness, and insufficient real-time feedback for drivers. This poses a significant risk to both pedestrians and drivers.

#### Initial Solution 
==Attach a camera to the car's bonnet== equipped with AI-powered image recognition and real-time processing. This system can ==detect pedestrians, cyclists, and obstacles,== alerting the driver with audible and visual signals. It can also integrate advanced security features such as ==automatic braking, lane departure warnings, and adaptive cruise control==, ensuring pedestrian safety and reducing the likelihood of accidents.


1. Collision Avoidance (CA)
2. AI-based driving assistance system (AI-DAS)
3. Raspberry Pi; OpenCV
4. safety message dissemination
5. multihop broadcast protocol for dissemination^[the action or fact of spreading something] of time-critical emergency messages (EMs) in vehicular ad hoc networks (VANETs)^[https://ieeexplore.ieee.org/document/6675860]
6.  medium access control (MAC)(check this out with the article)



## Coding
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
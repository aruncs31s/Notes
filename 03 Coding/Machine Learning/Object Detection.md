---
id: Object Detection
aliases: []
tags:
  - coding
  - machine_learning
dg-publish: true
---
# Object Detection
object detection draws bounding boxes around each detected object, specifying its location.^[https://www.ultralytics.com/glossary/object-detection]

**Prerequisites**
- [[CNN]]
- [[Intersection over Union|Intersection over Union (IoU)]]
- [[Mean average precision(mAP)]]

There are 2 process
1. Classification: Identifies what objects are present
2. Localization: where it is present , and draws a bounding box around them.

## Detecting Objects

![](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2018/11/yolo_design.jpg?lossy=2&strip=1&webp=1)

```mermaid
graph LR
Detectors --> R-CNN & Fast_R-CNN & YOLO & Single_Short_Detector(SSDs)
R-CNN --> Selective_Search

```


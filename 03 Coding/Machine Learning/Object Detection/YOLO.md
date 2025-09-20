---
id: YOLO
aliases: []
tags:
  - coding
  - machine_learning
  - object_detection
Date: 30-01-25
dg-publish: true
---
# YOLO

### Installition
Yolo also requiers pytorch

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

```

*Note that i have used only cpu, there is a cuda version -> [Check this](https://pytorch.org/get-started/locally/) out when i get a gpu*

```bash
pip install ultralytics opencv-python

```

--- Old 
- [ ] Need to check weather the notes down are actually usefull?

#### Mac OS
  

```bash
git clone https://github.com/pjreddie/darknet
cd darknet
make

```

```bash
wget https://pjreddie.com/media/files/yolov3.weights

```

##### **To run on a single image**

```bash
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

```

##### **To run on multiple images**
???

### Real-Time Detection
- Need to compile `darknet` with `cuda` and `openCV` 

```bash
./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights

```

> The following did not work

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install opencv-python

```

- edit `Makefile` and Change `OPENCV=0` to `1`

> Tring to install the  `libopusenc`

```bash
 brew install libopusenc

```

### Linux

```bash
git clone https://github.com/pjreddie/darknet
cd darknet
make

```

```bash
sudo pamcan -S opencv

```

```bash

```

## References 

1. https://pjreddie.com/darknet/yolo/

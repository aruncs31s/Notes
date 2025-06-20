---
aliases: 
Date: "17-05-2025"
---
# 05 HUman Interaction


## 
[Mac File Link](file:///Users/aruncs/Documents/AmritaOjectRecgRobot.pdf) [Paper Link](https://www.researchgate.net/publication/251892709_Object_recognition_and_obstacle_avoidance_robot) 
. Obstacle detection, pattern recognition and
obstacle avoidance

## Voice Assistant
### Home Assistant

```bash
 docker run -it -p 10200:10200 -v /home/aruncs/docker/data:/data rhasspy/wyoming-piper \
    --voice en_US-lessac-medium

docker run -it -p 10300:10300 -v /home/aruncs/docker/data:/data rhasspy/wyoming-whisper \
    --model tiny-int8 --language en

```
```
http://homeassistant.local:8123/
```

- [[Frigate]]
---
id: Gcek Weather Prediction
aliases: []
tags:
  - projects
  - ai_ml
  - gcek_weather_prediction
Completed: false
Starting Date: "2024-09-12"
Status: true
Target Date: "2024-09-23"
dg-publish: true
---
# Gcek Weather Prediction

#tasks

- [ ] Implement predictions based on obtained data using [Weather data scraper](https://github.com/aruncs31s/GCEK_Weather_Meter_Scraper)

[Source](https://janaksenevirathne.medium.com/building-a-weather-prediction-model-with-machine-learning-a-step-by-step-guide-9eaf768171be)

- Datasheet : It consists of Variables, they are often called features which is used to train the [[Machine Learning]] Model
  - Temperature
  - Humidity
  - Wind Speed

### Coding

- Read Data

```python
import pandas as pd

data = pd.read_csv("./data/readings/weather_data.csv")

```

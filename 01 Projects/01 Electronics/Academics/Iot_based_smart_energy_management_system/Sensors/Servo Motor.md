---
id: Servo_Motor
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - sensors
dg-publish: true
---
<h2 align="center">Servo Motor</h2>

- [Introduction]()
- [Specs](#specs)
- [Interfacing]()
-

#### Introduction

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4gbYIJz2kTJ4w4GVCk7cVSDW3qMh8HvBQig&usqp=CAU)

#### Specs

| Key     | Value               |
| ------- | ------------------- |
| Speed   | 0.12 – 0.10 sec/60o |
| Voltage | 4.8 – 6.0 V         |

#### Interfacing

```c
#include <ESP32Servo.h>

// Define the GPIO pin connected to the servo
const int servoPin = 2;

// Create a Servo object
Servo myservo;

void setup() {
  Serial.begin(9600);

  // Attach the servo to the GPIO pin
  myservo.attach(servoPin);
}

void loop() {
  // Sweep the servo back and forth
  for (int angle = 0; angle <= 180; angle += 1) {
    myservo.write(angle);
    delay(15);
  }
  for (int angle = 180; angle >= 0; angle -= 1) {
    myservo.write(angle);
    delay(15);
  }
}

```

- Need To install ESP32Servo.h Header file

#### Working

#### Solar Tracking algorithm using Servo Motor

```cpp
  short V_current_position = 0;
  short H_current_position = 0;
  bool status = 1;
  // int avg_top, avg_bottom, avg_left, avg_right;
  while (status != 0) {
    if (avg(LDR_TOP_LEFT, LDR_TOP_RIGHT) <
        avg(LDR_BOTTOM_LEFT, LDR_BOTTOM_RIGHT)) {
      Vertical_Servo.write(current_position - 1);
      if (current_position > SERVO_LIMIT_HIGH) {
        // FIXME:
        V_current_position = (V_current_position > SERVO_LIMIT_HIGH)
                                 ? SERVO_LIMIT_HIGH
                                 : V_current_position;
        delay(1000);
      }
      //
    } else if (avg(LDR_BOTTOM_LEFT, LDR_BOTTOM_RIGHT) <
               avg(LDR_TOP_LEFT, LDR_TOP_RIGHT)) {
      Vertical_Servo.write(current_position + 1);
      // FIXME:
      V_current_position = (V_current_position < SERVO_LIMIT_LOW)
                               ? SERVO_LIMIT_LOW
                               : current_position;
    } else {
      Vertical_Servo.write(current_position);
    }
    if (avg(LDR_BOTTOM_LEFT, LDR_TOP_LEFT) >
        avg(LDR_BOTTOM_RIGHT, LDR_TOP_RIGHT)) {
      Horizontal_Servo.write(current_position - 1);
      V_current_position = (V_current_position > SERVO_LIMIT_HIGH)
                               ? SERVO_LIMIT_HIGH
                               : V_current_position;
    }
    delay(5);
  }
    else if(avg(LDR_TOP_RIGHT,LDR_BOTTOM_RIGHT) > avg(LDR_TOP_LEFT,LDR_BOTTOM_LEFT){
    Horizontal_Servo.write(H_current_position + 1);
    H_current_position = (H_current_position < SERVO_LIMIT_LOW)
                             ? SERVO_LIMIT_LOW
                             : H_current_position;

    delay(5);
    }
    else {
    Horizontal_Servo.write(H_current_position);
    }
    delay(50);
}

```

rt = top_right
lt = left top
ld = bottom left
rd = bottom right

avt = avrage value top
avd = average value down
avl = average value left
avr = average value right

avt = avg()

```cpp

Vertical_Servo.write(current_position - 1);
      if (V_current_position > SERVO_LIMIT_HIGH) {
        // FIXME:
        V_current_position = (V_current_position > SERVO_LIMIT_HIGH)? SERVO_LIMIT_HIGH : V_current_position;
        delay(1000);
      }
      //
    } else if (avg(LDR_BOTTOM_LEFT, LDR_BOTTOM_RIGHT) <
               avg(LDR_TOP_LEFT, LDR_TOP_RIGHT)) {
      Vertical_Servo.write(V_current_position + 1);
      // FIXME:
      V_current_position = (V_current_position < SERVO_LIMIT_LOW)
                               ? SERVO_LIMIT_LOW
                               : current_position;
    } else {
      Vertical_Servo.write(V_current_position);
    }
    if (avg(LDR_BOTTOM_LEFT, LDR_TOP_LEFT) >
        avg(LDR_BOTTOM_RIGHT, LDR_TOP_RIGHT)) {
      Horizontal_Servo.write(H_current_position - 1);
      V_current_position = (V_current_position > SERVO_LIMIT_HIGH)
                               ? SERVO_LIMIT_HIGH
                               : V_current_position;
    }
    else if(avg(LDR_TOP_RIGHT,LDR_BOTTOM_RIGHT) > avg(LDR_TOP_LEFT,LDR_BOTTOM_LEFT){
    Horizontal_Servo.write(H_current_position + 1);
    H_current_position = (H_current_position < SERVO_LIMIT_LOW)
                             ? SERVO_LIMIT_LOW
                             : H_current_position;

    delay(5);
    }
    else {
    Horizontal_Servo.write(H_current_position);
    }
    delay(50);

    Serial.println(" Left Average = " + String(avg(LDR_BOTTOM_LEFT, LDR_TOP_LEFT)));
    delay(1000);
    Serial.println("Hi");
    delay(1000);

```

#### Findings
- Vertical_Servo  - 1 = clockwise


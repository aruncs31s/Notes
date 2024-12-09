---
aliases: 
Date: 06-12-2024
---
# Arduino PWM
**pins**:  (3, 5, 6, 9, 10, or 11). 

`analogWrite()` ->  Does not provide control over frequency 

Generating the PWM using any pin using digital PIN [Source](https://docs.arduino.cc/tutorials/generic/secrets-of-arduino-pwm/)
```c
void setup()
{
  pinMode(13, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  delayMicroseconds(100); // Approximately 10% duty cycle @ 1KHz
  digitalWrite(13, LOW);
  delayMicroseconds(1000 - 100);
}
```

		 
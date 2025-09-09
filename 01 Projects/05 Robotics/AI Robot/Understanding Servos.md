---
id: Understanding_Servos
aliases: []
tags:
  - projects
  - robotics
  - ai_robot
dg-publish: true
---
# Understanding Servos 
## Their Rotation (Sweep)
**Sweep**: the shaft of a RC servo motor back and forth across 180 degrees

There are mainly 2 types of motion for a servo motor , 
1. It's body maybe fixed and it rotor can move
2. Its rotor may be fiex and its body can move 

- The servo(MG995) moves **Counter Clockwise (Anti-Clockwise , + Ve Direction)** when angle increases 

![[Pasted image 20250608231528.png]]

>[!summary]- Code for triggering this behaviour
>#causeCode
>```cpp
>Servo s1;
>void setup(){
>	s1.attach(some_pin);
>}
>void loop(){
>	for (int i = 0 ; i < 180 ; ++ i){
>		s1.write(i);
>	}
>}
>```

^d90f88

#### Fixed Body 

```yaml
motion_direction: counter clockwise

```

> The rotating element is directly attached to the rotor and it will follow the same direction as the rotor. 
> - Servo Horn is the rotor in this case 
>![[Pasted image 20250608032206.png]]

Fixed body will be the most common , because it is mostly seen when testing . And when testing we usually write the following

We usually observe this motion as something(something attached to the rotor) travels from $\begin{bmatrix}  1 & 0\end{bmatrix} \to  \begin{bmatrix}-1 & 0\end{bmatrix}$ 

This movement happens if the **rotor** of the motor is not fixed.  And if someone were to touch the rotor and if there enough friction between the rotor and the finger the body will start to move, and the movement of the body will be in oposite direction. 
### Fixed Rotor

```yaml
motion_direction: clockwise

```

In this the rotor is fixed , this is mainly seen in linked motors[^1]
[^1]: linked motors in the sense that 2 or more motors connected together and they will form a "Z" like structure 

- motion of the moving part will be $\begin{bmatrix}  -1 & 0\end{bmatrix} \to  \begin{bmatrix}1 & 0\end{bmatrix}$  
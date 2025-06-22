# Walking
The key to walking is to adjust the center of mass. 
-  servo torque limits?
`
```cpp
void WalkForward(){
}
```


## Human Walking  (Bipedal walking)
![[Walk-Cycle.gif|right]] ^80cec7

**Humanoid walking involves:**
1. Alternating leg movements (gait cycle)
2. Weight shifting between legs
3. Arm swinging for balance
4. Center of gravity management
### 1. The Gait Cycle

![[Pasted image 20250622213556.png]]

```mermaid
graph TB 
gait --> Swing_Phase & Stance_Phase
```
#### Stance Phase (60%)
In this the foot is in contact with the ground 
- Initial contact (heel strike)
- Loading response (foot flat)
- Mid-stance
- Terminal stance (heel off)
- Pre-swing (toe off)
#### Swing Phase  (40%)
Foot is  not in contact with the ground 
- Initial swing
- Mid-swing
- Late swing
![[Pasted image 20250622214203.png]]

### 2. Weight Shifting
[Source](https://www.med.umich.edu/1libr/PMR/BalanceExercises/Weight%20Shifting%20-%20Side%20to%20Side.pdf)

![[Pasted image 20250622214408.png]]

### 3. Arm Swing

![[#^80cec7]]


- each arm swings with the motion of the **opposing** leg
- Swinging arms in an opposing direction with respect to the lower limb reduces the angular momentum of the body, balancing the rotational motion produced during walking
- As the walking speed increases, the amplitude of the arm swing increases accordingly.
- 
**Why**
 the leg swing results in an angular momentum that is balanced by the ground reaction moments on the stance foot. Swinging arms create an angular momentum in the opposing direction of lower limb rotation, reducing the total angular momentum of the body. Lower angular momentum of the body results in a decline on the ground reaction moment on the stance foot


### 4. Center of Gravity Management
Managing Center of Gravity (COG) crucial for maintaining balance and preventing falls. *By positioning the Center of Gravity over the base of support (feet)*
 
 [Source](https://en.egaco.com/11537/)
 ![[Pasted image 20250622220132.png]]
![[Pasted image 20250622220156.png]]
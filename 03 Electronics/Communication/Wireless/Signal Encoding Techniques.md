---
aliases: 
Date: 01-11-2024
tags:
  - communicaiton
---
# Signal Encoding Techniques
- Signal Encoding Criteria 
- Digital Data , Analog Signals
- Analog Data, Analog Signal 
- Analog Data, Digital Signals 

### Fundamentals 
**Common Communication Process** : In basic communication process we will have a source then a destination , between source and destination there will be a channel or medium(i guess?) .


>[!blank|right-small]
>![[BOB and OLIVIA.excalidraw]]

**BOB** and **OLIVIA** are childhood friends ,they like to talk about Technology and stuff . And they are in a cute little relationship . Also they go tho University of Electronics together. But one day **OLIVIA's** father **VICTER** take her away to a new place . Months go by , **BOB** is now studying **Communication System** and oneday he accidentally meets **OLIVIA** . she told **BOB** about her new location and said i will be there every day waiting for your message. 
So now **BOB** is exited and go to home because the sky is getting dark . After that night **BOB** tries to communicate with **OLIVIA** like usual . But the problem is **OLIVIA** is now $10Km$ apart so **BOB** has to make something with his engineering knowledge so he started working on a new communication system .

 >[!blank|right-small]
>![[basic communication.excalidraw]]

So now bob is imagining how he's gonna build this system . His imagination is as follows 
- **BOB** sends message **HI** to **OLIVIA** 
- **OLIVIA** can hear if the **BOB** is near him , but **OLIVIA** is far from where he is standing , about $10Km$ apart , but **BOB** wants to talk to her 
- One method is , he can scream loud enough that the **OLIVIA** can here but unfortunately for human we simply cant scream like that 
- So the **BOB** builds a **Communication System** why not? 
- Initially he transmits his voice through a **loud speaker** 
- The problem with the first method or approach is that the voice will not reach her(**OLIVIA**) because of fading[^1] 
- Also everyone near the Speaker can here his messages
- So he builds an **[[Antennas]]** to transmit the message 
- Due to **frequency** is being between $20 - 20Khz$ he will need 
$$
 L = \frac{\lambda}{4}
$$

> Where $L$ is the antenna lenght 

$$
\begin{align}
L &= \frac{\frac{c}{f }}{4} \\ \\
  &= \frac{3\times 10 ^ 8}{4 \times f}  \\
\end{align}
$$

>Which is around $1500km$ so he can not possibly build that kind of antenna 




---
[^1]: as the sound travels through air the sound will get reduced and reduced as the the distance increases and eventually reach to zero
- The problem with this approach is that our as we are humans our sound will have a frequency range of $20 - 20Khz$ 

![[03 Electronics/Communication/Wireless/attachments/basic communication.canvas|Untitled]]

![[basic comm with modulation.canvas|basic comm with modulation]]
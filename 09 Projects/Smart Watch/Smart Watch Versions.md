---
Date:
  Created: 2024-12-20
cssclasses:
  - wide-page
---
# Smart Watch Versions 
#### Requirements 
1. [ ] Should contain a sos button 
2. [ ] Should detect "HELP" command 
3. [ ] Should Send location to the parents 
4. [ ] Should measure the heart rate 
## Version 1

> [!multi-column]
>
>> [!blank]+ Use Case
>> ![[Smart Watch PCB Board GPS.excalidraw]]
>
>> [!blank]+ Resources
![[Smart Watch PCB Board GSM.excalidraw]]
>
>





### MIC Interfacing 
![[Drawing 2024-12-20 22.44.37.excalidraw]]

![[Pasted image 20241220232146.png]]

number of points/samples = **4581**

> starting of help 
$$
(4581 / 3 ) \times 1.86 = 2840.22 \tag{1}
$$
let this be $\large s_{start}$
> Ending of help
>  
$$
\left( \frac{4581}{3} \right) \times 1.96 = 2992.92 \tag{2}
$$

let this be $S_{stop}$


help took  $S_{stop} - S_{start} = 152$ samples 


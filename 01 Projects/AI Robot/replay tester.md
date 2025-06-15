---
aliases: 
Date: "16-06-2025"
---
# replay tester
Improved version of [[Position tester v0.0.1]]
- [ ] Complete Replay tester 📅 2025-06-16  

```widgets
type: countdown
date: 2025-06-16 12:00:00
to: Complete the Replay tester 🎉
```
## Inidial Idea 
Replay tester is indended to replay the data that is obtained from the `position_finder`. It its logic is as follows 
- Check if the new data has any difference from the initial angle 
- move each servo by a step from the initial angle to the new angle 
*This is ok if only one new `data` is available*. But in [[Position Finder.py]] i stored data in a [[json]] file which will contain more than one data entry. 

## Coding 
- Getting the `initial_angle`
```python
initial_angles = [25, 30, 160, 160, 160, 30, 93, 107, 130, 25, 160, 60, 150, 30, 90, 99]
```
---
id: Position_tester_v001
aliases: []
tags:
  - projects
  - robotics
  - ai_robot
Date: 16-06-2025
dg-publish: true
---
# Position tester v0.0.1
 ```python
import time
import requests
url = "http://192.168.181.110/setServo"
angles = [25, 30, 160, 160, 160, 30, 93, 107, 130, 25, 160, 60, 165, 25, 90, 99]
def set_position(val, id=0):
    req_params = {"id": id, "angle": val}
    response = requests.get(url, params=req_params)
    print(f"Response: {response.text}")
f_move = [[6, 75], [7, 85], [8, 110], [9, 35], [14, 75], [15, 85]]
f_move_2 = [[8, 90], [9, 0], [10, 180], [15, 99], [14, 90]]
f_move_3 = [
    [7, 80],
]
step = 1
# NOTE: to get id  the_arr[i][0]
# to get id from angles the index itself is the id
def move(the_arr):
    count = 0
    print("exec move")
    while not count == len(the_arr):
        for i in range(len(the_arr)):
            print(f"I: {i}")
            if the_arr[i][1] > angles[the_arr[i][0]]:
                angles[the_arr[i][0]] += step
                set_position(angles[the_arr[i][0]], the_arr[i][0])
                if angles[the_arr[i][0]] == the_arr[i][1]:
                    count += 1
                time.sleep(0.0005)
            elif the_arr[i][1] < angles[the_arr[i][0]]:
                angles[the_arr[i][0]] -= step
                # print(angles[the_arr[i][0]])
                set_position(angles[the_arr[i][0]], the_arr[i][0])
                if angles[the_arr[i][0]] == the_arr[i][1]:
                    count += 1
                time.sleep(0.0005)
if __name__ == "__main__":
    move(f_move)
    move(f_move_2)

```

```python
def move(the_arr):
    count = 0
    print("exec move")
    while not count == len(the_arr):
        for i in range(len(the_arr)):
            print(f"I: {i}")
            if the_arr[i][1] > angles[the_arr[i][0]]:
                angles[the_arr[i][0]] += step
                set_position(angles[the_arr[i][0]], the_arr[i][0])
                if angles[the_arr[i][0]] == the_arr[i][1]:
                    count += 1
                time.sleep(0.0005)
            elif the_arr[i][1] < angles[the_arr[i][0]]:
                angles[the_arr[i][0]] -= step
                # print(angles[the_arr[i][0]])
                set_position(angles[the_arr[i][0]], the_arr[i][0])
                if angles[the_arr[i][0]] == the_arr[i][1]:
                    count += 1
                time.sleep(0.0005)

```

## Logic 


---
id: Servos
aliases: []
tags:
  - projects
  - robotics
  - ai_robot
Date: 18-06-2025
dg-publish: true
---
# Servos

This will provide all supporting function for the servo's data manipulations
## Uses
- Get new_servos 

```python
new_servos = get_new_servos(initial_angles, new_angles)

```

- Get servos that's value is changed. 

```python
old_delta_servos = get_old_delta_servos(initial_angles, new_angles, new_servos)

```

#### `dict_to_list` 

```python
def dict_to_list(the_dict):
    if len(the_dict) != 16:
        raise ValueError("The dictionary must contain exactly 16 elements.")
    return [the_dict[i] for i in range(16)]

```

#### `list_to_dict`

```python
def list_to_dict(the_list):
    if len(the_list) != 16:
        raise ValueError("The list must contain exactly 16 elements.")
    return {id: angle for id, angle in enumerate(the_list)}

```

#example 

```python
initial_angles = [25, 30, 160, 160, 160, 30, 93, 107, 130, 25, 160, 60, 150, 30, 90, 99]
initial_angles_dict = list_to_dict(initial_angles)

```

#### `is_new_servos`

```python
from servos import list_to_dict , dict_to_list, is_new_servos

initial_angles = [25, 30, 160, 160, 160, 30, 93, 107, 130, 25, 160, 60, 150, 30, 90, 99]
new_angles = initial_angles.copy()

print(is_new_servos(list_to_dict(initial_angles), list_to_dict(new_angles)))

```

#example 

```python
from servos import list_to_dict , dict_to_list, is_new_servos

initial_angles = [25, 30, 160, 160, 160, 30, 93, 107, 130, 25, 160, 60, 150, 30, 90, 99]
new_angles = initial_angles.copy()

initial_angles_dict = list_to_dict(initial_angles)
new_angles_dict = list_to_dict(new_angles)

print(is_new_servos(initial_angles_dict, new_angles_dict))

initial_angles_dict.pop(10)

print(is_new_servos(initial_angles_dict, new_angles_dict))

```

>[!Note]- `int` keys vs `str` keys 
>```python
>initial_angles_dict["12"] = 100  
>initial_angles_dict[12] = 200 
>```

>They both are not same


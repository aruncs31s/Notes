---
id: Pandas
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# Pandas

- It provides

  - Cleaning
  - Exploring
  - Manipulating Data
  - and Analyzing Data

- Pandas can clean messy data sets, and make them readable and relevant.

##### Ordering

```python
import panda as pd
m -c "Telescope find_files"
a = [1 ,3 ,4 ]
print(pd.Series(a))

"""output:
0    1
1    3
2    4
dtype: int64
"""

```

2. Labeling

```python
print(pd.Series(a, index=["x", "y", "z"]))

```

3. Sorting

```python
sample_data = {"day1": 10, "day2": 300, "day3": 22}

print(pd.Series(sample_data).sort_values(ascending=True))

```

---
id: Modules
aliases: []
tags:
  - coding
  - python
Date: "15-06-2025"
dg-publish: true
---
# Modules
```bash
git add -A

```


```python
from .gui import gui_main 

```

- `.` -> current package , or directory 
- used when the `script` is part of a package
When executing these kind of scripts do the following , 

```bash
<path>.<sub_dir_path>.<filename_without_extension>

```

eg: 

```bash
python3 -m src.position_finder.position_finder

```

```python
from gui import gui_main

```

## Local Testing

```bash
pip install -e .

```

- This installs the package in editable mode, allowing you to test changes without reinstalling. 

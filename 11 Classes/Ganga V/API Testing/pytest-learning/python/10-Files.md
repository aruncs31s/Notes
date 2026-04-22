---
id: 10-Files
tags:
  - python
  - files
  - io
dg-publish: true
---

# Working with Files

Read and write files in Python.

## Read File

```python
with open("file.txt", "r") as f:
    content = f.read()
```

## Write File

```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

## Read Lines

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
```

---

**Next:** [[11-Built-in-Functions]] - Built-in functions

**See Also:** [[09-JSON]] - JSON
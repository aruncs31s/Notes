---
id: 03_Advanced
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
## Error handling

```python
try:
	somecode()
except SomeError:
		print("Error")
finally:
	print("Always executed")

```

#eg

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()
    print("File has been closed.")`

```
---
id: 09-JSON
tags:
  - python
  - json
dg-publish: true
---

# Working with JSON

Parse and generate JSON data.

## Parse JSON String

```python
import json
data = json.loads('{"name": "Ganga V", "age": 30}')
```

## Convert to JSON String

```python
json_str = json.dumps({"name": "Ganga V", "age": 30})
```

## Pretty Print

```python
print(json.dumps(data, indent=2))
```

---

**Next:** [[10-Files]] - Working with files

**See Also:** [[08-Exception-Handling]] - Exception handling
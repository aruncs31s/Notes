---
id: requests
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# `requests`

```bash

>>> import requests
>>> r = requests.get('https://www.python.org')
>>> r.status_code
200
>>> b'Python is a programming language' in r.content
True

... or POST:

>>> payload = dict(key1='value1', key2='value2')
>>> r = requests.post('https://httpbin.org/post', data=payload)
>>> print(r.text)
{
 ...
 "form": {
   "key1": "value1",
   "key2": "value2"
 },
 ...
}

```
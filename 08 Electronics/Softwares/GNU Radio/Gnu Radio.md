---
id: Gnu Radio
aliases: []
tags:
  - electronics
  - softwares
  - gnu_radio
Created: "09-10-2024"
cssclasses: 
dg-publish: true
---
# Gnu Radio

- [[Old Notes]]
- [[Modulations]]
[[GNU FM.canvas|GNU FM]]

## Tutorial

- Integer data type `int(10e3) -> 10000` , `int(3.2222) -> 3`
- `this is string`
- `.25` is `250m` -> converted to milli
- Lists -> [1,2,4,'k',4]
- Tuples -> (1,2,3,4)

```python
>>> (1,2,3)[:]
(1, 2, 3)
>>> (1,2,3,(2,3,4))
(1, 2, 3, (2, 3, 4))
>>> (1,2,3,(2,3,4))[3]
(2, 3, 4)
>>> (1,2,3,(2,3,4))[3][2]
4
>>> (1,2,3,(2,3,4))[3][:]
(2, 3, 4)
>>>

```

#### Types
![](https://wiki.gnuradio.org/images/7/7c/Types.png)

#### freq shifting
done by multiplication by a complex sinusoid.

### Streaming Data
- see https://wiki.gnuradio.org/index.php?title=Stream_Tags
- 
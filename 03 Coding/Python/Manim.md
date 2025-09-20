---
id: Manim
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# Manim 
[Tutorial](https://docs.manim.community/en/stable/tutorials/quickstart.html)

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

```

```python

```
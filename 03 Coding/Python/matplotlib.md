---
id: matlibplot
aliases: []
tags:
  - coding
  - python
dg-publish: true
---
# Matlibplot

- [[#Basics]]

## Basics

```python
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 2,4,3,4,5,1])
plt.show()

```

#### Ploting a Sine wave

```python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6 * np.pi, 0.1)
y = np.sin(x)

# Plotting Sine Graph
plt.plot(x, np.cos(x), color="green")
plt.plot(x, np.sin((3.14/2 )- x), color="red")
#plt.plot(x, np.tan(x), color="blue")

plt.show()

```

```python
import matplotlib.pyplot as plt
import networkx as nx

# Define the activities and their dependencies
activities = {
    'A': {'duration': 5, 'dependencies': []},
    'B': {'duration': 3, 'dependencies': ['A']},
    'C': {'duration': 7, 'dependencies': ['A']},
    'D': {'duration': 2, 'dependencies': ['B', 'C']},
    'E': {'duration': 4, 'dependencies': ['D']}
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for activity, info in activities.items():
    G.add_node(activity, duration=info['duration'])
    for dep in info['dependencies']:
        G.add_edge(dep, activity)

# Calculate the earliest and latest start/finish times
topo_sort = list(nx.topological_sort(G))
earliest_start = {node: 0 for node in G.nodes()}
earliest_finish = {node: activities[node]['duration'] for node in G.nodes()}
latest_finish = {node: earliest_finish[node] for node in G.nodes()}
latest_start = {node: latest_finish[node] - activities[node]['duration'] for node in G.nodes()}

for node in topo_sort[1:]:
    for pred in G.predecessors(node):
        earliest_start[node] = max(earliest_start[node], earliest_finish[pred])
    earliest_finish[node] = earliest_start[node] + activities[node]['duration']

for node in reversed(topo_sort):
    for succ in G.successors(node):
        latest_finish[node] = min(latest_finish[node], latest_start[succ])
    latest_start[node] = latest_finish[node] - activities[node]['duration']

# Draw the network diagram
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)

# Add critical path highlighting
critical_path = [node for node in G.nodes() if latest_start[node] == earliest_start[node]]
nx.draw_networkx_nodes(G, pos, nodelist=critical_path, node_color='red')

plt.title('CPM Network Diagram')
plt.axis('off')
plt.show()

```

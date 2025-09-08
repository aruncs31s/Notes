import numpy as np

inputs = [1, 2, 3, 4]
weights = [[1, 2, 1, 3], [1, 2, 3, 4], [1, 2, 3, 5]]
biases = [2, 2, 3]
print(np.dot(inputs, weights) + biases[1])
print(np.dot(weights, inputs) + biases[2])

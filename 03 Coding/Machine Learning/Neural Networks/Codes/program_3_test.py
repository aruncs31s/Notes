inputs = [1, 2, 3]
weights = [[2, 4, 5], [3, 4, 5], [0.1, 0.2, 0.3]]
biases = [2, -1, -2]

output = []

for neuron_weights, neuron_bias in zip(weights, biases):
    # print(neuron_weights)
    print(neuron_bias)

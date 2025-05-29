inputs = [1, 2, 3]
weights_1 = [2, 4, 5]
weights_2 = [3, 4, 5]
weights_3 = [0.1, 0.2, 0.3]

bias_1 = 2
bias_2 = -1
bias_3 = -2

output = [
    inputs[0] * weights_1[0]
    + inputs[1] * weights_1[1]
    + inputs[2] * weights_1[2]
    + bias_1,
    inputs[0] * weights_2[0]
    + inputs[1] * weights_2[1]
    + inputs[2] * weights_2[2]
    + bias_2,
    inputs[0] * weights_3[0]
    + inputs[1] * weights_3[1]
    + inputs[2] * weights_3[2]
    + bias_3,
]
print(output)

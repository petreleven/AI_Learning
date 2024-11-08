import numpy as np

inputs = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
])

outputs = np.array([0, 1, 0, 1, 1, 0])

weights1 = np.zeros(shape=(4, 3))
print(weights1)
weights2 = np.zeros(shape=(1, 4))

h_out = weights1.dot(inputs[0])
pred = weights2.dot(h_out)
error = pred - outputs[0] ** 2
delta = pred - outputs[0] 

print("error is" + str(error))
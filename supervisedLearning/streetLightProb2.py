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

weights1 = np.zeros(shape=(3, 4))
print(weights1)
weights2 = np.zeros(shape=(4, 1))

for i in range(100):
    for j in range(len(inputs)):
        h_out = inputs[j].dot(weights1)
        pred = h_out.dot(weights2)
        error = pred - outputs[j] ** 2
        delta = pred - outputs[j]
        delta_hidden = weights2.dot(delta.T)# T = Transpose aka reversing

        lr = 0.01
        #update weights
        weights2 -= h_out.T.dot(delta) * lr
        weights1 -= inputs.T.dot(delta_hidden) * lr
    
        print("error is" + str(error))
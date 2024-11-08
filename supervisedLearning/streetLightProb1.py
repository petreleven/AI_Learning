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

weights = np.array([-0.5, 0, -1])

myInput = inputs[0]
myOutput = outputs[0]

for i in range(20):
    for j in range(len(inputs)):
        pred = inputs[j].dot(weights)
        error = (pred - outputs[j]) ** 2
        print("ERROR is: " + str(error))
        delta = pred - outputs[j]
        print("DELTA is: " + str(delta))
        weightDelta = delta * inputs[j]
        weightDelta = weightDelta * 0.1 #lr
        weights -= weightDelta

pred = inputs[0].dot(weights)
print("Final Prediction: " + str(pred))
print("Final Weights: " + str(weights))
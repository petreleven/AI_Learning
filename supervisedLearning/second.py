import numpy as np

speed = 0.5
height = 0.7
cloudy = 1

#MATRICE
weights = [
    #speed height weather
    [0.6,  0.7,  0.4], # basketball
    [0.7,  0.3,  0.5], # football
    [0.3,  0.5,  0.7] # tennis
]

#VECTOR
inputs = [speed, height, cloudy]

weights = np.array(weights)
inputs = np.array(inputs)

# DOT PRODUCT
def neuralNetwork(input):
    prediction = input.dot(weights)
    return prediction
    """
    "todo  weights  *  input"
    bballPred = input[0] * weights[0][0] + input[1] * weights[0][1] + input[2] * weights[0][2]
    fballPred = input[0] * weights[1][0] + input[1] * weights[1][1] + input[2] * weights[1][2]
    tennPred = input[0] * weights[2][0] + input[1] * weights[2][1] + input[2] * weights[2][2]
    
    
    return [bballPred, fballPred, tennPred]
    """

answer = neuralNetwork(inputs)
print(answer)
# Input
number_fans = 0.5

# Outputs
target_win = 0.6
target_draw = 0.3
target_lose = 0.1
outputs = target_win, target_draw, target_lose

# Weights
weights = [0.7, 0.6, -0.2]

def neuralNetwork(weights, input):
                #win draw lose
    prediction = [0, 0,   0]
    for i in range(len(prediction)):
        prediction[i] = weights[i] * input
    return prediction

def calcErrors(predictions, targets):
            #win draw lose
    errors = [0, 0,   0]
    for i in range(len(errors)):
        errors[i] = (predictions[i] - targets[i]) ** 2
    return errors

def calcDeltas(predictions, targets):
            #win draw lose
    deltas = [0, 0,   0]
    for i in range(len(deltas)):
        deltas[i] = predictions[i] - targets[i]
    return deltas

def calcWeightDeltas(input, deltas):
    weightDelta = [0, 0, 0]
    for i in range(len(weightDelta)):
        weightDelta[i] = input * deltas[i]
    return weightDelta

lr = 0.1
def changeWeight(weights, weightDelta):
    for i in range(len(weights)):
        weights[i] = weights[i] - (weightDelta[i] * lr)

for i in range(2000):
    ai_pred = neuralNetwork(weights, number_fans)
    print("AI prediction: " + str(ai_pred))

    error = calcErrors(ai_pred, outputs)
    print("ERRORS are: " + str(error))
    delta = calcDeltas(ai_pred, outputs)
    print("DELTAS are: " + str(delta))
    weightDelta = calcWeightDeltas(number_fans, delta)
    print("WEIGHT DELTAS are: " + str(weightDelta))

    # Update Weights
    changeWeight(weights, weightDelta)
    
ai_pred = neuralNetwork(weights, number_fans)
print("Final prediction: " + str(ai_pred))





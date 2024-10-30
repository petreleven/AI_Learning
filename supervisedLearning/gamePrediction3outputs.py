# Input
number_fans = 50

# Outputs
target_win = 0.6
target_draw = 0.3
target_lose = 0.1
outputs = target_win, target_draw, target_lose

# Weights
weights = [0.7,  0.6, 11]

def neuralNetwork(weights, input):
                #win draw lose
    prediction = [0, 0,   0]
    prediction[0] = weights[0] * input # Win
    prediction[1] = weights[1] * input # Draw
    prediction[2] = weights[2] * input # Lose
    return prediction

def calcErrors(predictions, targets):
            #win draw lose
    errors = [0, 0,   0]
    errors[0] = (predictions[0] - targets[0]) ** 2 # Win
    errors[1] = (predictions[1] - targets[1]) ** 2 # Draw
    errors[2] = (predictions[2] - targets[2]) ** 2 # Lose
    return errors

def calcDeltas(predictions, targets):
            #win draw lose
    deltas = [0, 0,   0]
    deltas[0] = (predictions[0] - targets[0]) # Win
    deltas[1] = (predictions[1] - targets[1]) # Draw
    deltas[2] = (predictions[2] - targets[2]) # Lose
    return deltas

def calcWeightDeltas(input, deltas):
    weightDelta = [0, 0, 0]
    weightDelta[0] = input * deltas[0]
    weightDelta[1] = input * deltas[1]
    weightDelta[2] = input * deltas[2]
    return weightDelta

lr = 0.001
def changeWeight(weights, weightDelta):
    for i in range(len(weights)):
        weights[i] = weights[i] - (weightDelta[i] * lr)

for i in range(1000):
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





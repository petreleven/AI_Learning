# Our Inputs
subs = 10
previous_wins = 20
no_fans = 15
target = 0.8 #80% chance of winning
lr = 0.1

# Our Weights
          #Toes  PrvWins #Fans
weights = [0.1,  0.2,    -0.1]

inputs = [subs, previous_wins, no_fans]

def neuralNetwork(weights):
    pred = 0
    for i in range(len(inputs)):
        single_pred = inputs[i] * weights[i]
        pred = pred + single_pred
    return pred

def calcWeightDeltas(delta:float, inputs:list):
    weights_delta = [0, 0, 0]
    for i in range(len(inputs)):
        single_w_delta = inputs[i] * delta
        weights_delta[i] = single_w_delta * lr 
        
    return weights_delta

ai_pred = neuralNetwork(weights)
print("PREDICION is: " + str(ai_pred) + " and the TARGET is: " + str(target))
error = (ai_pred - target) ** 2
print("ERROR is: " + str(error))
delta = ai_pred - target
weights_delta = calcWeightDeltas(delta, inputs)
print("Weight Deltas: " + str(weights_delta))
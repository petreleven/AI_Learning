input = 2
target = 0.8

weight = 0.5
lr = 0.1

def neuralNetwork(weight):
    pred = input * weight
    return pred


for i in range (20):
    ai_pred = neuralNetwork(weight)

    error = (ai_pred - target) ** 2

    delta = ai_pred - target #how far off you are
    weight_delta = delta * input #how much you need to change the weight by

    weight = weight - weight_delta * lr #new weight

    print("Error: " + str(error))
    print("Delta: " + str(delta) + " | Weight Delta: " + str(weight_delta))
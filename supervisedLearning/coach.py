input = 0.5
target_prediction_output = 0.75

# Assume weight
weight = 20

def neuralNetwork():
    prediction = weight * input 
    return prediction

ai_prediction = neuralNetwork()
error = (target_prediction_output - ai_prediction) ** 2  # Square the error
print(error)
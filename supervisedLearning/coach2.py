input = 0.5
target_prediction_output = 0.75

# Assume weight
weight = 20

def neuralNetwork():
    prediction = weight * input 
    return prediction

ai_prediction = neuralNetwork()
error = (target_prediction_output - ai_prediction) ** 2  # Square the error
print("Original error" + str(error))

# Learning rate
lr = 0.1
weight = weight - lr
ai_prediction_with_increased_weight = neuralNetwork()
incr_weight_error = (target_prediction_output - ai_prediction_with_increased_weight) ** 2
print("Increase Weight:" + str(incr_weight_error))
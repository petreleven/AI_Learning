input = 0.5
target_prediction = 0.75

# Assume weight
weight = 20

def neuralNetwork(myinput, myweights):
    ai_pred = myinput * myweights
    return ai_pred

ai_pred = neuralNetwork(input, weight)
original_error = (target_prediction - ai_pred) ** 2  # Square the error
print("Original error: " + str(original_error))

# Increase weight
lr = 0.1
ai_pred = neuralNetwork(input, weight + lr)
new_error = (target_prediction - ai_pred) ** 2  # Square the error
print("Increased weight error: " + str(new_error))

ai_pred = neuralNetwork(input, weight - lr)
new_error = (target_prediction - ai_pred) ** 2  # Square the error
print("Decreased weight error: " + str(new_error))

# Update weight
weight = weight - lr
print("-"*20)

# Repeating with updated weight
ai_pred = neuralNetwork(input, weight)
original_error = (target_prediction - ai_pred) ** 2  # Square the error
print("Original error: " + str(original_error))

ai_pred = neuralNetwork(input, weight + lr)
new_error = (target_prediction - ai_pred) ** 2  # Square the error
print("Increased weight error: " + str(new_error))
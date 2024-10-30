input = 0.5
target_prediction = 0.75

# Assume weight
weight = 20

def neuralNetwork(myweights):
    ai_pred = input * myweights
    return ai_pred

lr = 0.1
orig_pred = neuralNetwork(weight)
print("Original prediction is: " + str(orig_pred))

for i in range (1000):
    ai_pred = neuralNetwork(weight)
    original_err = (target_prediction - ai_pred) ** 2
    
    # Inrease weight
    ai_pred = neuralNetwork(weight + lr)
    inc_w_err = (target_prediction - ai_pred) ** 2
    
    # Decrease weight
    ai_pred = neuralNetwork(weight - lr)
    dec_w_error = (target_prediction - ai_pred) ** 2
    
    # Update weight by checking least error
    if inc_w_err < original_err or dec_w_error < original_err:
        if inc_w_err < dec_w_error:
            weight = weight + lr
        elif dec_w_error < inc_w_err:
            weight = weight - lr
            
new_pred = neuralNetwork(weight)
print("New prediction is: " + str(new_pred))
print(weight)
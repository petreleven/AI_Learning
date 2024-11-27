import numpy as np
from keras.datasets import mnist
from matplotlib import pyplot as plt


(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
print(train_data.shape)
print(train_labels.shape)

# Reduce our training to 1000 images
train_data = (train_data[0:1000]) / 255
train_data = train_data.reshape(1000, 784)


# print(train_data.shape)
# print(train_data[0])

train_labels = train_labels[0:1000]
print(train_labels[0])
target_labels = np.zeros((1000, 10))

for index, value in enumerate(train_labels):
    # print(index, " ", value)
    target_labels[index][value] = 1
    # target_labels[0][5] = 1
    
print(train_labels[200])
print(target_labels[200])

hidden_layer_size = 10
output_layer_size = 10
weights_1 = 2 * np.random.random((784, hidden_layer_size)) - 1
weights_2 = 2 * np.random.random((hidden_layer_size, output_layer_size)) - 1
lr = 0.1

def relu(x):
    return (x > 0) * x
    
def relu_deriv(x):
    return x > 0

for i in range(100):
    error = 0
    for j in range(len(train_data)):
        layer_1 = train_data[j : j+1]
        layer_2 = relu(np.dot(layer_1, weights_1))
        layer_3 = np.dot(layer_2, weights_2) # Output
        # Error
        error += np.sum(layer_3 - target_labels[j:j+1]) ** 2
        
        #WE NEED DELTAS TO UPDATE OUR WEIGHTS
        #delta = pred - target
        delta_l3 = layer_3 - target_labels[j:j+1]
        delta_l2 = np.dot(delta_l3, weights_2.T) * relu_deriv(layer_2)
        
        #WE NEED WEIGHTS DELTAS
        #weight_delta = delta * input
        weight_delta_l3 = np.dot(layer_2.T, delta_l3)
        weight_delta_l2 = np.dot(layer_1.T, delta_l2)
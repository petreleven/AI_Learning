import numpy as np
from keras.datasets import mnist
from matplotlib import pyplot as plt


(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
print(train_data.shape)
print(train_labels.shape)

# Reduce our training to 1000 images
train_data = (train_data[0:1000]) / 255
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
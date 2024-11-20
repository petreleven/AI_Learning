import numpy as np
from keras.datasets import mnist
from matplotlib import pyplot as plt


(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
print(train_data.shape)
plt.imshow(train_data[4500], cmap='gray')
plt.show()
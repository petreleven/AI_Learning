import numpy as np

myInputs = [10, 11, 12]
myInputs_as_array = np.array(myInputs)
print(myInputs_as_array.shape)

myInputs = [
    [20, 20],
    [40, 40]
]
myInputs_as_array = np.array(myInputs)
print(myInputs_as_array.shape)

myInputs = myInputs * 2
print(myInputs)
myInputs_as_array = myInputs_as_array * 2
print(myInputs_as_array)

myfancyMatrice = np.ones((3,4))
print(myfancyMatrice)
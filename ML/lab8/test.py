from tensorflow import keras
from keras.datasets import mnist
import numpy as np

#(x_train, y_train), (x_test, y_test) = mnist.load_data()
#print(x_train)

a = [
    [
        [1],[2],[3]
    ],
    [
        [1],[2],[3]
    ],
    [
        [1],[2],[3]
    ],
]
print(list(map(np.ndarray.flatten,np.array(a))))
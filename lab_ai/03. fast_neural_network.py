# 03. fast_neural_network.py
import numpy as np

def relu(x):
    if x < 0:
        return 0
    else:
        return x

class Model:
    def __init__(self):
        self.relu = lambda x: np.maximum(0,x)
        self.sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

        # (x w1) - > (l1 w2) -> y
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 *16, 9))
        self.b1 = np.random.uniform(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9,6))
        self.b2 = np.random.uniform(low=-1, high=1, size=(6,))

    def predict(selfself, data):
        l1 = np.matmul(data, self.w1) + self.b1
        l1 = self.relu(l1)

        l2 = np.matmul(l1_output, self.w2) + self.b2
        l2_output = self.sigmoid(l2)

        predict = 12_output
        print(result)

if __name__== '__main__':
    model = Model()
    data = np.random.randint(0, 3 (13*16,), dtype=np.int)
    print(model.predict(data))
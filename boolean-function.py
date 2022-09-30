import math
from random import randint
import numpy as np

# n inputs => 2^n outputs

class Network:
    def __init__(self, weights, theta):
        self.weights = weights
        self.theta = theta
        self.N = len(weights)

    def calcBooleanFunc(self, func, input):
        n = len(input)
        binStr = ''
        for j in range(0, n):
            if input[j] == 1:
                binStr += '1'
            else:
                binStr += '0'

        index = int(binStr, 2)
        return func[index]

    def indexToInput(self, i):
        binary = bin(i)[2:].zfill(self.N)

        input = []
        for b in binary:
            if b == '1':
                input.append(1)
            else:
                input.append(-1)

        return input

    def trainNetwork(self, func):
        for _ in range(0, 20):
            # Loop over possible inputs
            for i in range(0, pow(2, self.N)):

                # Generate input value
                input = self.indexToInput(i)

                # Take input and run through network.
                O = self.calcNetworkOutput(input)
                t = self.calcBooleanFunc(func, input)

                # Update weights and theta
                self.theta += -0.05 * (t - O)
                for j in range(0, self.N):
                    dw = 0.05 * (t - O) * input[j]
                    self.weights[j] += dw

    def calcNetworkOutput(self, input):
        sum = 0
        for j in range(0, self.N):
            sum += self.weights[j] * input[j]

        if (sum - self.theta) < 0:
            O = -1
        else:
            O = 1

        return O

    def testNetwork(self, func):
        for i in range(0, pow(2, self.N)):

            # Generate input value
            input = self.indexToInput(i)

            O = self.calcNetworkOutput(input)
            t = self.calcBooleanFunc(func, input)
            if O != t:
                return False

        return True


def genBooleanFunc(nr_inputs):
    outputs = []
    for _ in range(0, pow(2,nr_inputs)):
        if randint(0, 1) == 0:
            outputs.append(-1)
        else:
            outputs.append(1)

    return outputs

def initWeights(nr_inputs):
    standard_deviation = 1/nr_inputs
    mean = 0

    w = np.random.normal(mean, standard_deviation, nr_inputs)
    return list(w)


def testFunctionsSeparable(n):
    funcs = []
    for i in range(0, 10000):
        func = genBooleanFunc(n)
        weights = initWeights(n)
        theta = 0

        network = Network(weights, theta)

        network.trainNetwork(func)
        linearSeparable = network.testNetwork(func)

        if linearSeparable:
            if func not in funcs:
                funcs.append(func)

    return len(funcs)

funcsList = []
funcsList.append(testFunctionsSeparable(2))
funcsList.append(testFunctionsSeparable(3))
funcsList.append(testFunctionsSeparable(4))
funcsList.append(testFunctionsSeparable(5))

print(funcsList)

import array
from random import randint
from multiprocessing import Process
from multiprocessing import Manager
import numpy as np

def genPatters(p, N):
    patterns = []
    for i in range(p):
        pattern = []
        for j in range(N):
            val = randint(0, 1)
            if val == 1:
                pattern.append(1)
            else:
                pattern.append(-1)
        patterns.append(pattern)
    return patterns


def storePatterns(p):
    neurons = len(p[0])
    patterns = len(p)
    shape = (neurons, neurons)
    weights = np.zeros(shape)

    for i in range(0, neurons):
        for j in range(0, neurons):
            patternsSum = 0
            for pat in range(0, patterns):
                storingPattern = p[pat]
                patternsSum += storingPattern[i]*storingPattern[j]

            weights[i][j] = patternsSum/neurons

    return weights

def runWithState(S, weights):
    newS = S
    for i in range(0, len(S)):
        si = S[i]
        new_si = 0
        for j in range(0, len(S)):
            new_si += weights[i][j]*si

        if new_si < 0:
            newS[i] = -1
        else:
            newS[i] = 1

    return newS


def randomCalcOneStepError(S, weights):
    random_index = randint(0, len(S)-1)
    random_si = S[random_index]

    sum = 0
    for j in range(0, len(S)):
        sum += weights[random_index][j]*S[j]

    if sum < 0:
        random_si = -1
    else:
        random_si = 1

    return S[random_index] != random_si

def runXTrials(trials, p, N):
    fails = 0
    ran = 0
    for x in range(0, trials):
        print("Step: " + str(p) + " Progress: " + str(ran))
        patterns = genPatters(p, N)
        weights = storePatterns(patterns)
        feedPattern = patterns[1]

        swapped = randomCalcOneStepError(feedPattern, weights)
        if swapped:
            fails += 1
        ran += 1

    return fails/trials


one_step_values = []

runTimes = 100000
N = 120

one_step_values.append(runXTrials(runTimes, 12, N))
print("p=12 Finished. Value: " + str(one_step_values[0]))
one_step_values.append(runXTrials(runTimes, 24, N))
print("p=24 Finished. Value: " + str(one_step_values[1]))
one_step_values.append(runXTrials(runTimes, 48, N))
print("p=48 Finished. Value: " + str(one_step_values[2]))
one_step_values.append(runXTrials(runTimes, 70, N))
print("p=70 Finished. Value: " + str(one_step_values[3]))
one_step_values.append(runXTrials(runTimes, 100, N))
print("p=100 Finished. Value: " + str(one_step_values[4]))
one_step_values.append(runXTrials(runTimes, 120, N))
print("p=120 Finished. Value: " + str(one_step_values[5]))

print(one_step_values)

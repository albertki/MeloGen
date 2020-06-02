# Written by Albert Ki
import numpy as np
import random as rm

class Markov:
    def __init__(self, states, transitionName, transitionMatrix):
        print('Markov() object created')
        # statespace
        self.states = states
        self.transitionName = transitionName
        self.transitionMatrix = transitionMatrix

    # A function that implements the Markov model to predict the next note duration.
    def note_forecast(self, days, startState):
        noteSequence = [startState]
        i = 0
        prob = 1
        while i != days:
            if startState == "0.5":
                change = np.random.choice(self.transitionName[0],replace=True,p=self.transitionMatrix[0])
                if change == "0.5-0.5":
                    prob = prob * self.transitionMatrix[0][0]
                    noteSequence.append("0.5")
                    pass
                elif change == "0.5-1.0":
                    prob = prob * self.transitionMatrix[0][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "0.5-1.5":
                    prob = prob * self.transitionMatrix[0][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "0.5-2.0":
                    prob = prob * self.transitionMatrix[0][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "0.5-2.5":
                    prob = prob * self.transitionMatrix[0][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "0.5-3.0":
                    prob = prob * self.transitionMatrix[0][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                elif change == "0.5-3.5":
                    prob = prob * self.transitionMatrix[0][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "0.5-4.0"
                    prob = prob * self.transitionMatrix[0][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "1.0":
                change = np.random.choice(self.transitionName[1],replace=True,p=self.transitionMatrix[1])
                if change == "1.0-1.0":
                    prob = prob * self.transitionMatrix[1][1]
                    noteSequence.append("1.0")
                    pass
                elif change == "1.0-0.5":
                    prob = prob * self.transitionMatrix[1][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "1.0-1.5":
                    prob = prob * self.transitionMatrix[1][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "1.0-2.0":
                    prob = prob * self.transitionMatrix[1][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "1.0-2.5":
                    prob = prob * self.transitionMatrix[1][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "1.0-3.0":
                    prob = prob * self.transitionMatrix[1][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                elif change == "1.0-3.5":
                    prob = prob * self.transitionMatrix[1][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "1.0-4.0"
                    prob = prob * self.transitionMatrix[1][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "1.5":
                change = np.random.choice(self.transitionName[2],replace=True,p=self.transitionMatrix[2])
                if change == "1.5-1.5":
                    prob = prob * self.transitionMatrix[2][2]
                    noteSequence.append("1.5")
                    pass
                elif change == "1.5-0.5":
                    prob = prob * self.transitionMatrix[2][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "1.5-1.0":
                    prob = prob * self.transitionMatrix[2][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "1.5-2.0":
                    prob = prob * self.transitionMatrix[2][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "1.5-2.5":
                    prob = prob * self.transitionMatrix[2][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "1.5-3.0":
                    prob = prob * self.transitionMatrix[2][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                elif change == "1.5-3.5":
                    prob = prob * self.transitionMatrix[2][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "1.5-4.0"
                    prob = prob * self.transitionMatrix[2][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "2.0":
                change = np.random.choice(self.transitionName[3],replace=True,p=self.transitionMatrix[3])
                if change == "2.0-2.0":
                    prob = prob * self.transitionMatrix[3][3]
                    noteSequence.append("2.0")
                    pass
                elif change == "2.0-0.5":
                    prob = prob * self.transitionMatrix[3][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "2.0-1.0":
                    prob = prob * self.transitionMatrix[3][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "2.0-1.5":
                    prob = prob * self.transitionMatrix[3][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "2.0-2.5":
                    prob = prob * self.transitionMatrix[3][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "2.0-3.0":
                    prob = prob * self.transitionMatrix[3][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                elif change == "2.0-3.5":
                    prob = prob * self.transitionMatrix[3][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "2.0-4.0"
                    prob = prob * self.transitionMatrix[3][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "2.5":
                change = np.random.choice(self.transitionName[4],replace=True,p=self.transitionMatrix[4])
                if change == "2.5-2.5":
                    prob = prob * self.transitionMatrix[4][4]
                    noteSequence.append("2.5")
                    pass
                elif change == "2.5-0.5":
                    prob = prob * self.transitionMatrix[4][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "2.5-1.0":
                    prob = prob * self.transitionMatrix[4][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "2.5-1.5":
                    prob = prob * self.transitionMatrix[4][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "2.5-2.0":
                    prob = prob * self.transitionMatrix[4][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "2.5-3.0":
                    prob = prob * self.transitionMatrix[4][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                elif change == "2.5-3.5":
                    prob = prob * self.transitionMatrix[4][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "2.5-4.0"
                    prob = prob * self.transitionMatrix[4][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "3.0":
                change = np.random.choice(self.transitionName[5],replace=True,p=self.transitionMatrix[5])
                if change == "3.0-3.0":
                    prob = prob * self.transitionMatrix[5][5]
                    noteSequence.append("3.0")
                    pass
                elif change == "3.0-0.5":
                    prob = prob * self.transitionMatrix[5][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "3.0-1.0":
                    prob = prob * self.transitionMatrix[5][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "3.0-1.5":
                    prob = prob * self.transitionMatrix[5][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "3.0-2.0":
                    prob = prob * self.transitionMatrix[5][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "3.0-2.5":
                    prob = prob * self.transitionMatrix[5][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "3.0-3.5":
                    prob = prob * self.transitionMatrix[5][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
                else:   # "3.0-4.0"
                    prob = prob * self.transitionMatrix[5][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "3.5":
                change = np.random.choice(self.transitionName[6],replace=True,p=self.transitionMatrix[6])
                if change == "3.5-3.5":
                    prob = prob * self.transitionMatrix[6][6]
                    noteSequence.append("3.5")
                    pass
                elif change == "3.5-0.5":
                    prob = prob * self.transitionMatrix[6][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "3.5-1.0":
                    prob = prob * self.transitionMatrix[6][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "3.5-1.5":
                    prob = prob * self.transitionMatrix[6][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "3.5-2.0":
                    prob = prob * self.transitionMatrix[6][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "3.5-2.5":
                    prob = prob * self.transitionMatrix[6][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "3.5-3.0":
                    prob = prob * self.transitionMatrix[6][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                else:   # "3.5-4.0"
                    prob = prob * self.transitionMatrix[6][7]
                    startState = "4.0"
                    noteSequence.append("4.0")
            elif startState == "4.0":
                change = np.random.choice(self.transitionName[7],replace=True,p=self.transitionMatrix[7])
                if change == "4.0-4.0":
                    prob = prob * self.transitionMatrix[7][7]
                    noteSequence.append("4.0")
                    pass
                elif change == "4.0-0.5":
                    prob = prob * self.transitionMatrix[7][0]
                    startState = "0.5"
                    noteSequence.append("0.5")
                elif change == "4.0-1.0":
                    prob = prob * self.transitionMatrix[7][1]
                    startState = "1.0"
                    noteSequence.append("1.0")
                elif change == "4.0-1.5":
                    prob = prob * self.transitionMatrix[7][2]
                    startState = "1.5"
                    noteSequence.append("1.5")
                elif change == "4.0-2.0":
                    prob = prob * self.transitionMatrix[7][3]
                    startState = "2.0"
                    noteSequence.append("2.0")
                elif change == "4.0-2.5":
                    prob = prob * self.transitionMatrix[7][4]
                    startState = "2.5"
                    noteSequence.append("2.5")
                elif change == "4.0-3.0":
                    prob = prob * self.transitionMatrix[7][5]
                    startState = "3.0"
                    noteSequence.append("3.0")
                else:   # "4.0-3.5"
                    prob = prob * self.transitionMatrix[7][6]
                    startState = "3.5"
                    noteSequence.append("3.5")
            i += 1    
        # return noteSequence
        return float(noteSequence[1])  # return next state name

def initializeMarkovChain():
    # States are quarter-length note durations (ex. 0.5 = eighth-note, 1.0 = quarter-note)
    states = ["0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0"]
    
    # Possible sequences of events
    transitionName = [  ["0.5-0.5","0.5-1.0","0.5-1.5","0.5-2.0","0.5-2.5","0.5-3.0","0.5-3.5","0.5-4.0"],
                        ["1.0-0.5","1.0-1.0","1.0-1.5","1.0-2.0","1.0-2.5","1.0-3.0","1.0-3.5","1.0-4.0"],
                        ["1.5-0.5","1.5-1.0","1.5-1.5","1.5-2.0","1.5-2.5","1.5-3.0","1.5-3.5","1.5-4.0"],
                        ["2.0-0.5","2.0-1.0","2.0-1.5","2.0-2.0","2.0-2.5","2.0-3.0","2.0-3.5","2.0-4.0"],
                        ["2.5-0.5","2.5-1.0","2.5-1.5","2.5-2.0","2.5-2.5","2.5-3.0","2.5-3.5","2.5-4.0"],
                        ["3.0-0.5","3.0-1.0","3.0-1.5","3.0-2.0","3.0-2.5","3.0-3.0","3.0-3.5","3.0-4.0"],
                        ["3.5-0.5","3.5-1.0","3.5-1.5","3.5-2.0","3.5-2.5","3.5-3.0","3.5-3.5","3.5-4.0"],
                        ["4.0-0.5","4.0-1.0","4.0-1.5","4.0-2.0","4.0-2.5","4.0-3.0","4.0-3.5","4.0-4.0"]]

    # Probabilities matrix (transition matrix)
                        # .5   1  1.5     2   2.5    3   3.5    4
    transitionMatrix = [[.30, .25,.28,   .11,.02,   .01,.01,   .02],    # .5
                        [.24, .23,.25,   .13,.005,  .02,.005,  .12],    # 1
                        [.36, .25,.21,   .105,.05,  .01,.005,  .01],    # 1.5
                        [.39, .34,.20,   .02,.018,  .015,.008, .009],   # 2
                        [.55, .178,.255, .005,.005, .003,.002, .002],   # 2.5
                        [.31, .40,.15,   .05,.02,   .02,.02,   .03],    # 3
                        [.51, .24,.21,   .02,.01,   .003,.003, .004],  # 3.5
                        [.30, .33,.326,  .02,.01,   .004,.001, .009]]   # 4

    # if sum(transitionMatrix[0])!=1 or sum(transitionMatrix[1])!=1 or sum(transitionMatrix[2])!=1 or sum(transitionMatrix[3])!=1 or sum(transitionMatrix[4])!=1 or sum(transitionMatrix[5])!=1 or sum(transitionMatrix[6])!=1 or sum(transitionMatrix[7])!=1:
        # print("Transition matrix row doesn't add to 1...?")

    # for x in range(0,8):
    #     print(sum(transitionMatrix[x]))

    m = Markov(states, transitionName, transitionMatrix)
    # # To save every noteSequence
    # list_sequence = []
    # count = 0
    # startNoteDuration = "3.5"
    # for iterations in range(1,10000):
            # print(m.note_forecast(1, startNoteDuration))
            # list_sequence.append(m.note_forecast(1, startNoteDuration))
    # print(m.note_forecast(1, startNoteDuration))

    # nextNoteDuration = "4.0"
    # # Iterate through the list to get a count of all states ending in given end state
    # for smaller_list in list_sequence:
    #     if(smaller_list[1] == nextNoteDuration):
    #         count += 1
    # print(count)
    
    # Calculate the probability of starting from given start state and ending at given end state:
    # percentage = (count/10000) * 100
    # print("The probability of starting at state:{0} and ending at state:{1}= ".format(startNoteDuration, nextNoteDuration) + str(percentage) + "%")
    return m

if __name__ == "__main__":
    initializeMarkovChain()
import numpy as np
import Graph
import Traveler
import itertools
class RecSys:
    def __init__(self, ttWeight):
        self.ttWeight = ttWeight
        self.psi = [[1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0]]
    # converts a number n to b-ary representation. 
    # def numberToBase(n, m):
    #     if n == 0:
    #         return [0]
    #     digits = []
    #     while n:
    #         digits.append(int(n % m))
    #         n //= m
    #     return digits[::-1]


    # def muPossibleSignals(maxTravelers, edges):
    #     prob_values = [0, 0.25, 0.5, 0.75, 1]
    #     recSysSignal = []
    #     for i in range(5**maxTravelers):
    #         arr =  [0]*maxTravelers
    #         Num_Base = RecSys.numberToBase(i, 5)
    #         reverse_Num_Base = [i for i in reversed(Num_Base)]
    #         for x in reverse_Num_Base:
    #             arr[-1 -reverse_Num_Base.index(x)] = arr[-1 -reverse_Num_Base.index(x)] + prob_values[x]
    #         if sum(arr) == 1:
    #             recSysSignal.append(arr)
    #     # muPossibleSignals = list(itertools.combinations(recSysSignal, edges))
    #     return recSysSignal

    def networkStateFromPsi(self, psi):
        
        networkState = []
        for i in psi:
            networkState.append(i.index(max(i)))
        return networkState
   

    # def psiTransition(self, totalTravelers):
    #     if totalTravelers == 0:
    #         pass
    #     else: 
    #         for 
        

    def y(self, networkState):
        cost = 0
        # for e in Graph.graph.edgeState:
        #     if Graph.graph.edgeState[e][0] == "car":
        #         cost = self.ttWeight*(max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1])) + (1 - self.ttWeight)*(max(Graph.graph.CO(e, networkState), Graph.graph.edgeState[e][1]))
        #     elif Graph.graph.edgeState[e][0] == "train":
        #         cost += self.ttWeight*(Graph.graph.edgeState[e][1]) + (1 - self.ttWeight)*(0.5*Graph.graph.edgeState[e][1])
        #     elif Graph.graph.edgeState[e][0] == "walk":
        #         cost += self.ttWeight*(Graph.graph.edgeState[e][1])
        #     elif Graph.graph.edgeState[e][0] == "switch":
        #         cost += 1

        for e in range(15089):
            bpr = max(Graph.graph.BPR(e, networkState), Graph.graph.flow(e))
            CO = max(Graph.graph.CO(e, networkState), Graph.graph.flow(e))
            cost += self.ttWeight*(bpr)+ (1 - self.ttWeight)*(CO)
        return cost

System = RecSys(1)
# print(System.y(Graph.graph.networkState))
import cvxpy as cp
import Game
import Graph
import numpy
import time
from timeit import default_timer as timer

noOfEdges = 15089
maxTravelers = 10
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.d, 0.5)
# traveler1 = Game.game.addTraveler(1, int(time.time()), Graph.graph.b, Graph.graph.b, 0.8)
# traveler2 = Game.game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.6)
# traveler2 = Game.game.addTraveler(2, int(time.time()), [1], [3], 0.7)
# travelTimeDict = {}

# def activeInactive():
#     for t in range(int(time.time()), int(time.time())+100):
#         print(Game.game.Travelers)
#         for i in Game.game.Travelers:
#            if i.state[0]==1:
#                Game.game.activeTravelers.append(i)
#         # travelTimeDict = {}
#         print(Game.game.activeTravelers)
#         for activeTraveler in Game.game.activeTravelers:
#             signal = optimalSignal(activeTraveler)
#             print(optimalSignal)
#             activeTravelerPath = Game.game.chosenPath(signal, activeTraveler)
#             print(activeTravelerPath)
#             activeTraveler.state[0] = 0
#             activeTraveler.state[1] = activeTravelerPath
#             if activeTraveler.state[2] == None:
#                 activeTraveler.state[2] = activeTravelerPath[0]
#                 Graph.graph.networkState[activeTraveler.state[2]] += 1
#             else: 
#                 Graph.graph.networkState[activeTraveler.state[2]] -= 1
#                 activeTraveler.state[2] = activeTravelerPath[0]
#                 Graph.graph.networkState[activeTraveler.state[2]] += 1
#             print(activeTraveler.state)
#             travelTime = t + Graph.graph.edgeTravelTime(activeTraveler.state[2], Graph.graph.networkState)
#             travelTimeDict[activeTraveler] = travelTime
#             Game.game.activeTravelers.remove(activeTraveler)
#         for traveler in (travelTimeDict): 
#             if t > travelTimeDict[traveler]:
#                 traveler.state[0] = 1
#                 traveler.state[2] = traveler.state[1][1] 
#                 if traveler.state[2] in Graph.graph.a:
#                     traveler.origin = Graph.graph.a
#                 elif traveler.state[2] in Graph.graph.b:
#                     traveler.origin = Graph.graph.b
#                 elif traveler.state[2] in Graph.graph.c:
#                     traveler.origin = Graph.graph.c
#                 elif traveler.state[2] in Graph.graph.d:
#                     traveler.origin = Graph.graph.d
#                 travelTimeDict.pop(traveler)
#                 print(traveler.origin)

def optimalSignal(traveler):
    start = timer()
    variable = cp.Variable((noOfEdges, maxTravelers))
    constraints = [  
    variable @ numpy.ones((maxTravelers,1)) == numpy.ones((noOfEdges, 1)),
    variable >= 0,
    variable <= 1]
    
    # def zL(L):
    #     zL = numpy.zeros((L+1, 1))
    #     for i in range(L+1):
    #         zL[i][0] += i
    #     return zL


    # variable @ zL(maxTravelers) == maxTravelers]
    # for i in range(noOfEdges):
    #     for j in range(maxTravelers):                                       
    #         constraints += [variable[i][j] >= 0.0]
    #         constraints += [variable[i][j] <= 1.0]
    
    objective = cp.Minimize(systemCost(variable, traveler))
   
    prob = cp.Problem(objective, constraints)
    prob.solve()
    end = timer()
    # print("Time to run optimalSignal is " + str(end -start))
    # print("\n")
    return variable.value


def systemCost(variable, traveler):
    start = timer()
    priorPhi = traveler.priorBeliefs(noOfEdges, maxTravelers)
    # print(priorPhi)
    # priorPhi = traveler.state[3].copy()
    # posteriorPhiTraveler0 = Game.game.traveler0.posteriorBeliefPhi(variable, priorPhiTraveler0)
    
    posteriorBelief = []
    for i in range(len(priorPhi)):
        unNormalizedPosterior = cp.multiply(priorPhi[i], variable[i])
        posterior = unNormalizedPosterior / cp.sum(unNormalizedPosterior)
        posteriorBelief.append(posterior)
    # print(len(posteriorBelief))
    # print(posteriorBelief)
    # print(len(posteriorBelief))
    networkStateTraveler = []

    for i in range(len(posteriorBelief)):
        temp = cp.max(posteriorBelief[i])
        networkStateTraveler.append(temp)
    # print(len(networkStateTraveler0))
    # networkStateTraveler0 = Game.game.traveler0.networkStateFromPhi(posteriorBelief)
    # print(networkStateTraveler)
    # costTraveler = Game.game.travelerCostMatrix(traveler, networkStateTraveler)
    # # print(costTraveler)
    # costMatrices = []
    # costMatrices.append(costTraveler)
    # # print(costMatrices)
    # tempList = [x for x in Game.game.activeTravelers if x != Game.game.dummy]
    # if len(tempList) == 1: 
    #         tempList.append(Game.game.dummy)
    # for activeTraveler in tempList:
    #     if activeTraveler != traveler:
    #         cost = Game.game.travelerCostMatrix(activeTraveler, Graph.graph.networkState)
    #     # costTraveler2 = Game.game.travelerCostMatrix(Game.game.traveler2, Graph.graph.networkState)
    #         costMatrices.append(cost)
    # print(costMatrices)
    if Game.game.activeTravelers == 1: 
        costMatrices = Game.game.travelerCostMatrix1(traveler, networkStateTraveler)
        # print("The cost matrix of traveler " + str(traveler.id) + "is \n")
        # print("only one active traveler")
        # print(costMatrices)
    else: 
        # print("More than one active traveler")
        costMatrices = []
        costTraveler = Game.game.travelerCostMatrix2(traveler, networkStateTraveler)
        if costTraveler == None:
            path = Game.game.chosen_path_single_traveler(traveler)
            return Game.game.system_cost_single_traveler(traveler, path)
        costMatrices.append(costTraveler)
        tempList = [x for x in Game.game.activeTravelers if x != Game.game.dummy]
        if len(tempList) == 1: 
                tempList.append(Game.game.dummy)
        for activeTraveler in tempList:
            if activeTraveler != traveler:
                cost = Game.game.travelerCostMatrix2(activeTraveler, Graph.graph.networkState)
                if cost == None:
                    path = Game.game.chosen_path_single_traveler(traveler)
                    return Game.game.system_cost_single_traveler(traveler, path)
            # costTraveler2 = Game.game.travelerCostMatrix(Game.game.traveler2, Graph.graph.networkState)
                costMatrices.append(cost)
        # print("The cost matrix of traveler " + str(traveler.id) + "with \n" + str(len(costMatrices)) + "number of path choices and \n" + str(len(costMatrices[0]))+ "number of possible strategies across all the other" + str(len(Game.game.activeTravelers) - 1) + "active travelers")
        # print(costMatrices)

    paddedCosts = Game.game.padding(costMatrices)
    # print(paddedCosts)
    QREProb = Game.game.QRE(paddedCosts)
    # print("The QRE for traveler" + str(traveler.id) + "is" + str(QREProb))
    QRESlicced = Game.game.QRESlicing(len(paddedCosts[0]), QREProb)
    
    # print(QRESlicced)
    systemCost = Game.game.systemCost(traveler, QRESlicced)
    # print("The system cost is " + str(systemCost))
    end = timer()
    # print("Time to run systemCost is" + str(end - start))
    # print("\n")
    return systemCost

# activeInactive()


# print(optimalSignal(traveler2))


# print(variable.value)
# print(prob.value)


# print(prob.value)

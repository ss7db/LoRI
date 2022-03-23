import itertools
from operator import add
import pygambit
import Traveler
import Graph
import time
import numpy
import RecSys
import cvxpy
import math
from timeit import default_timer as timer

class Game():
    def __init__(self):
        self.Travelers = []
        self.activeTravelers = []
        self.dummy = Game.addTraveler(self, 999, 1, Graph.graph.a, Graph.graph.a, 0.5)
        self.dummy.state[0] = 0
        # self.traveler1 = Game.addTraveler(self,1,1, Graph.graph.b, Graph.graph.d, 0.8)
        # self.traveler2 = Game.addTraveler(self,1, Graph.graph.a, Graph.graph.d, 0.6)

    def addTraveler(self, id, t, origin, destination, ttWeight):
        traveler = Traveler.Traveler(id, t, origin, destination, ttWeight)
        self.Travelers.append(traveler)
        # self.activeTravelers.append(traveler)
        return traveler

    # def travelersPredictedCost(self, traveler):
    #     t = time.time()
    #     networkState = [x for x in Graph.graph.networkState]
    #     for traveler in Graph.graph.activeTravelers: 
    #         travelerState = traveler.state
    #         for path in travelerState[4]:
    #             for i in range(len(path)-1):
    #                 e = Graph.graph.graph.get_eid(path[i], path[i+1])
    #                 travelerState[1] = e
    #                 networkState[e] += 1
    #                 if Graph.graph.graph.edgeState[e][0] == "switch":
    #                     travelerState[5] = 1
    #                 elif Graph.graph.graph.edgeState[e][0] == "train":
    #                     travelerState[5] = Graph.graph.graph.edgeState[e][1]
    #                 elif Graph.graph.graph.edgeState[e][0] == "walk":
    #                     travelerState[5] = Graph.graph.graph.edgeState[e][1]
    #                 elif Graph.graph.graph.edgeState[e][0] == "car":
    #                     travelerState[5] = Graph.graph.graph.BPR(e)
                
    def predictedLocation(self, t, path, networkState):
        dic = {}
        for i in range(len(path)-1):
            e = Graph.graph.graph.get_eid(path[i], path[i+1])
            dic[e] = t + Graph.graph.edgeTravelTime(e, networkState)
        return dic

    def strategyProfiles(self, traveler):
        start = timer()
        l = [x for x in self.activeTravelers if x != traveler]

        row_traveler_incidence = []

        if traveler.state[1] == None:
            row_traveler_incidence = []
        else:
            row_traveler_incidence = Graph.graph.graph.incident(traveler.state[1][1])
        

        travelers_incident_with_row_traveler = []
        for i in l:

            if i.state[1] == None: 
                pass
            elif len(set(row_traveler_incidence).intersection(Graph.graph.graph.incident(i.state[1][1]))) != 0:
                travelers_incident_with_row_traveler.append(i)
        
        temp = []
        for i in travelers_incident_with_row_traveler:
            temp.append(i.top3Paths())
        end = timer()

        return list(itertools.product(*temp))

    # def strategyProfilesTop3(self, traveler):
    #     start = timer()
    #     l = [x for x in self.activeTravelers if x != traveler]
    #     # l.remove(traveler)
    #     temp = []
    #     for i in l:
    #         travelerAllPaths = []
    #         travelerAllPaths.append(i.top3Paths())
    #         pathCost = []
    #         for path in travelerAllPaths:
    #             print(path)
    #             j = i.pathCostsGivenPath(path, Graph.graph.networkState)
    #             pathCost.append(j)
    #         x = sorted(zip(pathCost, travelerAllPaths))[:3]
    #         y = [z[1] for z in x]
    #         temp.append(y)
    #     end = timer()
    #     print("Time to run strategyProfiles is " + str(end - start))
    #     print("\n")
    #     return list(itertools.product(*temp))

    def locationPredictionForProfile(self, networkState, Profile):
        start = timer()
        l = []
        for path in Profile:
            dic = Game.predictedLocation(self, int(time.time()), path , networkState)
            l.append(dic)
        end = timer()
        # print("Time to run locationPredictionForProfile is " + str(end - start))
        # print("\n")
        return l

    def locationPredictionForAllStrategies(self, networkState, strategyProfiles):
        start = timer()
        temp = []
        for profile in strategyProfiles:
            l = Game.locationPredictionForProfile(self, networkState, profile)
            temp.append(l)
        end = timer()

        return temp

    def networkStateIncDcrBasedOnProfile(self, profile):
        start = timer()
        l = []
        dic = {}
        for pathDic in profile: 
            keyList = Game.dicKeys(self, pathDic)
            n = [0]*15089
            n[keyList[0]] += 1
            dic[int(time.time())] = n
            for j in range(len(keyList)):
                if j < len(keyList)-1: 
                    networkState = [0]*15089
                    networkState[keyList[j]] -= 1
                    networkState[keyList[j+1]] += 1
                    dic[pathDic[keyList[j]]] = networkState
                elif j == len(keyList)-1:
                    networkState = [0]*15089
                    networkState[keyList[j]] -= 1
                    dic[pathDic[keyList[j]]] = networkState    
            l.append(dic)
        end = timer()
        # print("Time to run networkStateIncrDcr is " + str(end - start))  
        # print("\n")
        return l
    
    # def allStrategyBasedNetworkState(self, traveler):
    #     networkState = [i for i in Graph.graph.networkState]
    #     for i in traveler.top3Paths():
    #         strategyProfile = Game.strategyProfile(self, self.Travelers[0])
    #         for i in strategyProfile:

    def networkStateAtTimeIntervalsForProfile(self ,incDcr):
        start = timer()
        dic = {}
        networkState = [i for i in Graph.graph.networkState]
        l = []
        for i in incDcr:
            for key in i:
                networkState = list(map(add, networkState, i[key]))
                dic[key] = networkState
            l.append(dic)
        end = timer()
        # print("Time to run netwrokStateAtTimeIntervals is " + str(end - start))
        # print("\n")
        return l
    
    def networkStateGivenTime(self, t, dic):
        tt = t
        keyList = Game.dicKeys(self, dic)
        for i in range(len(keyList)):
            if tt >= int(keyList[i]- 10):
                if tt <= int(keyList[i]+10):
                    return dic[keyList[i]]
            else: 
                return dic[keyList[-1]]
    
    # def networkStateGivenTime(self, t, dic):
    #     tt = t
    #     keyList = Game.dicKeys(self, dic)
    #     temp = [x for x in keyList]
    #     for i in range(len(temp)):
    #         if tt >= int(temp[i]- 10):
    #             if tt <= int(temp[i]+10):
    #                 return dic[temp[i]]
    #         else: 
    #             return dic[temp[-1]]
    
    def travelerCostMatrix1(self, traveler, networkState):
        # print(self.activeTravelers) 
            costMatrix = []
            # print(len(traveler.top3Paths())) 
            for path in traveler.top3Paths():
                print(path)
                costList = []
                cost = 0
                for i in range(len(path)-1):
                    # print(i)
                    if i == 0:
                        e = Graph.graph.graph.get_eid(path[i], path[i+1])
                        # print(e)
                        cost += traveler.edgeCost(e, networkState)
                        # print("cost for edge", e, cost)
                    else: 
                        e = Graph.graph.graph.get_eid(path[i], path[i+1])
                        cost += traveler.edgeCost(e, networkState)
                        # print("cost for edge", e, cost)
                        # cost += traveler.edgeCost(e, dic[keyList[-1]])
                cost = int(cost)*100
                # cost = int(cvxpy.multiply(cost, 100))
                # print(cost)
                costList.append([cost])
                # print(costList)
                costMatrix.append(costList)
            dummyPlayer = [[0]]
            costMatrix.append(dummyPlayer)
            # print(costMatrix)
            return costMatrix

    def travelerCostMatrix2(self, traveler, networkState):
        start = timer()
        costMatrix = []
        t = int(time.time())
        strategyProfiles = Game.strategyProfiles(self, traveler)
        # print(strategyProfiles)
        # predictedLocationsForAllStrategies = Game.locationPredictionForAllStrategies(self, networkState,strategyProfiles)
        for path in traveler.top3Paths():
            costList = []
            travelerLocation = Game.predictedLocation(self, t, path, networkState)
            for i in range(len(strategyProfiles)):
                cost = 0
                predictedLocationsForProfile = Game.locationPredictionForProfile(self, networkState, strategyProfiles[i])
                incDcr = Game.networkStateIncDcrBasedOnProfile(self, predictedLocationsForProfile)
                network = Game.networkStateAtTimeIntervalsForProfile(self, incDcr)
                for dic in network:
                    keyList = Game.dicKeys(self, dic)
                    for i in range(len(path)-1):
                        if i == 0:
                            e = Graph.graph.graph.get_eid(path[i], path[i+1])
                            cost += traveler.edgeCost(e, dic[keyList[i]])
                        else: 
                            e = Graph.graph.graph.get_eid(path[i], path[i+1])
                            # cost += traveler.edgeCost(e, Game.networkStateGivenTime(self, travelerLocation[e], dic))
                            cost += traveler.edgeCost(e, dic[keyList[-1]])
                cost = int(cost*100)
                # print(cost)
                costList.append(cost)
                # print(costList)
            costMatrix.append(costList)
            end = timer()
            # print("Time to run travelerCostMatrix2 is " + str(end - start))
            # print("\n")
            # print(costMatrix)
        return costMatrix

    # def costTensor(self, networkState):


    def travelerCostMatrix1forCP(self, traveler, networkState):
        # print(self.activeTravelers) 
            costMatrix = []
            # print(len(traveler.top3Paths())) 
            for path in traveler.top3Paths():
                # print(path)
                costList = []
                cost = 0
                for i in range(len(path)-1):
                    # print(i)
                    if i == 0:
                        e = Graph.graph.graph.get_eid(path[i], path[i+1])
                        # print(e)
                        cost += traveler.edgeCost(e, networkState)
                        # print("cost for edge", e, cost)
                    else: 
                        e = Graph.graph.graph.get_eid(path[i], path[i+1])
                        cost += traveler.edgeCost(e, networkState)
                        # print("cost for edge", e, cost)
                        # cost += traveler.edgeCost(e, dic[keyList[-1]])
                cost = int(cost)*100
                # cost = int(cvxpy.multiply(cost, 100))
                # print(cost)
                costList.append([cost])
                # print(costList)
                costMatrix.append(costList)
            dummyPlayer = [[0]]
            costMatrix.append(dummyPlayer)
            # print(costMatrix)
            return costMatrix

    def travelerCostMatrix2forCP(self, traveler, networkState):
        costMatrix = []
        t = int(time.time())
        strategyProfiles = Game.strategyProfiles(self, traveler)
        # predictedLocationsForAllStrategies = Game.locationPredictionForAllStrategies(self, networkState,strategyProfiles)
        for path in traveler.top3Paths():
            costList = []
            travelerLocation = Game.predictedLocation(self, t, path, networkState)
            for i in range(len(strategyProfiles)):
                cost = 0
                predictedLocationsForProfile = Game.locationPredictionForProfile(self, networkState, strategyProfiles[i])
                incDcr = Game.networkStateIncDcrBasedOnProfile(self, predictedLocationsForProfile)
                network = Game.networkStateAtTimeIntervalsForProfile(self, incDcr)
                for dic in network:
                    keyList = Game.dicKeys(self, dic)
                    for i in range(len(path)-1):
                        if i == 0:
                            e = Graph.graph.graph.get_eid(path[i], path[i+1])
                            cost += traveler.edgeCost(e, dic[keyList[i]])
                            print(cost)
                        else: 
                            e = Graph.graph.graph.get_eid(path[i], path[i+1])
                            # cost += traveler.edgeCost(e, Game.networkStateGivenTime(self, travelerLocation[e], dic))
                            cost += traveler.edgeCost(e, dic[keyList[-1]])
                            print(cost)
                # print(cost)
                cost = int(cost*100)
                # print(cost)
                costList.append(cost)
                # print(costList)
            costMatrix.append(costList)
            # print(costMatrix)
        return costMatrix

    def padding(self, costMatrices):
        maxColumn =  max(list(map(lambda x:len(x), costMatrices)))
        maxRow = max(list(map(lambda x:len(x[0]), costMatrices)))
        for matrix in costMatrices:
            if len(matrix) < maxColumn:
               z = [0]*maxRow
               matrix.extend([z]*(maxColumn - len(matrix)))

            if len(matrix[0]) < maxRow:
                temp = maxRow - len(matrix[0])
                for l in matrix:
                    l.extend([0]*temp)
        
        return costMatrices
             


    def QRE(self, costMatrices):
        start = timer()
        payoff = []
        for i in costMatrices:
            payoff.append(numpy.array(i, dtype=pygambit.Rational))
            # print(payoff)
            # print(*payoff)
        g = pygambit.Game.from_arrays(*payoff)
        solver = pygambit.nash.ExternalLogitSolver()
        x = solver.solve(g)
        end = timer()
        # print("Time to compute QRE is" + str(end - start))
        return x
        # with open("mainGame.nfg", "w") as f:
        #     f.write(g.write('nfg'))

    def dicKeys(self, dic):
        temp = []
        for key in dic:
            temp.append(key)
        return temp

    def QRESlicing(self, padLen, QRE):
        l = [x for x in QRE[0]]
        temp = []
        for i in range(len(self.activeTravelers)):
            temp.append(l[(padLen*i):(padLen*(i+1))])
        return temp

    def systemCost(self, traveler, QRESliced):
        cost = 0
        pathIndex = QRESliced[self.activeTravelers.index(traveler)].index(max(QRESliced[self.activeTravelers.index(traveler)]))
        path = traveler.top3Paths()[pathIndex]
        travelerLocation = Game.predictedLocation(self, int(time.time()), path, Graph.graph.networkState)
        l = []
        l.append(travelerLocation)
        incDcr = Game.networkStateIncDcrBasedOnProfile(self, l)
        network = Game.networkStateAtTimeIntervalsForProfile(self, incDcr)
        for dic in network:
            keyList = Game.dicKeys(self, dic)
            for i in range(len(path)-1):
                if i == 0:
                    e = Graph.graph.graph.get_eid(path[i], path[i+1])
                    cost += RecSys.System.y(dic[keyList[i]])
                else: 
                    e = Graph.graph.graph.get_eid(path[i], path[i+1])
                    cost += RecSys.System.y(Game.networkStateGivenTime(self, travelerLocation[e], dic))
        return cost

    def chosenPath(self, mu, traveler):
        priorPhi = traveler.priorBeliefs(15089,10)
        # posteriorPhiTraveler0 = Game.game.traveler0.posteriorBeliefPhi(variable, priorPhiTraveler0)
        
        posteriorBelief = traveler.posteriorBeliefPhi(mu, priorPhi)
        # print(len(posteriorBelief))
        networkStateTraveler = traveler.networkStateFromPhi(posteriorBelief)
        # print(len(networkStateTraveler0))
        # networkStateTraveler0 = Game.game.traveler0.networkStateFromPhi(posteriorBelief)
        
        if self.activeTravelers == 1: 
            costMatrices = self.travelerCostMatrix1forCP(traveler, networkStateTraveler)
        else: 
            costMatrices = []
            costTraveler = self.travelerCostMatrix2forCP(traveler, networkStateTraveler)
            costMatrices.append(costTraveler)
            tempList = [x for x in self.activeTravelers if x != self.dummy]
            if len(tempList) == 1: 
                    tempList.append(self.dummy)
            for activeTraveler in tempList:
                if activeTraveler != traveler:
                    cost = self.travelerCostMatrix2forCP(activeTraveler, Graph.graph.networkState)
                # costTraveler2 = Game.game.travelerCostMatrix(Game.game.traveler2, Graph.graph.networkState)
                    costMatrices.append(cost)
        
        paddedCosts = self.padding(costMatrices)
        QREProb = self.QRE(paddedCosts)
        QRESlicced = self.QRESlicing(len(paddedCosts[0]), QREProb)
        pathIndex = QRESlicced[self.activeTravelers.index(traveler)].index(max(QRESlicced[self.activeTravelers.index(traveler)]))
        # systemCost = Game.game.systemCost(traveler, QRESlicced)
        return traveler.top3Paths()[pathIndex]
        
    # def gamePreprocessing(self):
    # def piList(self, filepath):
        # f = open("mainGame.nfg","r")
        # filedata = f.read()
        # f.close()

        # filedata = filedata.replace(r"\n", "\n")
        # filedata = filedata.replace("b", "")
        # filedata = filedata.replace("'", "")

        # f = open("mainGameProcessed","w+")
        # f.write(filedata)
        # f.close()
    
    # def piList(self):
    #     lastLine = []
    #     with open("mainGameProcessed", "rb") as f:
    #         for line in f:
    #             pass
    #     lastLine.append(line.rstrip())
    #     lastLine.remove(lastLine[0])
    #     return lastLine
            

game = Game()
# print(game.dummy.state)

# x = game.travelerCostMatrix(game.traveler0, Graph.graph.networkState)
# y = game.padding(x)
# print("padded", y)
# print("QRE", game.QRE(y))


# strategyProfiles = game.strategyProfiles(game.traveler0)
# for profile in strategyProfiles: 
#     profileLocation = game.locationPredictionForProfile(Graph.graph.networkState, profile)
#     incDcr = game.networkStateIncDcrBasedOnProfile(profileLocation)
#     print(profileLocation)
#     print(incDcr)
#     # predictedLocationsForAllStrategies = game.locationPredictionForAllStrategies(Graph.graph.networkState, strategyProfiles)
#     travelerLocation = game.predictedLocation(int(time.time()), traveler0.top3Paths()[0], Graph.graph.networkState)
    
#     network = game.networkStateAtTimeIntervalsForProfile(incDcr)
#     cost = 0
#     path = traveler0.top3Paths()[0]
#     for dic in network:
#         keyList = [*dic.keys()]
#         for i in range(len(path)-1):
#             if i == 0:
#                 # nS = [x for x in network[keyList[i]]]
#                 e = Graph.graph.graph.get_eid(path[i], path[i+1])
#                 cost += traveler0.edgeCost(e, dic[keyList[i]])
#             else: 
#                 e = Graph.graph.graph.get_eid(path[i], path[i+1])
#                 cost += traveler0.edgeCost(e, game.networkStateGivenTime(travelerLocation[e], dic))
#     print(cost)





# for i in range(len(strategyProfiles)):
#     # incDcr = game.networkStateIncDcrBasedOnProfile(predictedLocationsForAllStrategies[i])
#     # print(incDcr)
#     print(strategyProfiles[i])
# for i in range(len(predictedLocationsForAllStrategies)):
#     print(predictedLocationsForAllStrategies[i])
# print(predictedLocationsForAllStrategies)
# print(len(strategyProfiles), len(predictedLocationsForAllStrategies))
# # network = game.networkStateAtTimeIntervalsForProfile(incDcr)

# print([*predictedLocationsForAllStrategies[5].keys()][0])

# print(traveler0.top3Paths()[0])# print(range(len(traveler0.top3Paths()[0])))
# print(len(network))

# x = game.strategyProfiles(traveler0)
# print(len(x), x)
# print(game.activeTravelers, traveler0)
# matrix0 = game.travelerCostMatrix(game.Travelers[0], Graph.graph.networkState)
# print(matrix0)
# matrix1 = game.travelerCostMatrix(game.traveler1, Graph.graph.networkState)
# print(len(matrix0[0]))
# print(len(matrix0))
# print(len(game.traveler0.top3Paths()))
# print(len(matrix1[0]))
# print(len(matrix1))
# print(len(game.traveler1.top3Paths()))
# l = []
# l.append(matrix0)
# l.append(matrix1)
# print(game.padding(l))
# m = game.padding(l)
# print(len(m), len(m[0]), len(m[1]))
# QRE = game.QRE(m)
# QRESlicced = game.QRESlicing(len(m[0]), QRE)
# print(QRE)
# print(QRESlicced)
# x = game.predictedLocation(int(time.time()), game.activeTravelers[0].top3Paths()[0], Graph.graph.networkState)
# l = []
# l.append(x)
# # print(l)
# inc = game.networkStateIncDcrBasedOnProfile(l)
# tim = game.networkStateAtTimeIntervalsForProfile(inc)
# print(tim)
# state = game.networkStateGivenTime(int(time.time()), tim[0])
# # print(state)
# print(game.systemCost(game.traveler1, QRESlicced))
# x = game.traveler0.priorBeliefs(5,7)
# print(game.traveler0.networkStateFromPhi(x))
# print(Graph.graph.graph.vcount())
# p = game.traveler0.priorBeliefs(5,7)
# q = game.traveler0.priorBeliefs(5,7)
# q = game.traveler0.posteriorBeliefPhi(p, p)
# print(game.traveler0.networkStateFromPhi(q))
# print(game.traveler0.posteriorBeliefPhi(p, q))
# print(game.travelerCostMatrix(game.traveler0))
###################################################################################################################
# Analysis to improve the cost matrix structure and reduce computational complexity. 
# traveler0 = game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
# # print(traveler0.top3Paths())
# x = numpy.random.randint(5, size=(10, 800))
# print(x)
# print(game.QRE(x))

# traveler1 = game.addTraveler(1, int(time.time()), [0], [3], 0.6)
# traveler2 = game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.5)
# traveler3 = game.addTraveler(3, int(time.time()), Graph.graph.a, Graph.graph.d, 0.6)
# begin = timer()
# x = game.travelerCostMatrix1forCP(traveler1, Graph.graph.networkState)
# print(x)
# print(traveler1.pathCostsGivenPath(traveler1.top3Paths()[0], Graph.graph.networkState))
# beginnot = timer()
# print("Time to Compute is " + str(beginnot - begin
# x = game.strategyProfiles(traveler1)
# print(traveler1.paths())
# print(x, len(x))
# print(traveler1.top3Paths()())


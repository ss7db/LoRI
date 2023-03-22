import Game
import Graph
import Traveler
import RecSys
import signalOptimization
import time
import numpy

startTime = time.time()

traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
traveler1 = Game.game.addTraveler(1, int(time.time()), Graph.graph.d, Graph.graph.b, 0.6)
traveler2 = Game.game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.5)
traveler3 = Game.game.addTraveler(3, int(time.time()), Graph.graph.a, Graph.graph.d, 0.6)
# traveler4 = Game.game.addTraveler(4, int(time.time()), Graph.graph.b, Graph.graph.d, 0.3)

# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.b, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.c, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.d, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.b, Graph.graph.a, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.b, Graph.graph.c, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.b, Graph.graph.d, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.c, Graph.graph.a, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.c, Graph.graph.b, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.c, Graph.graph.d, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.d, Graph.graph.a, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.d, Graph.graph.b, 0.5)
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.d, Graph.graph.c, 0.5)



travelTimeDict = {}
ti = []
travelerCost = []
labels = []
systemCostList = []
travelerCostDic = {} 

# s = 0
def systemCost(ttWeight, networkState):
    cost = 0
    for e in Graph.graph.edgeState:
        if Graph.graph.edgeState[e][0] == "car":
            cost = ttWeight*(max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1])) + (1 - ttWeight)*(max(Graph.graph.CO(e, networkState), Graph.graph.edgeState[e][1]))
        elif Graph.graph.edgeState[e][0] == "train":
            cost += ttWeight*(Graph.graph.edgeState[e][1]) + (1 - ttWeight)*(0.5*Graph.graph.edgeState[e][1])
        elif Graph.graph.edgeState[e][0] == "walk":
            cost += ttWeight*(Graph.graph.edgeState[e][1])
        elif Graph.graph.edgeState[e][0] == "switch":
            cost += 1
    return cost

def activeInactive(systemTtWeight):
    systemCostList = []
    # k = 0
    # for t in range(int(time.time()), int(time.time())*100):
    for t in range(1, 100):
    
        # print("time", t)
        # y = RecSys.System.y(Graph.graph.networkState)
        # print(Graph.graph.networkState)
        # print(Game.game.Travelers)
        for i in Game.game.Travelers:
           if i.state[0]==1:
            #    if i not in Game.game.activeTravelers:
                Game.game.activeTravelers.append(i)
        # travelTimeDict = {}
        # print("active travelers list", Game.game.activeTravelers)
        tempList = Game.game.activeTravelers.copy()
        # if len(tempList) == 1: 
        #     tempList.append(Game.game.dummy)
        for activeTraveler in tempList:
            print("Active traveler is" + str(activeTraveler.id))
            optimalSignal = signalOptimization.optimalSignal(activeTraveler) 
            print("Optimal Signal for" + str(activeTraveler.id) + "is \n")
            print(optimalSignal)
            activeTravelerPath = Game.game.chosenPath(optimalSignal, activeTraveler)
            print(activeTravelerPath)
            activeTraveler.state[0] = 0
            activeTraveler.state[1] = activeTravelerPath
            if activeTraveler.state[2] == None:
                activeTraveler.state[2] = Graph.graph.graph.get_eid(activeTravelerPath[0], activeTravelerPath[1])
                # print(activeTraveler.state[2])
                Graph.graph.networkState[activeTraveler.state[2]] += 1
                # print(Graph.graph.networkState)
            else: 
                # print(activeTraveler.state[2])
                Graph.graph.networkState[activeTraveler.state[2]] -= 1
                # print(Graph.graph.networkState)
                activeTraveler.state[2] = Graph.graph.graph.get_eid(activeTravelerPath[0], activeTravelerPath[1])
                # print(activeTraveler.state[2])
                Graph.graph.networkState[activeTraveler.state[2]] += 1
                # print(Graph.graph.networkState)
        
            travelTime = t + Graph.graph.edgeTravelTime(activeTraveler.state[2], Graph.graph.networkState)
            activeTraveler.state[3] = activeTraveler.state[3] + activeTraveler.edgeCost(activeTraveler.state[2], Graph.graph.networkState)
            travelTimeDict[activeTraveler] = travelTime
            y = systemCost(systemTtWeight, Graph.graph.networkState)
            # print("\n\n")
            # print("time", t)
            # print(activeTraveler.state)
            # print(Graph.graph.networkState)
            # print(travelTimeDict)
            # print("system cost", y)
            Game.game.activeTravelers.remove(activeTraveler)
            ti.append(t)
            travelerCost.append(activeTraveler.state[3])
            labels.append(activeTraveler.state[1])
            systemCostList.append(y)
            travelerCostDic[activeTraveler.id] = travelerCost

            # print("active travelers list", Game.game.activeTravelers)
        tempDic = travelTimeDict.copy()
        for traveler in tempDic: 
            if t > travelTimeDict[traveler]:
                traveler.state[0] = 1
                e = Graph.graph.graph.es[traveler.state[2]]
                newOrigin = e.target
                # traveler.state[2] = traveler.state[1][1]
                if newOrigin in traveler.destination:
                    Graph.graph.networkState[traveler.state[2]] -= 1
                    traveler.state[2] = None
                    # print("\n\n")
                    # print("time", t)
                    # print("Traveler State", traveler.state)
                    # print("Traveler Cost", traveler.state[3])
                    # print(Graph.graph.networkState)
                    # print("system cost", y)
                    Game.game.Travelers.remove(traveler)
                    # print(Game.game.Travelers)
                    # print(systemCostList)
                    k = sum(systemCostList)
                    print(k/len(systemCostList))

                    # s = k/8
                    # print(t)
                if newOrigin in Graph.graph.a:
                    traveler.origin = Graph.graph.a
                elif newOrigin in Graph.graph.b:
                    traveler.origin = Graph.graph.b
                elif newOrigin in Graph.graph.c:
                    traveler.origin = Graph.graph.c
                elif newOrigin in Graph.graph.d:
                    traveler.origin = Graph.graph.d
                travelTimeDict.pop(traveler)
                # print(traveler.origin)
    # return systemCostList

# activeInactive(0)
# activeInactive(0.1)
# activeInactive(0.2)
# activeInactive(0.3)
# activeInactive(0.4)
# activeInactive(0.5)
# activeInactive(0.6)
activeInactive(0.7)
# print(time.time() - startTime)
# activeInactive(0.8)
# activeInactive(0.9)
# activeInactive(1)

# lt = []
# for i in numpy.arange(0,1,0.1):
#     print(i)
#     x = activeInactive(i)
#     print(x)
#     y = sum(x)
#     g = len(x)
#     z = y/g
#     lt.append(z)
#     print(lt)
# print(lt)
# g = []
# for i in x:
#     g.append(x[i][-1])
# f = sum(g)
# d = f/len(g)
# print(d)
# bg = [12.5, 13.550092592592593, 14.600185185185186, 15.650277777777777, 16.700370370370372, 17.750462962962963, 18.800555555555555, 19.850648148148146, 20.900740740740744, 21.95083333333333, 23.000925925925927]

# bg = []
# # for c in numpy.arange(0,1,0.1):
# v = (activeInactive(0.1))
# k = sum(v[:8])
# s = k/8
# bg.append(s)
# print("LISTTTT", bg)
# print(bg)
# print(traveler0.state)
# traveler0.state[0] = 0
# print(traveler0.state)
# matrix0 = Game.game.travelerCostMatrix(traveler0, Graph.graph.networkState)
# print(traveler0.edgeCost(0, Graph.graph.networkState))
        
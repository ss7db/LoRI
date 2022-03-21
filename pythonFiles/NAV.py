import Game
import Graph
import Traveler
import RecSys
import signalOptimization
import time
from timeit import default_timer as timer


startTime = time.time()
# traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
# traveler1 = Game.game.addTraveler(1, int(time.time()), Graph.graph.d, Graph.graph.b, 0.6)
# traveler2 = Game.game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.5)

# traveler3 = Game.game.addTraveler(3, int(time.time()), Graph.graph.a, Graph.graph.d, 0.6)
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

traveler0 = Game.game.addTraveler(0, int(time.time()), Graph.graph.a, Graph.graph.b, 0.5)
traveler1 = Game.game.addTraveler(1, int(time.time()), Graph.graph.a, Graph.graph.c, 0.6)
traveler2 = Game.game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.7)
traveler3 = Game.game.addTraveler(3, int(time.time()), Graph.graph.b, Graph.graph.a, 0.5)
traveler4 = Game.game.addTraveler(4, int(time.time()), Graph.graph.b, Graph.graph.c, 0.6)
traveler5 = Game.game.addTraveler(5, int(time.time()), Graph.graph.b, Graph.graph.d, 0.7)
traveler6 = Game.game.addTraveler(6, int(time.time()), Graph.graph.c, Graph.graph.a, 0.5)
traveler7 = Game.game.addTraveler(7, int(time.time()), Graph.graph.c, Graph.graph.b, 0.6)
traveler8 = Game.game.addTraveler(8, int(time.time()), Graph.graph.c, Graph.graph.d, 0.7)
traveler9 = Game.game.addTraveler(9, int(time.time()), Graph.graph.d, Graph.graph.a, 0.5)
traveler10 = Game.game.addTraveler(10, int(time.time()), Graph.graph.d, Graph.graph.b, 0.6)
traveler11 = Game.game.addTraveler(11, int(time.time()), Graph.graph.d, Graph.graph.c, 0.7)
traveler12 = Game.game.addTraveler(12, int(time.time()), Graph.graph.a, Graph.graph.b, 0.2)
traveler13 = Game.game.addTraveler(13, int(time.time()), Graph.graph.a, Graph.graph.c, 0.3)
traveler14 = Game.game.addTraveler(14, int(time.time()), Graph.graph.a, Graph.graph.d, 0.4)
traveler15 = Game.game.addTraveler(15, int(time.time()), Graph.graph.b, Graph.graph.a, 0.2)
traveler16 = Game.game.addTraveler(16, int(time.time()), Graph.graph.b, Graph.graph.c, 0.3)
traveler17 = Game.game.addTraveler(17, int(time.time()), Graph.graph.b, Graph.graph.d, 0.4)
traveler18 = Game.game.addTraveler(18, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)
traveler19 = Game.game.addTraveler(19, int(time.time()), Graph.graph.c, Graph.graph.d, 0.3)
traveler20 = Game.game.addTraveler(20, int(time.time()), Graph.graph.c, Graph.graph.d, 0.4)
traveler21 = Game.game.addTraveler(21, int(time.time()), Graph.graph.d, Graph.graph.a, 0.2)
traveler22 = Game.game.addTraveler(22, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
traveler23 = Game.game.addTraveler(23, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
traveler24 = Game.game.addTraveler(24, int(time.time()), Graph.graph.a, Graph.graph.b, 1.0)
traveler25 = Game.game.addTraveler(25, int(time.time()), Graph.graph.a, Graph.graph.c, 0.9)
traveler26 = Game.game.addTraveler(26, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
traveler27 = Game.game.addTraveler(27, int(time.time()), Graph.graph.b, Graph.graph.a, 1.0)
traveler28 = Game.game.addTraveler(28, int(time.time()), Graph.graph.b, Graph.graph.c, 0.9)
traveler29 = Game.game.addTraveler(29, int(time.time()), Graph.graph.b, Graph.graph.d, 0.8)
traveler30 = Game.game.addTraveler(30, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
traveler31 = Game.game.addTraveler(31, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
traveler32 = Game.game.addTraveler(32, int(time.time()), Graph.graph.c, Graph.graph.d, 0.8)
traveler33 = Game.game.addTraveler(33, int(time.time()), Graph.graph.d, Graph.graph.a, 1.0)
traveler34 = Game.game.addTraveler(34, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)
traveler35 = Game.game.addTraveler(35, int(time.time()), Graph.graph.d, Graph.graph.c, 0.8)
traveler36 = Game.game.addTraveler(36, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
traveler37 = Game.game.addTraveler(37, int(time.time()), Graph.graph.a, Graph.graph.b, 1.0)
traveler38 = Game.game.addTraveler(38, int(time.time()), Graph.graph.a, Graph.graph.c, 0.9)
traveler39 = Game.game.addTraveler(39, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
traveler40 = Game.game.addTraveler(40, int(time.time()), Graph.graph.b, Graph.graph.a, 1.0)
traveler41 = Game.game.addTraveler(41, int(time.time()), Graph.graph.b, Graph.graph.c, 0.9)
traveler42 = Game.game.addTraveler(42, int(time.time()), Graph.graph.b, Graph.graph.d, 0.8)
traveler43 = Game.game.addTraveler(43, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
traveler44 = Game.game.addTraveler(44, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)




travelTimeDict = {}
ti = []
travelerCost = []
travelerCostDic = {} 
labels = []
systemCostList = []
traveler_total_cost = []

def travelerEdgeCost(e, networkState):
    if Graph.graph.edgeState[e][0] == "car":
        cost = (max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1]))
        # cost = Graph.graph.edgeState[e][1] 
        # print("edge cost", cost)
    elif Graph.graph.edgeState[e][0] == "train":
        cost = (Graph.graph.edgeState[e][1])
        # print("edge cost", cost)
    elif Graph.graph.edgeState[e][0] == "walk":
        cost = (Graph.graph.edgeState[e][1])
        # print("edge cost", cost)
    elif Graph.graph.edgeState[e][0] == "switch":
        cost = 1
        # print("edge cost", cost)
    # print(int(cost)*100)
    return cost

def systemCost(networkState):
        cost = 0
        for e in Graph.graph.edgeState:
            if Graph.graph.edgeState[e][0] == "car":
                cost = (max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1]))
            elif Graph.graph.edgeState[e][0] == "train":
                cost += (Graph.graph.edgeState[e][1])
            elif Graph.graph.edgeState[e][0] == "walk":
                cost += (Graph.graph.edgeState[e][1])
            elif Graph.graph.edgeState[e][0] == "switch":
                cost += 1
        return cost

def chosenPathNav(traveler):
    costList = []
    for path in traveler.paths():
        cost = 0
        for i in range(len(path)-1):
            if i == 0:
                e = Graph.graph.graph.get_eid(path[i], path[i+1])
                cost += travelerEdgeCost(e, Graph.graph.networkState)
            else: 
                e = Graph.graph.graph.get_eid(path[i], path[i+1])
                cost += travelerEdgeCost(e, Graph.graph.networkState)
        # cost = int(cost*100)
        costList.append(cost)
    # print(costList)
    bestCost = min(costList)
    # print(bestCost)
    pathIndex = costList.index(bestCost)
    # print(costList[pathIndex])
    return traveler.paths()[pathIndex]


def activeInactive():
    start = timer()
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
            # print(activeTraveler)
            # optimalSignal = signalOptimization.optimalSignal(activeTraveler) 
            # print(optimalSignal)
            activeTravelerPath = chosenPathNav(activeTraveler)
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
            y = systemCost(Graph.graph.networkState)

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
                    traveler_total_cost.append(traveler.state[3])
                    print(traveler_total_cost, len(traveler_total_cost))
                    g = sum(traveler_total_cost)
                    print(g/len(traveler_total_cost))
                    # print(Game.game.Travelers)
                    # print(travelerCostDic)
                    # print(sum(systemCostList)/8)
                    # print(ti)
                    # print(systemCostList)
                    k = sum(systemCostList)
                    print(k/len(systemCostList))
                if newOrigin in Graph.graph.a:
                    traveler.origin = Graph.graph.a
                elif newOrigin in Graph.graph.b:
                    traveler.origin = Graph.graph.b
                elif newOrigin in Graph.graph.c:
                    traveler.origin = Graph.graph.c
                elif newOrigin in Graph.graph.d:
                    traveler.origin = Graph.graph.d
                travelTimeDict.pop(traveler)
                end = timer()
                print("Time to run activeInactive is" + str(end - start))
                print("\n")
                # print(traveler.origin)
    # return 

activeInactive()
# print(time.time()-startTime)
# print(traveler0.state)
# traveler0.state[0] = 0
# print(traveler0.state)
# matrix0 = Game.game.travelerCostMatrix(traveler0, Graph.graph.networkState)
# print(traveler0.edgeCost(0, Graph.graph.networkState))
# print(chosenPathNav(traveler0))d

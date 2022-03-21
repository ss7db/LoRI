import Game
import Graph
import Traveler
import RecSys
import signalOptimization
import time
import numpy
from timeit import default_timer as timer

startTime = time.time()

traveler0 = Game.game.addTraveler(0, int(time.time()), [0], [3], 0.5)
traveler1 = Game.game.addTraveler(1, int(time.time()), [0], [5], 0.6)
# traveler2 = Game.game.addTraveler(2, int(time.time()), Graph.graph.a, Graph.graph.d, 0.7)
# traveler3 = Game.game.addTraveler(3, int(time.time()), Graph.graph.b, Graph.graph.a, 0.5)
# traveler4 = Game.game.addTraveler(4, int(time.time()), Graph.graph.b, Graph.graph.c, 0.6)
# traveler5 = Game.game.addTraveler(5, int(time.time()), Graph.graph.b, Graph.graph.d, 0.7)
# traveler6 = Game.game.addTraveler(6, int(time.time()), Graph.graph.c, Graph.graph.a, 0.5)
# traveler7 = Game.game.addTraveler(7, int(time.time()), Graph.graph.c, Graph.graph.b, 0.6)
# traveler8 = Game.game.addTraveler(8, int(time.time()), Graph.graph.c, Graph.graph.d, 0.7)
# traveler9 = Game.game.addTraveler(9, int(time.time()), Graph.graph.d, Graph.graph.a, 0.5)
# traveler10 = Game.game.addTraveler(10, int(time.time()), Graph.graph.d, Graph.graph.b, 0.6)
# traveler11 = Game.game.addTraveler(11, int(time.time()), Graph.graph.d, Graph.graph.c, 0.7)
# traveler12 = Game.game.addTraveler(12, int(time.time()), Graph.graph.a, Graph.graph.b, 0.2)
# traveler13 = Game.game.addTraveler(13, int(time.time()), Graph.graph.a, Graph.graph.c, 0.3)
# traveler14 = Game.game.addTraveler(14, int(time.time()), Graph.graph.a, Graph.graph.d, 0.4)
# traveler15 = Game.game.addTraveler(15, int(time.time()), Graph.graph.b, Graph.graph.a, 0.2)
# traveler16 = Game.game.addTraveler(16, int(time.time()), Graph.graph.b, Graph.graph.c, 0.3)
# traveler17 = Game.game.addTraveler(17, int(time.time()), Graph.graph.b, Graph.graph.d, 0.4)
# traveler18 = Game.game.addTraveler(18, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)
# traveler19 = Game.game.addTraveler(19, int(time.time()), Graph.graph.c, Graph.graph.d, 0.3)
# traveler20 = Game.game.addTraveler(20, int(time.time()), Graph.graph.c, Graph.graph.d, 0.4)
# traveler21 = Game.game.addTraveler(21, int(time.time()), Graph.graph.d, Graph.graph.a, 0.2)
# traveler22 = Game.game.addTraveler(22, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
# traveler23 = Game.game.addTraveler(23, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
# traveler24 = Game.game.addTraveler(24, int(time.time()), Graph.graph.a, Graph.graph.b, 1.0)
# traveler25 = Game.game.addTraveler(25, int(time.time()), Graph.graph.a, Graph.graph.c, 0.9)
# traveler26 = Game.game.addTraveler(26, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
# traveler27 = Game.game.addTraveler(27, int(time.time()), Graph.graph.b, Graph.graph.a, 1.0)
# traveler28 = Game.game.addTraveler(28, int(time.time()), Graph.graph.b, Graph.graph.c, 0.9)
# traveler29 = Game.game.addTraveler(29, int(time.time()), Graph.graph.b, Graph.graph.d, 0.8)
# traveler30 = Game.game.addTraveler(30, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
# traveler31 = Game.game.addTraveler(31, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
# traveler32 = Game.game.addTraveler(32, int(time.time()), Graph.graph.c, Graph.graph.d, 0.8)
# traveler33 = Game.game.addTraveler(33, int(time.time()), Graph.graph.d, Graph.graph.a, 1.0)
# traveler34 = Game.game.addTraveler(34, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)
# traveler35 = Game.game.addTraveler(35, int(time.time()), Graph.graph.d, Graph.graph.c, 0.8)
# traveler36 = Game.game.addTraveler(36, int(time.time()), Graph.graph.d, Graph.graph.c, 0.4)
# traveler37 = Game.game.addTraveler(37, int(time.time()), Graph.graph.a, Graph.graph.b, 1.0)
# traveler38 = Game.game.addTraveler(38, int(time.time()), Graph.graph.a, Graph.graph.c, 0.9)
# traveler39 = Game.game.addTraveler(39, int(time.time()), Graph.graph.a, Graph.graph.d, 0.8)
# traveler40 = Game.game.addTraveler(40, int(time.time()), Graph.graph.b, Graph.graph.a, 1.0)
# traveler41 = Game.game.addTraveler(41, int(time.time()), Graph.graph.b, Graph.graph.c, 0.9)
# traveler42 = Game.game.addTraveler(42, int(time.time()), Graph.graph.b, Graph.graph.d, 0.8)
# traveler43 = Game.game.addTraveler(43, int(time.time()), Graph.graph.c, Graph.graph.a, 1.0)
# traveler44 = Game.game.addTraveler(44, int(time.time()), Graph.graph.c, Graph.graph.a, 0.2)

travelTimeDict = {}
ti = []
traveler_total_cost = []
travelerCost = []
labels = []
systemCostList = []
travelerCostDic = {} 

# s = 0
def systemCost(ttWeight, networkState):
    cost = 0
    # for e in Graph.graph.edgeState:
    #     if Graph.graph.edgeState[e][0] == "car":
    #         cost = ttWeight*(max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1])) + (1 - ttWeight)*(max(Graph.graph.CO(e, networkState), Graph.graph.edgeState[e][1]))
    #     elif Graph.graph.edgeState[e][0] == "train":
    #         cost += ttWeight*(Graph.graph.edgeState[e][1]) + (1 - ttWeight)*(0.5*Graph.graph.edgeState[e][1])
    #     elif Graph.graph.edgeState[e][0] == "walk":
    #         cost += ttWeight*(Graph.graph.edgeState[e][1])
    #     elif Graph.graph.edgeState[e][0] == "switch":
    #         cost += 1
    for e in Graph.graph.edgeState:
        bpr = max(Graph.graph.BPR(e, networkState), Graph.graph.flow(e))
        CO = max(Graph.graph.CO(e, networkState), Graph.graph.flow(e))
        cost += ttWeight*(bpr)+ (1 - ttWeight)*(CO)
    return cost

def activeInactive(systemTtWeight):
    start = timer()
    systemCostList = []
    traveler_average_cost = 0
    system_average_cost = 0

    for t in range(1, 100):
    
        for i in Game.game.Travelers:
           if i.state[0]==1:
                Game.game.activeTravelers.append(i)

        tempList = Game.game.activeTravelers.copy()

        for activeTraveler in tempList:

            optimalSignal = signalOptimization.optimalSignal(activeTraveler) 

            activeTravelerPath = Game.game.chosenPath(optimalSignal, activeTraveler)

            activeTraveler.state[0] = 0
            activeTraveler.state[1] = activeTravelerPath
            if activeTraveler.state[2] == None:
                activeTraveler.state[2] = Graph.graph.graph.get_eid(activeTravelerPath[0], activeTravelerPath[1])

                Graph.graph.networkState[activeTraveler.state[2]] += 1

            else: 

                Graph.graph.networkState[activeTraveler.state[2]] -= 1

                activeTraveler.state[2] = Graph.graph.graph.get_eid(activeTravelerPath[0], activeTravelerPath[1])
 
                Graph.graph.networkState[activeTraveler.state[2]] += 1                  

        
            travelTime = t + Graph.graph.edgeTravelTime(activeTraveler.state[2], Graph.graph.networkState)
            activeTraveler.state[3] = activeTraveler.state[3] + activeTraveler.edgeCost(activeTraveler.state[2], Graph.graph.networkState)
            travelTimeDict[activeTraveler] = travelTime
            y = systemCost(systemTtWeight, Graph.graph.networkState)

            Game.game.activeTravelers.remove(activeTraveler)
            ti.append(t)
            travelerCost.append(activeTraveler.state[3])
            labels.append(activeTraveler.state[1])
            systemCostList.append(y)
            travelerCostDic[activeTraveler.id] = travelerCost


        tempDic = travelTimeDict.copy()
        for traveler in tempDic: 
            if t > travelTimeDict[traveler]:
                traveler.state[0] = 1
                e = Graph.graph.graph.es[traveler.state[2]]
                newOrigin = e.target

                if newOrigin in traveler.destination:
                    Graph.graph.networkState[traveler.state[2]] -= 1
                    traveler.state[2] = None


                    Game.game.Travelers.remove(traveler)
                    traveler_total_cost.append(traveler.state[3])
                    g = sum(traveler_total_cost)
                    # print(g/len(traveler_total_cost))
                    traveler_average_cost = g/len(traveler_total_cost)
                    k = sum(systemCostList)
                    # print(k/len(systemCostList))
                    system_average_cost = k/len(systemCostList)

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
    return traveler_average_cost, system_average_cost

# x = [i / 100 for i in range(0,110,10)]
# sys_cost_with_diff_motives = []
# for i in x:
#     print(i)
#     sys_cost_with_diff_motives.append(activeInactive(i)[1])
#     print(sys_cost_with_diff_motives, i)

# print(sys_cost_with_iff_motives)
print(activeInactive(0.7))
# activeInactive(0.1)
# activeInactive(0.2)
# print(Game.game.travelerCostMatrix2forCP(traveler0, Graph.graph.networkState))
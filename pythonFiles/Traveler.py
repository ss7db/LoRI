
import Graph
import numpy 
import random
import time
import cvxpy
from timeit import default_timer as timer

class Traveler:
    def __init__(self, id, t, origin, destination, ttWeight):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.ttWeight = ttWeight
        self.t = t
        # self.belief = Traveler.priorBeliefs()
        # Graph.graph.activeTravelers.append(Traveler)
        self.state = {
            0 : 1, #State of the commuter (active = 1, inactive = 0) 
            1 : None, #Path chosen by the commuter
            2 : None, #Current edge, initialized as None #Traveler Beliefs
            3 : 0 #Cost accumulated
            # 5 : time.time(), #Time when the traveler is added 0
        }

    def priorBeliefs(self, noOfEdges, maxTravelers):
        matrix = numpy.random.rand(noOfEdges, maxTravelers)
        matrix/matrix.sum(axis=1)[:,None]
        return matrix

    def paths(self):
        start = timer()
        # gr = Graph.Graph()
        paths = []
        for i in self.origin:
            for j in self.destination:
                path = Graph.graph.graph.get_all_shortest_paths(i,j)
                paths.extend(path)
        end  = timer()
        # print("Time to run Travelers.paths is " + str(end - start))
        return paths 

    # def pathCosts(self):
    #     # Graph.graph.graph = Graph.graph.graphaph.Graph.graph.graphaph()
    #     pathCosts = []
    #     for i in Traveler.paths(self):
    #         cost = 0
    #         for j in range(len(i)-1):
    #             e = Graph.graph.graph.Graph.graph.graphaph.get_eid(i[j], i[j+1])
    #             if Graph.graph.graph.edgeState[e][0] == "car":
    #                 cost += self.ttWeight*(Graph.graph.graph.BPR(e)) + (1 - self.ttWeight)*(Graph.graph.graph.CO(e))
    #             elif Graph.graph.graph.edgeState[e][0] == "train":
    #                 cost += self.ttWeight*(Graph.graph.graph.edgeState[e][1]) + (1 - self.ttWeight)*(0.5*Graph.graph.graph.edgeState[e][1])
    #             elif Graph.graph.graph.edgeState[e][0] == "walk":
    #                 cost += self.ttWeight*(Graph.graph.graph.edgeState[e][1])
    #             elif Graph.graph.graph.edgeState[e][0] == "switch":
    #                 cost += 1
    #         pathCosts.append(cost)
    #     return pathCosts

    def posteriorBeliefPhi(self, mu, prior):
        posteriorBelief = []
        for i in range(len(prior)):
            unNormalizedPosterior = [ a * b for a, b in zip(prior[i], mu[i])]
            posterior = unNormalizedPosterior / sum(unNormalizedPosterior)
            posteriorBelief.append(posterior)
        return posteriorBelief

    def rho(self, e,ePrime):
        paths = Traveler.paths()
        rho = []
        pi = [0.0]*20
        for i in  paths:
            if (e in i and ePrime in i):
                if(i.index(ePrime) == i.index(e) + 1):
                    rho.append(pi[paths.index(i)])
        return sum(rho)

    def networkStateFromPhi(self, belief):
        networkState = []
        for i in range(len(belief)):
            temp = max(belief[i])
            networkState.append(temp)
        return networkState
    # def currentEdge(self, previousEdge, currentEdge, numberOfCommuters):
    #     if previousEdge == None:
    #         numberOfCommuters[currentEdge] += 1
    #     else:
    #         numberOfCommuters[previousEdge] -= 1
    #         numberOfCommuters[currentEdge] += 1

    # def position(self, numberOfCommuters):
    #     # Graph.graph.graph = Graph.graph.graphaph.Graph.graph.graphaph()
    #     for i in Traveler.paths(self):
    #         # numberOfCommuters = Graph.graph.graph.numberOfCommuters
    #         print(i, time.time(), numberOfCommuters)
    #         for j in range(len(i)-1):
    #             e = Graph.graph.graph.get_eid(i[j], i[j+1])
    #             if j == 0:
    #                 Traveler.currentEdge(self, None, e, numberOfCommuters)
    #                 print((time.time()), numberOfCommuters)
    #             else:
    #                 previousEdge = Graph.graph.graph.get_eid(i[j-1],i[j])
    #                 Traveler.currentEdge(self, previousEdge, e, numberOfCommuters)
    #                 print((time.time()), numberOfCommuters)
    #             if Graph.graph.graph.edgeState[e][0] == "switch":
    #                 travelerState[5] = 1
    #             elif Graph.graph.graph.edgeState[e][0] == "train":
    #                 travelerState[5] = Graph.graph.graph.edgeState[e][1]
    #             elif Graph.graph.graph.edgeState[e][0] == "walk":
    #                 travelerState[5] = Graph.graph.graph.edgeState[e][1]
    #             elif Graph.graph.graph.edgeState[e][0] == "car":
    #                 travelerState[5] = Graph.graph.graph.BPR(e)
    #             time.sleep(travelerState[5])

    def pathCosts(self, networkState):
        for path in self.state[4]:
            travelerState = self.state
            # networkState = Graph.graph.networkState
            travelerState[2] = path
            for i in range(len(path)-1):
                e = Graph.graph.get_eid(path[i], path[i+1])
                travelerState[1] = e
                networkState[e] += 1
                if Graph.graph.graph.edgeState[e][0] == "switch":
                    travelerState[5] = 1
                elif Graph.graph.graph.edgeState[e][0] == "train":
                    travelerState[5] = Graph.graph.graph.edgeState[e][1]
                elif Graph.graph.graph.edgeState[e][0] == "walk":
                    travelerState[5] = Graph.graph.graph.edgeState[e][1]
                elif Graph.graph.graph.edgeState[e][0] == "car":
                    travelerState[5] = Graph.graph.graph.BPR(e, networkState)
                time.sleep(travelerState[5])

    def pathCostsGivenPath(self, path, networkState):
        cost = 0
        for i in range(len(path)-1):
            # print(i)
            if i == 0:
                e = Graph.graph.graph.get_eid(path[i], path[i+1])
                # print(e)
                cost += self.edgeCost(e, networkState)
                # print("cost for edge", e, cost)
            else: 
                e = Graph.graph.graph.get_eid(path[i], path[i+1])
                cost += self.edgeCost(e, networkState) 
        return cost
    
    def edgeCost(self, e, networkState):
        # print(Graph.graph.edgeState[e])
        # if Graph.graph.edgeState[e][0] == "car":
        #     cost = self.ttWeight*(max(Graph.graph.BPR(e, networkState), Graph.graph.edgeState[e][1])) + (1 - self.ttWeight)*(max(Graph.graph.CO(e, networkState), Graph.graph.edgeState[e][1]))
        # elif Graph.graph.edgeState[e][0] == "train":
        #     cost = self.ttWeight*(Graph.graph.edgeState[e][1]) + (1 - self.ttWeight)*(0.5*Graph.graph.edgeState[e][1])
        # elif Graph.graph.edgeState[e][0] == "walk":
        #     cost = self.ttWeight*(Graph.graph.edgeState[e][1])
        # elif Graph.graph.edgeState[e][0] == "switch":
        #     cost = 1
        bpr = max(Graph.graph.BPR(e, networkState), Graph.graph.flow(e))
        CO = max(Graph.graph.CO(e, networkState), Graph.graph.flow(e))
        return self.ttWeight*(bpr)+ (1 - self.ttWeight)*(CO)

    def top3Paths(self):
        costList = []
        travelerAllPaths = [x for x in self.paths()]
        for path in travelerAllPaths:
            pathCost = self.pathCostsGivenPath(path, Graph.graph.networkState)
            costList.append(pathCost)
        x = sorted(zip(costList, travelerAllPaths))[:3]
        return [z[1] for z in x]


    def current_edge_if_path_is_not_chosen(self):
        incident_edges_to_origin = Graph.graph.graph.incident(self.origin[0])
        edge_costs = []
        for edge in incident_edges_to_origin:
            cost = self.edgeCost(edge, Graph.graph.networkState)
            edge_costs.append(cost)
        min_cost = min(edge_costs)
        min_cost_index = edge_costs.index(min_cost)
        return incident_edges_to_origin[min_cost_index]

            

        



        


            

    
        
    

import igraph
import itertools
import math
import numpy as np
import cvxpy 

class Graph():
    def __init__(self): 
        # self.graph = igraph.Graph.Adjacency([[0,1,1,0,0,0,0,0,0,0,0,0], 
        #                     [0,0,1,1,0,0,0,0,0,1,0,0], 
        #                     [0,0,0,1,0,0,0,0,0,0,0,0],
        #                     [0,0,0,0,0,0,0,0,0,0,0,0],
        #                     [0,0,0,0,0,1,0,0,0,0,0,0],
        #                     [0,1,0,0,0,0,0,1,0,1,0,0],
        #                     [0,0,0,0,1,0,0,0,0,0,0,0],
        #                     [0,0,0,0,0,0,1,0,0,0,0,0],
        #                     [0,0,0,0,0,0,0,0,0,0,0,0],
        #                     [0,0,0,0,0,0,0,0,0,0,1,0],
        #                     [0,0,1,0,0,0,1,0,0,0,0,0],
        #                     [0,0,0,0,0,0,0,0,0,0,0,0]], directed = True)
        self.graph = igraph.Graph.Load('manhatten.graphml')
        # self.a = [0,4,8]
        # self.b = [1,5,9]
        # self.c = [2,6,10]
        # self.d = [3,7,11]

            #edge state: mode, number of commuters, flow
        # self.edgeState = {
        #     0 : ["car", 2,],
        #     1 : ["car", 3], 
        #     2 : ["car", 1], 
        #     3 : ["car", 3],
        #     4 : ["switch", "car", "train"], 
        #     5 : ["car", 2],
        #     6 : ["train", 3],
        #     7 : ["switch", "train", "car"], 
        #     8 : ["train", 4], 
        #     9 : ["switch", "train", "walk"],
        #     10 : ["train", 4], 
        #     11 : ["train", 2],
        #     12 : ["walk", 4],
        #     13 : ["switch", "walk", "car"],
        #     14 : ["switch", "walk", "train"]
        # }

        self.phi = [[1,0,0,0,0,0,0,0],
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
        self.networkState = [0]*15089
        # self.networkState = [8,4,6,9,3,0,0,0,0,0,0,0,0,0,0]
    def CO(self,e, networkState): 
        # print(networkState)
        flow = self.flow(e)
        # print("flow", flow)
        BPRno = Graph.BPR(self, e, networkState)
        # print("bpr", BPRno)
        ratio = 0.7962*(flow)/BPRno
        # print("ratio",ratio)
        t = 0.2038*(BPRno)*(math.exp(ratio))
        # t = 0.2038*(BPRno)**ratio
        # print("t", t)
        return t
    # def CO(self,e, networkState): 
    #     print(networkState)
    #     flow = self.edgeState[e][1]
    #     print("flow", flow)
    #     BPRno = Graph.BPR(self, e, networkState)
    #     print("bpr", BPRno)
    #     t = cvxpy.multiply(0.7962, flow)
    #     ratio = t/BPRno
    #     print("ratio",ratio)
    #     # t = 0.2038*(BPRno)*(math.exp(ratio))
    #     v = cvxpy.multiply(0.2038, BPRno)
    #     b = cvxpy.exp(ratio)
    #     t = cvxpy.multiply(v,b)
    #     print("t", t)
    #     return t

    def BPR(self, e, networkState):
        # print(e)
        noOfCommuters = networkState[e]
        flow = self.flow(e)
        ratio = noOfCommuters/3
        tc = flow*(1 + 0.15*(ratio**4))
        return tc

    def edgeTravelTime(self, e, networkState):
        return Graph.BPR(self, e, networkState)
        # if self.edgeState[e][0] == "switch":
        #     return 1
        # elif self.edgeState[e][0] == "train":
        #     return self.edgeState[e][1]
        # elif self.edgeState[e][0] == "walk":
        #     return self.edgeState[e][1]
        # elif self.edgeState[e][0] == "car":
        #     return Graph.BPR(self, e, networkState)

    def flow(self, e):
        length = float(self.graph.es[e].attributes()['length'])
        if self.graph.es[e].attributes()['maxspeed'] == '':
            max_speed = 20
        else: 
            max_speed = float(self.graph.es[e].attributes()['maxspeed'][0:2])
        flow = length/max_speed
        return flow



graph = Graph()
# print(graph.flow(0, [0]*14))
# for e in graph.graph.es:
#     print(e, e.source, e.target)

# for v in graph.graph.vs:
#     print(v, graph.graph.incident(v))
# y = graph.graph.incident(5)
# if len(set(x).intersection(y)) != 0:
#     print("true")
# else:
#     print("false")

# pathsCarCar = graph.graph.get_all_simple_paths(0,3)
# print(pathsCarCar)
# pathsCarTrain = g.get_all_simple_paths(0,7)
# # pathsCarWalk = g.get_all_simple_paths(0,11)
# pathsTrainCar = g.get_all_simple_paths(4,3)
# pathsTrainTrain = g.get_all_simple_paths(4,7)
# # pathsTrainWalk = g.get_all_simple_paths(4,11)

# paths = list(itertools.chain(pathsCarCar, pathsCarTrain, pathsTrainCar, pathsTrainTrain))
              
# print(paths)
# print(len(paths))
# p = pathCosts(paths, 0.5)
# print(p)
# print(len(p))
# for e in gr.g.es:
#     print(e, e.source, e.target)
# print(graph.BPR(0, graph.networkState))
import itertools
import random
import sched
import threading
import time
import numpy

import Graph

# a = [0,4,8]
# b = [1,5,9]
# c = [2,6,10]
# d = [3,7,11]
# gr = Graph.Graph()
# def paths(a,d):
#     paths = []
#     for i in a:
#         for j in d:
#             path = gr.graph.get_all_simple_paths(i,j)
#             print(path)
#             paths.append(path)
#     return paths 

# print(paths(a,d))
# p = []
# prob = [0, 0.25, 0.5, 0.75, 1.0]
# arr = numpy.zeros(5)
# for j in range(3):
#     x = random.randrange(len(prob))
#     y = random.randrange(len(arr))
#     arr[y] = arr[y] + prob[x]
#     if sum(arr) == 1:
#         p.append(arr)
#         break
# print(p)
# a = [1,2,3,4,5,6,7,8,9,10]
# arr = numpy.zeros(5)
# for j in range(3):
#     x = random.randrange(0,len(a))
#     y = random.randrange(0,len(arr))
#     print(x,y)
#     arr[y] = arr[y] + a[x]
#     if sum(arr) == 10:
#         print(arr)
#         break
# def numberToBase(n, m):
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % m))
#         n //= m
#     return digits[::-1]
# print(numberToBase(780, 5))

# edgeState = {
#     0 : ["car", 2, 2],
#     1 : ["car", 2, 3], 
#     2 : ["car", 1, 1], 
#     3 : ["car", 4, 3],
#     4 : ["switch", "car", "train"], 
#     5 : ["car", 2, 2],
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

# for i in edgeState: 
#     print(edgeState[i][1])
# ma = [[1,2],[3,4]]
# for i in range(len(ma)):
#     for j in range(len(ma[0])):
#         print(ma[i][j])
# print(sum(2*ma[0]))
# print(ma[0])
# list = [1,2,3,4]
# def x(a,b):
#     list = [1,2,3,4]
#     if a == None:
#         list[b] +=1
#     else:
#         list[a] -= 1
#         list[b] +=1 
#     return list

# print(x(None,1))
# def main():
#     print(time.time())
#     sec = 1
#     threading.Timer(1, main).start()

# # if __name__ == "__main__":
# #     main()

# if __name__ == "__main__":
#     main()
# for i in range(5):
#     print(i)
#     # if i ==2:
#     #     continue
#     if i == 2:
#         break

# def ti():
#     print(time.time())

# threading.Timer(1, ti).start()
    # activeTravelers = Graph.graph.activeTravelers
    # activeTravelers.remove(traveler)
# temp = [[[1,2,],[3,4]], [[5,6],[7,8]], [[9,10], [11,12, 13], [14,15,16]]]
# s = list(itertools.product(*temp))
# print(s[0])
# dic = {}
# for i in range(5):
#     for j in range(2): 
#         dic[i] = j
# print(dic, [*dic.keys()])
# keyList = [2,3,4,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,7,6]
# keyList = [2,3,5]
# for j in range(0, len(keyList)):
#     if j < len(keyList)-1: 
#         networkState = [0]*14
#         networkState[keyList[j]] -= 1
#         networkState[keyList[j+1]] += 1
#         print(networkState)
#     else:
#         networkState = [0]*14
#         networkState[keyList[j]] -= 1
#         print(networkState)



# locationPredictionForAllStrategies(Graph.graph.networkState, Game.game.strategyProfiles)
# d = {0:1}
# b = {1:2}
# l =[] 
# v = []
# l.append(d)
# l.append(b)
# print(l)
# v.append(d)
# v.append(b)
# print(v)
# s = []
# f= []
# s.append(l)
# s.append(v)
# print(s[0])
# f.extend(l)
# f.extend(v)
# print(f)

# psi = [[1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0]]
# n = []
# for i in psi:
#     i.extend([3]*(4-2))
    
# print(psi)

# with open("g2.nfg", "r") as file :
#   filedata = file.read()



# with open("g2_test.nfg", "w+") as file1:
#   filedata1 = filedata.replace("\n", " \r\n")  
#   file1.write(filedata)
# filedata1 = filedata.replace('\n', '\r\n')
# print(filedata) 
f = open('mainExample.nfg','r')
filedata = f.read()
f.close()

newdata = filedata.replace(r"\n", "\n")
newdata = newdata.replace("b", "")
newdata = newdata.replace("'", "")

# f = open('mainExampleProcessed.nfg','w')
# f.write(newdata)
# f.close()
lastLine = []
# with open('mainExampleQRE.txt', 'rb') as f:
for line in newdata:
    print(line)
#     pass
# lastLine.append(line.rstrip())
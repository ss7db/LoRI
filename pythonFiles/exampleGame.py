import gambit
import math
import numpy

g = gambit.Game.new_table([2,2])
g.title = "Example QRE"
g.players[0].label = "Traveler1"
g.players[1].label = "Traveler2"
g[0,0][0] = 2
g[0,0][1] = 2
g[0,1][0] = 0
g[0,1][1] = 5
g[1,0][0] = 5
g[1,0][1] = 0
g[1,1][0] = 1
g[1,1][1] = 1

# g1 = gambit.Game.read_game("xyz2.nfg")

with open("prisonersDilemmaQre.nfg", "w") as f:
    f.write(g.write('native'))
# def padding(costMatrices):
    # maxColumn =  max(list(map(lambda x:len(x), costMatrices)))
    # maxRow = max(list(map(lambda x:len(x[0]), costMatrices)))
    # for matrix in costMatrices:
    #     if len(matrix) < maxColumn:
    #         z = [0]*maxRow
    #         matrix.extend([z]*(maxColumn - len(matrix)))

    #     if len(matrix[0]) < maxRow:
    #         temp = maxRow - len(matrix[0])
    #         for l in matrix:
    #             l.extend([0]*temp)
    
    # return costMatrices
# solver = gambit.nash.ExternalEnumPureSolver()
# one = numpy.array([[1,2,3], [4,5,6]], dtype=gambit.Rational)
# two = numpy.array([[1,2],[3,4],[5,6]], dtype=gambit.Rational)
# l = []
# l.append(one)
# l.append(two)
# m = padding([[[1.89,2.76,3.8], [4.34,5.67,6.54]],[[1.67,2.34],[3.65,4.32],[5.76,6.34]]])
# # g2 = gambit.Game.from_arrays(numpy.array(m[0], dtype=gambit.Rational), numpy.array(m[1], dtype=gambit.Rational))
# # print(g2)

# with open("g3.nfg", "w") as f:
#     f.write(g2.write('nfg'))
# # print(one)
# m1 = numpy.array([numpy.zeros(130)]*10, dtype=gambit.Rational)
# m2 = numpy.array([numpy.zeros(130)]*10, dtype=gambit.Rational)
# g3 = gambit.Game.from_arrays(m1,m2)
# print(g3)

# h = gambit.Game.read_game("xyz2.nfg")
# solver = gambit.nash.ExternalLogitSolver()
# print(solver.solve(g))

# with open('somefile1.txt', 'w') as f:
#     f.write(g.write('native'))

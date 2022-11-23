from egzP8btesty import runtests
from math import inf


def Floyd_Warh(D, n):
    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][k] + D[k][v], D[u][v])
    return D


def robot( G, P ):
    n = len(G)
    Martix = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            Martix[i][G[i][j][0]] = G[i][j][1]

    Results = Floyd_Warh(Martix, n)
    result = 0
    for i in range(len(P) - 1):
        result += Results[P[i]][P[i+1]]
    return result
    
runtests(robot, all_tests = True)

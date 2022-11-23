from egzP3btesty import runtests 
from queue import PriorityQueue


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1



def lufthansa ( G ):
    n = len(G)
    mass = 0
    K = []
    vertex = []
    for i in range(n):
        vertex.append(Node(i))
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                mass += G[i][j][1]
                K.append((i, G[i][j][0], -G[i][j][1]))
    K.sort(key = lambda x:x[2])

    result = []
    # i = 0
    for j in range(len(K)):
        (fromm, to, cost) = K[j]
        source = find(vertex[fromm])
        sink = find(vertex[to])
        if sink != source:
            result.append((fromm, to, cost))
            union(sink, source)
            # i += 1
            # if i == n-1: # niby przyspiesza, w rzeczywistości się nie opłaca
            #     break

    for j in range(len(K)):
        if K[j] not in result:
            (fromm, to, cost) = K[j]
            result.append((fromm, to, cost))
            break

    summ = 0
    for i in range(len(result)):
        summ -= result[i][2]
    return mass - summ

runtests ( lufthansa, all_tests=True )
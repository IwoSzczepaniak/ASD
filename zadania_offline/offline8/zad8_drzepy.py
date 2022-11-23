from zad8testy import runtests
from math import sqrt, ceil


def distance(A, i, j):
    dis = sqrt( (A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2 )
    return ceil(dis)


def create(A, n, graph):
    for source in range(n):
        for destination in range(n):
            if destination != source:
                tmp = (distance(A, source, destination), source, destination)
                graph.append(tmp)


def create_dfs(A, n):
    G = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                tmp = (j, distance(A, i, j))
                G[i].append(tmp)
    return G


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


def dfs(G, v, visited, path, n, l, r):
    if len(path) == n:
        return True
    for w in G[v]:
        if not visited[w[0]] and l < w[1] < r:
            visited[w] = True
            path.append(w)
            if dfs(G, w, visited, path, n, l, r):
                return True
    return None


def kruskal(graph, v, e, l, r, G):
    i = 0
    j = 0
    coherent = True
    begin_min = 10**10
    destiny_max = -1
    #wynik = []
    vertex = []
    for x in range(v):
        vertex.append(x)
        vertex[x] = Node(x)

    while i < v-1 and j < e:
        begin = graph[j][1]
        destiny = graph[j][2]
        value = graph[j][0]

        if l <= value <= r:
            b_parent = find(vertex[begin])
            d_parent = find(vertex[destiny])
            if b_parent != d_parent:
                union(b_parent, d_parent)
                #wynik.append((begin, destiny, graph[j][0] ))
                begin_min = min(value, begin_min)
                destiny_max = max(value, destiny_max)
                i += 1
        j += 1


    if i != v-1:
        coherent = False
    # visited = [False for _ in range(v)]
    # visited[G[0][0][1]] = True
    # path = [0]
    # coherent = dfs(G, 0, visited, path, v, l, r)
    # return destiny_max - begin_min
    return begin_min, destiny_max, coherent


def highway( A ):
    v = len(A)
    graph = []
    create(A, v, graph)
    e = len(graph)
    graph.sort()
    G = create_dfs(A, v)




    print(kruskal(graph, v, e, 8, 30, G))
    ret = None
    return ret

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = False )
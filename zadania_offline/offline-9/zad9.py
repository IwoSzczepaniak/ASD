# Iwo Szczepaniak
from zad9testy import runtests
from collections import deque


# Alogorytm oparty na metodzie Forda-Fulkersona wraz z modyfikacją dodającą sztuczną krawędź o pojemności INF,
# po to, by dla wszystkich dwóch krawędzi sprawdzić max_flow. Funkcja vertex liczy ilość wierzchołków w grafie, a
# funkcja matrix, tworzy reprezentację macierzową. BFS, o ile dotrze do pola sink, zwraca przepływ dla danej ścieżki,
# a ich suma daje max_flow. Ścieżki nie pokrywają się dzięki użyciu grafu rezydialnego (Ford-Fulkerson),
# a while wykonuje się do momentu gdy bfs dociera do końca tzn. gdy w grafie istnieją jeszcze niewykorzystane przepływy.

#Szacowana złożoność czasowa: f * V^3
#Szacowana złożoność pamięciowa: V^2

def vertex(G):
    ret = [G[0][0]]
    for x in G:
        if x[1] not in ret:
            ret.append(x[1])
        if x[0] not in ret:
            ret.append(x[0])
    return len(ret)


def matrix(G, graph):
    for i in range(len(G)):
        graph[G[i][0]][G[i][1]] = G[i][2]


def bfs(s, sink, parents, residual, ver):
    visited = [False for _ in range(ver)]
    visited[s] = True
    parents[s] = -1
    d_queue = deque()
    min_cap = 10**10
    d_queue.append((s, min_cap))

    while d_queue:
        u, capacity = d_queue.popleft()
        for x in range(ver):
            if residual[u][x] != 0:
                if not visited[x]:
                    parents[x] = u
                    visited[x] = True
                    min_cap = min(capacity, residual[u][x])
                    if x == sink:
                        return min_cap
                    d_queue.append((x, min_cap))


def ford_fulk(graph, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    residual = [graph[i][:] for i in range(ver)]
    max_flow = 0

    min_cap = bfs(source, sink, parent, residual, ver)
    while min_cap:
        max_flow += min_cap
        u = sink
        while u != source:
            v = parent[u]
            residual[u][v] += min_cap
            residual[v][u] -= min_cap
            u = v
        min_cap = bfs(source, sink, parent, residual, ver)
    return max_flow


def highway( G,s ):
    ver = vertex(G) + 1
    graph = [[0 for _ in range(ver)] for _ in range(ver)]
    matrix(G, graph)
    maxik = 0

    graph_c = [graph[i][:] for i in range(ver)]
    visited = [[False for _ in range(ver)] for _ in range(ver)]
    sink = ver - 1
    for i in range(sink):
        for j in range(sink):
            if not visited[j][i]:
                if j != s and i != s and i != j:
                    visited[i][j] = True
                    visited[j][i] = True
                    graph_c[i][sink] = 10**20
                    graph_c[j][sink] = 10**20
                    maxik = max(maxik, ford_fulk(graph_c, s, sink, ver))
                    graph_c[i][sink] = 0
                    graph_c[j][sink] = 0

    return maxik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
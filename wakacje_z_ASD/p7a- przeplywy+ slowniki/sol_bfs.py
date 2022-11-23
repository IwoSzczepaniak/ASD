from egzP7atesty import runtests 
from collections import deque
from math import inf


def bfs(source, sink, parents, residual):
    ver = len(residual)
    visited = [False for _ in range(ver)]
    visited[source] = True
    parents[source] = -1
    d_queue = deque()
    min_cap = inf
    d_queue.append((source, min_cap))

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
    return None


def Ford_Fulk(graph, source, sink):
    ver = len(graph)
    parent = [-1 for _ in range(ver)]
    residual = [graph[i][:] for i in range(ver)]
    max_flow = 0

    min_cap = bfs(source, sink, parent, residual)
    while min_cap:
        max_flow += min_cap
        u = sink
        while u != source:
            par_u = parent[u]
            residual[par_u][u] -= min_cap # krawędź z dfs'a, która zabiera część przepływu
            residual[u][par_u] += min_cap # krawędź cofająca przepływ
            u = par_u
        min_cap = bfs(source, sink, parent, residual)
    return max_flow


def akademik( T ): # od 0 do n1 ludzie, od n1+1 do 2*n1 pokoje o tych samych indeksach
    s = len(T)*2
    t = s + 1
    n = t + 1
    n1 = len(T)

    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n1):
        for j in range(3):
            if T[i][j] is not None:
                G[i][n1 + T[i][j]] = 1
    for i in range(n1):
        G[s][i] = 1
        G[n1+i][t] = 1

    pustych = 0
    for i in range(n1):
        if T[i] == (None,None,None):
            pustych += 1

    happy = Ford_Fulk(G, s, t)

    return n1 - happy - pustych
runtests ( akademik )

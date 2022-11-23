from zad9testy import runtests
from collections import deque


def vertex(G):
    ret = [G[0][0]]
    for x in G:
        if x[1] not in ret:
            ret.append(x[1])
        if x[0] not in ret:
            ret.append(x[0])
    return len(ret)


def bfs(graph, ver, s, t, parent):
    visited = [False for _ in range(ver)]
    d_queue = deque()
    d_queue.append(s)
    visited[s] = True
    while d_queue:
        u = d_queue.popleft()
        for neigh in graph[u]:
            if not visited[neigh[0]]:
                d_queue.append(neigh[0])
                visited[neigh[0]] = True
                parent[neigh[0]] = u
    if visited[t-1]:
        return True
    return False


def ford_fulk(graph, ver, source, sink):
    parent = [-1 for _ in range(ver)]
    residual = graph.copy()
    max_flow = 0
    min_cap = 0

    while bfs(residual, ver, source, sink, parent):
        max_flow += min_cap
        u = sink
        while u != source:
            v = parent[v]
            graph[u][v] += path_flow # DO NAPRAWY ostrej
            graph[v][u] -= path_flow # DO NAPRAWY ostrej
            u = v

    return max_flow


def create(G, ver):
    n = len(G)
    graph = [[0 for _ in range(ver+1)] for _ in range(ver+1)]
    for i in range(n):
        for j in range(n):
            if G[j][0] == i:
                graph[i][G[j][1]] = G[j][2]
    return graph


def highway( G,s ):
    e = len(G)
    ver = vertex(G)
    m_flow = -1

    for i in range(ver):
        for j in range(ver):
            if i != j:
                gcopy = G.copy()
                gcopy.append((i, ver, 10**10))
                gcopy.append((j, ver, 10**10))
                graph = create(gcopy, ver)
                m_flow = max(m_flow, ford_fulk(graph, ver, s, ver))

    return m_flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = False )
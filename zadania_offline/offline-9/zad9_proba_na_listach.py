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


def bfs(s, sink, parents, residual, ver):
    visited = [False for _ in range(sink+1)]
    visited[s] = True
    parents[s] = -1
    d_queue = deque()
    d_queue.append(s)
    min_cap = 10**10

    while d_queue:
        u = d_queue.popleft()
        for x in residual[u]:
            if x[0] is not None and not visited[x[0]]:
                parents[x[0]] = u
                visited[x[0]] = True
                min_cap = min(min_cap, x[1])
                if x[0] == sink:
                    return min_cap
                d_queue.append((x[0]))


def ford_fulk(graph, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    residual = [[graph[i][j] for j in range(len(graph[i]))] for i in range(ver)]
    max_flow = 0

    min_cap = bfs(source, sink, parent, residual, ver)
    while min_cap:
        max_flow += min_cap
        u = sink
        while u != source:
            v = parent[u]
            for i in range(len(residual[u])):
                if residual[u][i][0] == v:
                    residual[u][i][1] += min_cap
            for i in range(len(residual[v])):
                if residual[v][i][0] == u:
                    residual[v][i][1] -= min_cap
            u = v
        min_cap = bfs(source, sink, parent, residual, ver)

    return max_flow


def list(G, ver):
    n = len(G)
    graph = [[] for _ in range(ver)]
    cnt = 0
    for i in range(n):
        graph[G[i][0]].append([G[i][1], G[i][2]])
        cnt += 1
    return graph, cnt


def highway( G,s ):
    ver = vertex(G) + 1
    graph, e = list(G, ver)
    maxik = 0

    graph_c = [[graph[i][j] for j in range(len(graph[i]))] for i in range(ver)]
    visited = [[False for _ in range(ver)] for _ in range(ver)]
    sink = e + 1
    for i in range(ver):
        for j in range(ver):
            if not visited[j][i]:
                if i != j and i != s and j != s:
                    visited[i][j] = True
                    visited[j][i] = True
                    graph_c[i].append([e+1, 10**20])
                    graph_c[j].append([e+1, 10**20])
                    maxik = max(maxik, ford_fulk(graph_c, s, sink, ver))
                    graph_c[i].pop()
                    graph_c[j].pop()

    return maxik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
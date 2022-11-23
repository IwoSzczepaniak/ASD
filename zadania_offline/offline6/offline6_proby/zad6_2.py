from zad6testy import runtests
from collections import deque


def paths(v, parents):
    x = []
    while parents[v][0] != v:
        x.append(v)
        v = parents[v][0]
    x.append(v)
    return reversed(x)


def cut(v, parents, G):
    while parents[v][1] != INF and parents[v][1] != parents[v][0]:
        v = parents[v][0]
    if parents[v][0] == v:
        return None
    else:
        # wyjeb krawedz od parent[v] do v
        par = parents[v][0]
        G[v].remove(par)
        G[par].remove(v)


def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [(-1, INF) for _ in range(n)]

    visited[s] = True
    parents[s] = (s, INF)
    queue = deque()
    queue.append(s)

    while queue:
        v = queue.popleft()
        for x in G[v]:
            if not visited[x]:
                parents[x] = (v, INF)
                visited[x] = True
                queue.append(x)
            else:
                tmp = parents[x]
                parents[x] = (tmp[0], min(tmp[1], v))
    paths(t, parents)

    paths(t,parents)
    return (0,0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = False )
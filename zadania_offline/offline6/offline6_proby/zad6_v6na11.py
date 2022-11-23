from zad6testy import runtests
from collections import deque


def paths(s, v, parents):
    x = []
    while parents[v] != v:
        x.append(v)
        v = parents[v]
    x.append(v)
    if x[0] == s:
        return reversed(x)
    return None


def bfs(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]

    visited[s] = True
    parents[s] = s
    queue = deque()
    queue.append(s)

    cnt_paths_to_t = 0

    while queue and not visited[t]:
        v = queue.popleft()
        for x in G[v]:
            if not visited[x]:
                parents[x] = v
                visited[x] = True
                queue.append(x)
                if x == t:
                    cnt_paths_to_t += 1

    #ściagnac wszystko z obecnej kolejki
    while queue:
        v = queue.popleft()
        for x in G[v]:
            if x == t:
                cnt_paths_to_t += 1

    # jeśli jedna kraw. dochodzi do konca, to usuwamy ją
    if cnt_paths_to_t == 1:
        ret = (parents[t], t)
        return ret
    # jeśli żadna kraw nie dochodzi do końca, return None
    elif cnt_paths_to_t == 0:
        return None

    #bfs od tylu, jak dotrze do s, to znaczy ze nie ma krawedzi do usuniecia.

def longer(G, s, t):
    return bfs(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
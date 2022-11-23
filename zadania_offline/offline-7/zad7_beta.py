# Iwo Szczepaniak
from zad7testy import runtests
from collections import deque
timer = 0


def spojny(G, n):
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visited[0] = True
    parents[0] = -1
    d_queue = deque()
    d_queue.append(0)

    while d_queue:
        v = d_queue.popleft()
        for w in G[v]:
            for x in w:
                if not visited[x]:
                    parents[x] = v
                    visited[x] = True
                    d_queue.append(x)
    for i in range(n):
        if not visited[i]:
            return False
    return True


def dfs(G, v, visited, curr_t, gate_in):
    global timer
    visited[v] = True
    curr_t[v] = timer
    timer += 1
    gate_out = (1 - gate_in)

    path.append(v)



    for w in G[v][gate_out]: # in sasiedzi z innej bramy powinno byc
        if not visited[w]:
            if v in G[w][0]:
                tmp = 0
            else:
                tmp = 1
            dfs(G, w, visited, curr_t, tmp)

            if curr_t[v] + 1 < curr_t[w]:



def hamilton(G, v, visited, path, gate_in, n):
    if len(path) == n:
        return True
    gate_out = (1 - gate_in)

    for w in G[v][gate_out]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            if v in G[w][0]:
                tmp = 0
            else:
                tmp = 1
            if hamilton(G, w, visited, path, tmp, n):
                return True
            visited[w] = False
            path.remove(w)
    return None


def droga( G ):
    n = len(G)
    if not spojny(G, n):
        return None
    # sprawdzanie czy spójny

    visited = [False for i in range(n)]
    curr_t = [None for i in range(n)]
    start = 0
    visited[start] = True
    path = [start]



    dfs(G, 0, visited, curr_t, 0)

    return True





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
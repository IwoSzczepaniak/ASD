from egzP5btesty import runtests 
time = 0


def dfs(G, ART, low, discovery, parents, v):
    global time
    children = 0 # tylko dla korzenia
    time += 1
    low[v] = time
    discovery[v] = time

    for s in G[v]:
        if discovery[s] is None:
            children += 1 # tylko dla korzenia
            dfs(G, ART, low, discovery, parents, s)
            if low[s] >= discovery[v]:
                ART[v] = True
            low[v] = min(low[v], low[s])
        else:
            low[v] = min(low[v], discovery[s])
    return children # tylko dla korzenia


def artic(G):
    global time
    n = len(G)
    ART = [False for _ in range(n)]
    low = [None for _ in range(n)]
    discovery = [None for _ in range(n)]
    parents = [None for _ in range(n)]

    for i in range(n):
        if discovery[i] is None:
            if dfs(G, ART, low, discovery, parents, i) > 1: # tylko dla korzenia, wtedy wkw
                ART[i] = True
            else:
                ART[i] = False
    points = 0
    for i in range(n):
        if ART[i]:
            points += 1
    return points


def koleje ( B ):
    n = 0
    for i in range(len(B)):
        if B[i][0]>B[i][1]:
            B[i] = (B[i][1], B[i][0])
            n = max(n, B[i][1])
    n += 1 # ilość wiec 0 też
    B.sort(key = lambda x: (x[0], x[1]))

    G = [[] for _ in range(n)]
    last = None
    for i in range(len(B)):
        if last != B[i]:
            last = B[i]
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])
    return artic(G)

runtests ( koleje, all_tests=True )
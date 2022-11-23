from egzP7atesty import runtests
from math import inf


def dfs_visit(G, GP, V, P, i):
    V[i] = True
    for nb in G[i]:
        idd = str(i) + "_" + str(nb)
        if not V[nb] and GP[idd] != 0:
            P[nb] = i
            dfs_visit(G, GP, V, P, nb)


def dfs(G, GP, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, GP, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    GP = {}
    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(u) + "_" + str(G[u][v])
            iddBack = str(G[u][v]) + "_" + str(u)
            GP[idd] = 1
            if GP.get(iddBack) is None:
                GP[iddBack] = 0

    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(G[u][v]) + "_" + str(u)
            if GP[idd] == 0:
                G[G[u][v]].append(u)

    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, GP, s, t, P):
        curr_flow = inf
        current = t
        while current != s:
            curr_flow = min(curr_flow, GP[str(P[current]) + "_" + str(current)])
            current = P[current]
        max_flow += curr_flow
        v = t
        while v != s:
            u = P[v]
            GP[str(u) + "_" + str(v)] -= curr_flow
            GP[str(v) + "_" + str(u)] += curr_flow
            v = P[v]
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
                G[i].append(n1 + T[i][j])
    for i in range(n1):
        G[s].append(i)
        G[n1+i].append(t)

    pustych = 0
    for i in range(n1):
        if T[i] == (None, None, None):
            pustych += 1

    happy = Ford_Fulk(G, s, t)

    return n1 - happy - pustych


runtests ( akademik )

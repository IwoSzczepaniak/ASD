from egzP7atesty import runtests
from math import inf


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in range(len(G)):
        if not V[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, V, P, nb)


def dfs(G, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, s, t, P):
        curr_flow = inf
        current = t
        while current != s:
            curr_flow = min(curr_flow, G[P[current]][current])
            current = P[current]
        max_flow += curr_flow
        v = t
        while v != s:
            u = P[v]
            G[u][v] -= curr_flow
            G[v][u] += curr_flow
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

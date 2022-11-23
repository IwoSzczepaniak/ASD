from egzP1btesty import runtests
from math import inf
from queue import PriorityQueue


def relax(u, v, dist, prev, w, L):
    if v == L:
        copy_u = u
        cnt = 0
        while copy_u is not None:
            copy_u = prev[copy_u]
            cnt += 1
        if cnt == 3:
            dist[L] = min(dist[L], dist[u] + w)
    else:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            prev[v] = u


def Bell_Ford(G, s, dist, n, prev, L): # prev by dawał usprawnienie
    dist[s] = 0
    for _ in range(n-1):
        for x in G:
            relax(x[0], x[1], dist, prev, x[2], L)
    return dist[L]


def turysta( G, D, L ):
    n = G[0][1]
    for i in range(len(G)): n = max(n, G[i][1])
    dist = [inf for _ in range(n+1)]
    prev = [None for _ in range(n+1)]
    return Bell_Ford(G, D, dist, n, prev, L)





runtests ( turysta )

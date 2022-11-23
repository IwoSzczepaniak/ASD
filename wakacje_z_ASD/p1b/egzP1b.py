from egzP1btesty import runtests
from queue import PriorityQueue
from math import inf


def dijkstra(GP, D, L, cost, visited, parent, neighb):
    pq = PriorityQueue()
    cost[D] = 0
    pq.put((cost[D], D))

    while not pq.empty():
        (current_cost, u) = pq.get()
        visited[u] = True
        for v in neighb[u]:
            if visited[v] is None:
                if v == L:
                    v_is_L(u, v, GP, pq, cost, parent)
                else:
                    new_cost = GP[(u, v)] + cost[u]
                    if new_cost < cost[v]:
                        cost[v] = new_cost
                        parent[v] = u
                        pq.put((cost[v], v))
    return cost[L]


def v_is_L(u, v, GP, pq, cost, parent):
    par = parent[v]
    cnt = 2
    while par is not None:
        par = parent[v]
        cnt += 1
    if cnt == 5:
        new_cost = GP[(u, v)] + cost[u]
        if new_cost < cost[v]:
            cost[v] = new_cost
            parent[v] = u
            pq.put((cost[v], v))


def turysta( G, D, L ):
    GP = {}
    n = 0
    for i in range(len(G)):
        GP[(G[i][0], G[i][1])] = G[i][2]
        n = max(n, G[i][1])
    n += 1
    Neighbours = [[] for _ in range(n)]
    for i in range(len(G)): Neighbours[G[i][0]].append(G[i][1])
    cost = [inf for _ in range(n)]
    visited = [None for _ in range(n)]
    parent = [None for _ in range(n)]

    return dijkstra(GP, D, L, cost, visited, parent, Neighbours)




runtests ( turysta )

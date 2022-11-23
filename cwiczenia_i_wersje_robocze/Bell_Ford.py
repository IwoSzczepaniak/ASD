def relax(u, v, dist, G):
    dist[v] = min(dist[v], dist[u] + G[u][v])


def Bell_Ford(G, s, dist, n, prev): # prev by dawał usprawnienie
    dist[s] = 0
    for _ in range(n-1):
        for v in range(n):
            for u in range(n): # v is neighbour
                if G[u][v] != 0:
                    relax(u, v, dist, G)
    return dist


if __name__ == '__main__':
    n = 6
    graph = [ [0, 10, 0, 0, 0, 8],
              [0, 0, 0, 2, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, -2, 0, 0, 0],
              [0, -4, 0, -1, 0, 8],
              [0, 0, 0, 0, 1, 0]]
    s = 0
    dist = [10**10 for _ in range(n)]
    prev = [None for _ in range(n)]
    print(Bell_Ford(graph, s, dist, n, prev))


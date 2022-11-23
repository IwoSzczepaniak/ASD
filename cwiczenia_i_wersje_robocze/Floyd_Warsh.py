def Floyd_Warsh(dist, n):
    for k in range(n):
        for u in range(n):
            for v in range(n): # v is neighbour
                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]
    return dist


if __name__ == '__main__':
    n = 4
    inf = 10*10
    graph = [ [0, inf, -2, inf],
              [4, 0, 2, inf],
              [inf, inf, 0, 2],
              [inf, -1, inf, 0]]

    T = Floyd_Warsh(graph, n)
    for r in T:
        for c in r:
            print(c, end=" ")
        print()

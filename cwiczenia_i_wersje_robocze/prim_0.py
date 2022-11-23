from queue import PriorityQueue


def prim(G, s, visited, cost, parent):
    n = len(G)
    pq = PriorityQueue()
    pq.put((0, s))
    cost[s] = 0
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited[current_vertex] = True
        for i in range(n):
            if G[current_vertex][i] != 0 and not visited[i]:
                    pq.put((G[current_vertex][i], i))
                    if cost[i] > G[current_vertex][i]:
                        cost[i] = G[current_vertex][i]
                        parent[i] = current_vertex
    return parent


if __name__ == '__main__':
    n = 7
    graph = [ [0, 2, 3, 3, 0, 0, 0],
              [2, 0, 4, 0, 3, 0, 0],
              [3, 4, 0, 5, 1, 6, 0],
              [3, 0, 5, 0, 0, 7, 0],
              [0, 3, 1, 0, 0, 8, 0],
              [0, 0, 6, 7, 8, 0, 9],
              [0, 0, 0, 0, 0, 9, 0]]
    s = 0

    visited = [False for _ in range(n)]
    cost = [10 ** 10 for _ in range(n)]
    parent = [0 for _ in range(n)]
    print(prim(graph, s, visited, cost, parent))


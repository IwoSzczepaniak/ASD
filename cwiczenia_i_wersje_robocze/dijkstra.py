from queue import PriorityQueue


def dijkstra(G, s, visited, cost):
    n = len(G)
    pq = PriorityQueue()
    pq.put((0,s))
    cost[s] = 0
    while not pq.empty():
        (current_cost, current_vertex_nr) = pq.get()
        visited[current_vertex_nr] = True
        for i in range(n):
            if G[current_vertex_nr][i] != 0:
                if not visited[i]:
                    distance = G[current_vertex_nr][i]
                    new_cost = distance + current_cost
                    old_cost = cost[i]
                    if new_cost < old_cost:
                        pq.put((new_cost, i))
                        cost[i] = new_cost
                        parent[i] = current_vertex_nr
    return cost


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

    visited = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    cost = [10**10 for _ in range(n)]
    print(dijkstra(graph, s, visited, cost))


def ile_cyfr(str):
    cnt = 0
    for i in str:
        if i.isdigit():
            cnt += 1
    return cnt

if __name__ == '__main__':
    # a = '1j429jjzpvk09f04h9y2ju5he7'
    # b = '7zw6hkyjc2vsriag6ivh4tfbd'
    # print(len(a) - len(b))
    # print(ile_cyfr(a))
    # print(ile_cyfr(b))

    p = [1,2,3]
    while p:
        print(p.pop())













def Floyd_Warsh(dist, n):
    for k in range(n):
        for u in range(n):
            for v in range(n): # v is neighbour
                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]
    return dist









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










def dijkstra(G, s, visited, cost):
    n = len(G)
    pq = PriorityQueue()
    pq.put((0,s))
    cost[s] = 0
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited[current_vertex] = True
        for i in range(n):
            if G[current_vertex][i] != 0:
                distance = G[current_vertex][i]
                if not visited[i]:
                    new_cost = distance + dist
                    old_cost = cost[i]
                    if new_cost < old_cost:
                        pq.put((new_cost, i))
                        cost[i] = new_cost
    return cost













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
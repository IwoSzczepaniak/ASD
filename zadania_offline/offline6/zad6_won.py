# Iwo Szczepaniak
from zad6testy import runtests
from collections import deque
timer = 1

# Algorytm grafowy liczący zadany problem.

# Pomysł na algorytm: Używając bfs, dojeżdżamy do końca najkrótszej ścieżki oraz do końca tej fali.
# Jeśli ilość ścieżek = 1, usuwamy krawędź (t, parents[t]), jeśli ilość to 0, to zwracamy None
# Jeśli inna liczba ścieżek używamy dfs i sprawdzamy czy istieje most na ścieżce, jeśli tak, usuwamy go.
# Jeśli nie ma mostu, usuwamy po kolei krawędzie ze ścieżki wynikowej i sprawdzamy, czy skróciła się ścieżka.
# Szacowana złożoność czasowa: V + E
# Złożoność pamięciowa: V


def dfs_bridge(G, v, visited, curr_t, low_t, parent, bridges):
    global timer
    visited[v] = True
    curr_t[v] = timer
    low_t[v] = timer
    timer += 1
    # Dla v: w to dzieci, a parent to ojciec
    for w in G[v]:
        if not visited[w]:
            dfs_bridge(G, w, visited, curr_t, low_t, v, bridges)
            if curr_t[v] < low_t[w] and v in G[w]:
                bridges.append((v, w))
                return
            low_t[v] = min(low_t[v], low_t[w])
        else:
            if w != parent:
                low_t[v] = min(low_t[v], curr_t[w])


def shortest_path(G, s, t):
    path_list = [[s]]
    path_index = 0
    visited = [s]
    if s == t:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_vert = current_path[-1]
        next_verts = G[last_vert]
        if t in next_verts:
            current_path.append(t)
            return current_path
        for next_vert in next_verts:
            if not next_vert in visited:
                new_path = current_path[:]
                new_path.append(next_vert)
                path_list.append(new_path)
                visited.append(next_vert)
        path_index += 1
    return []


def brutal(G, s, t):
    shortest = shortest_path(G, s, t)
    length = len(shortest)

    for i in range(length - 1, 0, -1):
        vertex = shortest[i]
        edges = G[vertex]
        temp = edges
        temp.pop(edges.index(shortest[i - 1]))
        G[vertex] = temp
        check = shortest_path(G, t, s)
        if len(check) > length or check == []:
            return (shortest[i - 1], vertex)
        else:
            G[vertex] = edges
    return None


def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visited[s] = True
    parents[s] = -1
    d_queue = deque()
    d_queue.append(s)
    cnt_paths_to_t = 0
    Fala = [None for _ in range(n)]
    Fala[s] = 0
    fala_koncowa = -1

    while d_queue and not visited[t]:
        v = d_queue.popleft()
        for x in G[v]:
            if not visited[x]:
                parents[x] = v
                visited[x] = True
                Fala[x] = Fala[v] + 1
                d_queue.append(x)
                if x == t:
                    cnt_paths_to_t += 1
                    fala_koncowa = Fala[v]

    #ściagnac z kolejki tak, żeby nadal pozostawac w tej samej "fali bfs'a"
    while d_queue:
        v = d_queue.popleft()
        for x in G[v]:
            if x == t and fala_koncowa == Fala[v]:
                cnt_paths_to_t += 1

    # jeśli tylko jedna krawędź dochodzi do konca, to po prostu usuwamy ją
    if cnt_paths_to_t == 1:
        ret = (parents[t], t)
        return ret
    # Jeśli nie ma ścieżki do końca zwracamy None
    elif cnt_paths_to_t == 0:
        return None
    else:
        visited_bfs = [False for i in range(n)]
        curr_t = [None for i in range(n)]
        low_t = [None for i in range(n)]
        bridges = []
        dfs_bridge(G, 0, visited_bfs, curr_t, low_t, -1, bridges)

        if not bridges:
            return brutal(G, s, t)
        else:
            return bridges[0]

runtests( longer, all_tests = True )

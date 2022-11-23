# Iwo Szczepaniak
from zad6testy import runtests
from collections import deque
timer = 1

# Algorytm grafowy liczący zadany problem.
# Pomysł na algorytm: Używając bfs, dojeżdżamy do końca ścieżki, następnie używamy bfs i sprawdzamy czy istieje
# most, jeśli tak, usuwamy go. W przeciwnym razie usuwamy po kolei kawałki ze ścieżki wynikowej i sprawdzamy,
# czy skróciła się ścieżka.
# Szacowana złożoność czasowa: n
# Złożoność pamięciowa: n


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


def paths(v, parents):
    tab = []
    wyn = []
    while parents[v] != -1:
        tab.append(v)
        v = parents[v]
    tab.append(v)
    n = len(tab)
    for i in range(n-1):
        wyn.append((tab[i], tab[i+1]))
    return wyn


def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visited[s] = True
    parents[s] = -1
    queue = deque()
    queue.append(s)
    cnt_paths_to_t = 0
    Fala = [None for _ in range(n)]
    Fala[s] = 0
    fala_koncowa = -1

    while queue and not visited[t]:
        v = queue.popleft()
        for x in G[v]:
            if not visited[x]:
                parents[x] = v
                visited[x] = True
                Fala[x] = Fala[v] + 1
                queue.append(x)
                if x == t:
                    cnt_paths_to_t += 1
                    fala_koncowa = Fala[v]

    #ściagnac z obecnej kolejki tak, żeby nadal pozostawac w tej samej "fali bfs'a"
    while queue:
        v = queue.popleft()
        for x in G[v]:
            if x == t and fala_koncowa == Fala[v]:
                cnt_paths_to_t += 1

    # jeśli tylko jedna krawędź dochodzi do konca, to po prostu usuwamy ją
    if cnt_paths_to_t == 1:
        ret = (parents[t], t)
        return ret

    else:
        visited_bfs = [False for i in range(n)]
        curr_t = [None for i in range(n)]
        low_t = [None for i in range(n)]
        bridges = []
        dfs_bridge(G, 0, visited_bfs, curr_t, low_t, -1, bridges)

        if not bridges:
            print(paths(t, parents))
            wynik = paths(t, parents)
            for k in wynik:
                first = k[0]
                second = k[1]
                G2 = [item[:] for item in G]

            return None

        return bridges[0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
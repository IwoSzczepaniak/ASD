from zad6testy import runtests
from collections import deque


def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    visited[s] = True
    parents[s] = -1
    queue = deque()
    queue.append(s)
    cnt_paths_to_t = 0

    while queue and not visited[t]:
        v = queue.popleft()
        for x in G[v]:
            if not visited[x]:
                parents[x] = v
                visited[x] = True
                queue.append(x)
                if x == t:
                    cnt_paths_to_t += 1
                    par = parents[v]

    #ściagnac z obecnej kolejki tak, żeby nadal pozostawac w tej samej "fali bfs'a"
    while queue:
        v = queue.popleft()
        for x in G[v]:
            if x == t and par == parents[v]:
                cnt_paths_to_t += 1

    # jeśli tylko jedna krawędź dochodzi do konca, to po prostu usuwamy ją
    if cnt_paths_to_t == 1:
        ret = (parents[t], t)
        return ret

    else:
        return None
        # dfs od tylu, jak znajdzie most na x, wtedy usuwa tą krawędź,
        # a jak dotrze do s nie znajdując mostu na x, to znaczy ze nie ma krawedzi do usuniecia, zwaca None.

'''
        visited2 = [False for _ in range(n)]
        parents2 = [None for _ in range(n)]

        visited2[t] = True
        parents2[t] = t
        queue2 = deque()
        queue2.append(t)

        while queue2 and not visited2[s]:
            v = queue.popleft()
            for x in G[v]:
                if not visited2[x]:
                    parents2[x] = v
                    visited2[x] = True
                    queue2.append(x)
                    if x == s:
                        return None'''



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
from queue import PriorityQueue
  

def dijkstry(G, s):
    n = len(G)
    d = [10**10 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [None for _ in range(n)]
    d[s] = 0
    parent[s] = s
    tovisit = PriorityQueue()
    tovisit.put(d[s], s)

    while tovisit:
        curr = tovisit.get()
        curr_num = curr[1]
        visited[curr_num] = True
        for v, w in G[curr_num]:
            if visited[v]:
                if d[v] > d[curr_num] + w:
                    d[v] = d[curr_num] + w
                    parent[v] = curr_num
            else:
                tovisit.put(d[v], v)

################## MOŻE BYĆ MOCNO ŹLE, SPAWDZIĆ !!!!!!!!!!!!!!!!!!!!!!!!!!

def MST(G):
    n = len(G)
    E = []
    INF = 10**10
    for i in range(n):
        for j in range(n):
            if G[i][j] < INF:
                E.append(G[i, j], i, j)
    E.sort()
    S = [make.set(i) for i in range(n)]
    T = []
    for -,p,q in E:
        if find_set(S[p]) != find_set[S[q]]
            T.append((p,q))
            union_st(S[p], S[q])
    return T

###  Z WYKŁADU

################## W ACYKLICZNYM GRAFIE SKIEROWANYM ZNALEŹĆ ŚCIEŻKĘ HAMILTONA
# MOŻNA POSORTOWAĆ TOPOLOGICZNIE


#### WIERZCHOŁEK W GRAFIE SKIEROWANYM NAZYWAMY DOBRYM POCZĄTKIEM, JEŚLI KAŻDY WIERZCHOŁEK MOŻNA OSIĄGNĄĆ IGĄC
# ŚCIEŻKĄ SKIROWANĄ


#### MAMY DANY NIESKIEROWANY GRAF WAŻONY, DODATNIMI DUZYM LICZBAMI RZECZYWISTYMI. TAK, BY ILOCZYN BYŁ NAJMNIEJSZY.
# LOGARYTMY






















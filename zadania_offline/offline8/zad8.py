# Iwo Szczepaniak
from zad8testy import runtests
from math import sqrt

# Algorytm początkowo tworzy funkcją create z podanych wierzchołków graf pełny z parametrami:
# distance(funkcja distance), source(z), destination(do). Następnie korzystając z algorytmu Kruskala liczymy
# drzewo rozpinające, usuwając za każdym razem krawędzie o najniższej wadze. Funkcja Kruskal jest skonstruowana tak,
# by badać przy okazji spójność drzewa(coherent), zwracając wyniki tylko dla tych drzew, które są spójne
# i usuwać krawędzie z grafu.

# Jest to zachłanny program, liczący dla coraz mniejszego (od dołu) zakresu długości wierzchołków drzewo rozpinające,
# Usuwamy jedynie najkrótsze krawędzie - które w poprzednim minimalnym drzewie znalezły się -
# o ile były w optymalnym rozwiązaniu. Dlatego mimo wyrzucania krawędzi, nie omijamy żadnych przypadków.
# W ten spośob przejdziemy  wszystkie miniamalne drzewa rozpinające w zakresie (i,last),
# gdzie i to wszystkie liczby od 0 do last, a last to długość najdłuższej krawędzi.

# Szacowana złożoność pamięciowa: E / n^2
# Pesymistyczna złożoność obliczeniowa: E^2 logE / n^4 log(n^2)


def distance(A, i, j):
    dis = int(sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2)) + 1
    return dis


def create(A, n):
    graph = []
    for source in range(n):
        for destination in range(n):
            if destination != source:
                tmp = (distance(A, source, destination), source, destination)
                graph.append(tmp)
    return sorted(graph)


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(graph, v, e, l):
    i = 0
    coherent = False
    begin_min = 10**10
    destiny_max = -1
    vertex = []
    for x in range(v):
        vertex.append(Node(x))
    # value = graph[j][0]
    # begin = graph[j][1]
    # destiny = graph[j][2]]

    k = 0
    while l > graph[k][0]:
        del graph[k]
        k += 1
        e -= 1

    for j in range(k, e):
        b_parent = find(vertex[graph[j][1]])
        d_parent = find(vertex[graph[j][2]])
        if b_parent != d_parent:
            union(b_parent, d_parent)
            if graph[j][0] < begin_min:
                begin_min = graph[j][0]
            elif graph[j][0] > destiny_max:
                destiny_max = graph[j][0]
            i += 1
            if i == v - 1:
                coherent = True
                break

    return begin_min, destiny_max, coherent


def highway( A ):
    v = len(A)
    graph = create(A, v)
    res = graph[-1][0]
    for a in range(graph[-1][0]):
        tmp = kruskal(graph, v, len(graph), a + 1)
        n_res = tmp[1] - tmp[0]
        if tmp[2] and res > n_res:
            res = n_res
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
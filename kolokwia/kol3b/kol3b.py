# Iwo Szczepaniak
from kol3btesty import runtests
from queue import PriorityQueue

# Algorytm polega na modyfikacji podanego grafu funkcją modify_g poprzez rozszerzenie możliwych tras o wszystkie
# możliwe loty między lotniskami, wraz z kosztami takiej podróży. Następnie, aby obliczyć drogę między s a t,
# należy użyć algorytmu Dijkstry, który umożliwi nam odnalezienie najkrótszej trasy między s a t (zmodyfikuje
# distances tak, że na pozycji distances[t] zapisana jest szukana odległość).

# Szacowana złożoność pamięciowa: m*v
# Szacowana złożoność obliczeniowa: (m+n)*log(n)


# Aby poprawić złożoność, czyli dodawać mniej lotów, należałoby uzależnić ich występowanie od opłacalności względem
# podróży samochodem. To jednak osiągnięte może być algorytmem Floyda-Warshala, który ma złożoność n^3, więc finalnie
# pogorszyłoby złożoność. Zapewne jednak istnieje na to sprytniejszy sposób :). Funkcja Floyda Watshala została
# wykomentowana z racji niedokończenia tej ścieżki rozumowania przez autora

# def Floyd_Warsh(graph, A, n, d):
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     if d[i][j] > d[i][k] + d[j][k]:
#                         graph[i].append((j, A[i]+A[j]))
#                         d[i][j] = d[i][k] + d[j][k]


def modify_g(graph, A, n):
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append((j, A[i]+A[j]))


def relax(u, v, distances, dist):
    if distances[v] > distances[u] + dist:
        distances[v] = distances[u] + dist


def dijkstry(graph, s, distances, visited):
    pq = PriorityQueue()
    pq.put((0, s))
    distances[s] = 0
    while not pq.empty():
        tiem = pq.get()
        u = tiem[1]
        visited[u] = True
        for tmp in graph[u]:
            v = tmp[0]
            dist = tmp[1]
            if not visited[v]:
                relax(u, v, distances, dist)
                pq.put((distances[v], v))


def airports( G, A, s, t ):
    n = len(G)
    modify_g(G, A, n)
    distances = [10**10 for _ in range(n)]
    visited = [False for _ in range(n)]
    dijkstry(G, s, distances, visited)
    return distances[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )
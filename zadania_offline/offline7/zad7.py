# Iwo Szczepaniak
from zad7testy import runtests


# Algorytm opierający się na funkcji DFS, wraz z modyfikacją - backtrackingiem - pozwalającą na 'poprawienie' ścieżki
# DFS'a poprzez cofnięcie się do sąsiada którego zostawiono poza ścieżką i przejście przez ten wierzchołek, co umożliwia
# przejście przez wszystkie krawędzie, o ile to możliwe. Funckję zmieniono też tak, by zapamiętywać bramę wejściową.
#
# Aby uzyskac rozwiązanie, tworzymy potrzebną tablicę visited, wynikową listę path i puszczamy funckję hamilton
# dla bramy 0 i bramy 1, jeśli żadna nie zwróci True, wtedy nie ma ścieżki i zwracane jest None. Jeśli istnieje
# rozwiązanie funkcja hamilton modygfikuję path tak, by można było zwrócić ją jako wynik.
#
# Szacowana złożoność pamięciowa: V
# Pesymistyczna złożoność obliczeniowa: V!


def hamilton(G, v, visited, path, gate_in, n):
    if len(path) == n:
        return True
    gate_out = (1 - gate_in)

    for w in G[v][gate_out]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            if v in G[w][0]:
                tmp = 0
            else:
                tmp = 1
            if hamilton(G, w, visited, path, tmp, n):
                return True
            visited[w] = False
            path.pop()
    return None


def droga( G ):
    n = len(G)
    visited = [False for i in range(n)]
    start = 0
    # jako start można też dać randint(0,n-1)
    visited[start] = True
    path = [start]

    if hamilton(G, start, visited, path, 1, n):
        last = path[n-1]
        if last in G[start][1]:
            return path
    elif hamilton(G, start, visited, path, 0, n):
        last = path[n-1]
        if last in G[start][0]:
            return path
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
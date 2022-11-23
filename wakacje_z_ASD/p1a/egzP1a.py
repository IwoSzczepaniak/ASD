from egzP1atesty import runtests
from math import inf


def titanic( W, M, D ):
    letters = {}
    for i in range(len(M)): letters[M[i][0]] = M[i][1]
    message = str()
    for i in range(len(W)): message += letters[W[i]]
    available = set()
    for i in range(len(D)): available.add(M[D[i]][1])

    n = len(message)
    F = [inf for _ in range(n+1)]
    F[0] = 0
    for i in range(1, n+1):
        F[i] = F[i-1] + 1 # linijka dla czytelności
        j = i-1
        while j >= 0 and j >= i-4:
            if message[j:i] in available:
                F[i] = min(F[i], F[j] + 1)
            j -= 1
    return F[n]


runtests ( titanic, recursion=False)

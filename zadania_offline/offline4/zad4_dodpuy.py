# Iwo Szczepaniak
from zad4testy import runtests
'''
Algorytm dynamiczny, oparty na zasadzie działania knapsack'a, dodatkowo uwzględniając niepokrywanie się budynków.
W tym celu sortujemy Tmp, kopię T po wartości b, tak by sprawdzać jedynie czy nie przecina się z wartością a poprzednika.
Operujemy na tymczasowej tablicy Tmp. Po zakończeniu działania KS, funkcja wynik odtwarza indeks elementów
z pierwotnej tablicy T.
'''



def profit(T, i):
    return T[i][0] * (T[i][2] - T[i][1])


def Knapsack(F, T, p, i):
    if F[i][p] != -1:
        return F[i][p]
    if i < 0 or p <= 0:
        return 0

    w_i = T[i][3]
    result = -1

    if p - w_i > 0:
        j = i - 1
        while j >= 0 and T[i][1] <= T[j][2]:
            j -= 1
        result = profit(T, i) + Knapsack(F, T, p - w_i, j)
        result2 = Knapsack(F, T, p, i-1)
        result = max(result, result2)

    F[i][p] = result
    return result


def wynik(T,Tmp, F, i, b):
    j = i
    p = b
    Wyn = []

    while j > 0 and F[j - 1][p] == F[j][p]:
        j -= 1
    if j >= 0 and p >= Tmp[j][3]:
        Wyn.append(T.index(Tmp[j]))
        j -= 1
        p -= Tmp[j][3]

    for _ in range(i):
        while j > 0 and F[j-1][p] == F[j][p]:
            j -= 1
        if j >= 0 and p >= Tmp[j][3] and Tmp[j][2] < T[Wyn[-1]][1]:
            Wyn.append(T.index(Tmp[j]))
            j -= 1
            p -= Tmp[j][3]
        if j < 0:
            break

    return Wyn


def select_buildings(T, p):
    n = len(T)
    F = [[-1 for b in range(p + 1)] for i in range(n)]

    Tmp = T.copy()
    Tmp.sort(key=lambda x: (x[2], x[1]))

    Knapsack(F, Tmp, p, n-1)
    print(F[n-1][p])
    return wynik(T, Tmp, F, n-1, p)
runtests( select_buildings )
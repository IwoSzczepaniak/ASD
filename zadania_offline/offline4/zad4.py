# Iwo Szczepaniak
from zad4testy import runtests
'''
val - zwraca ilość studetnów
find_best - znajduje najlepszy przypadek dla danego przypadku
cleaner - czyści z nieporzebnych już -1 i znajduje indeksy z nieposortowanej listy

Algorytm rekurencyjny liczący zadany problem.
Sortujemy L, kopię T po wartości a i b, tak by sprawdzać jedynie czy nie przecina się z wartością a poprzednika.
Cały czas operujemy na tymczasowej tablicy L. Po zakończeniu działania find_best, 
funkcja cleaner odtwarza indeks elementów z pierwotnej tablicy T.
Szacowana złożonośc czasowa: 2^n 
Szacowana złożonośc pamięciowa: n 
'''


def val(X):
    return X[0] * (X[2] - X[1])


def find_best(L, Val, Tmp, i, p, prev_b, value):
    n = len(L)
    if i >= n:
        return value
    X = L[i]
    a = 0
    if p - X[3] >= 0 and X[1] > prev_b:
        a = find_best(L, Val, Tmp, i + 1, p - X[3], X[2], value + val(X))

    b = find_best(L, Val, Tmp, i + 1, p, prev_b, value)
    if b > a:
        if b > Val[i]:
            Val[i] = b
            Tmp[i] = -1
    else:
        if a > Val[i]:
            Val[i] = a
            Tmp[i] = i
    return Val[i]


def cleaner(Tmp, L, T):
    Tmp = [elem for elem in Tmp if elem != -1]
    Tmp2 = []
    for elem in Tmp:
        Tmp2.append(T.index(L[elem]))
    return Tmp2


def select_buildings(T, p):
    L = T.copy()
    L.sort(key=lambda x: (x[1], x[2]))
    n = len(L)
    V = [-1 for _ in range(n)]
    Tmp = [-1 for _ in range(n)]
    find_best(L, V, Tmp, 0, p, L[0][1] - 1, 0)
    return cleaner(Tmp, L, T)

runtests( select_buildings )

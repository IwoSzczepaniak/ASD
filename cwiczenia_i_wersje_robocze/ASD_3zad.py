#Iwo Szczepaniak
from zad3testy import runtests

'''
Iwo Szczepaniak

Pomysł na algorytm:
Funkcją maksi szukamy największego elementu w tablicy P. Na podstawie tej wielkości tworzymy funkcją bucket sort
kubełki. Następnie sortujemy je inserion sortem i łączymy ze sobą.

Ponieważ istnieje duża szansa, że będzie wśród kubełków wiele pustych - co wydłuza znacznie działanie -
a insertion nadal radzi sobie bardzo szybko przy idealnie równostajnym rozkładzie z sortowaniem około 10 elementów.
więc podział na n//10 kubełków jest bliski optymalnemu rozwiązaniu. 


Złożoność czasowa:
Dla bliskiego równostajnemu rozkładu ---> O = n
Bardzo pesymistyczne dane (niemal wszystkie dane w jednym kubełku) ----> O = n^2

Złożoność pamięciowa:
O = n ---> pamięć potrzebna na tablicę
'''


# funkcja maksi wyciaga element maksymalny z P
def maksi(tab):
    n = len(tab)
    maks = tab[0][1]
    for i in range(n):
        if maks < tab[i][1]:
            maks = tab[i][1]
    return maks


# insertion sortuje buckety
def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key


# algorytm dzieli n elementów na n//10 kubełków, bo jest to bliskie optymalnej dlugosci dla wielu pustych bucketow
def bucket_sort(A, maks):
    n = len(A)
    buckets = [[] for _ in range(n // 10)]

    for j in range(n):
        bucket = int(n*A[j]//maks) // 10
        buckets[bucket].append(A[j])

    for k in range(n // 10):
        insert_sort(buckets[k])

    # wypisanie wyniku do wynikowej tablicy l
    a = 0
    l = [0] * n
    for bucket in buckets:
        for item in bucket:
            l[a] = item
            a += 1
    return l


def SortTab(T, P):
    return bucket_sort(T, maksi(P))

runtests(SortTab)


#Iwo Szczepaniak
from kol1btesty import runtests

'''
Pomysl na algorytm:

sortuje tablice T wzgledem dlugosci elementow, nastepnie dopoki dlugosc jest ta sama, szukam anagramu, jesli prawda
zwiekszam cnt o 1. Nastepnie sprawdzam czy najwiekszy. Dodatkowo tablica podanagram sprawdza czy dany anagram nie był
już raz liczony, dzieki czemu skracam czas trwania algorytmu.

Orientacyjny czas dzialania w pesymistycznym przypadku to n^2.
Złożoność pamięciowa to około n. 

'''


def anagram(a, b):
    n = len(a)
    anag_b = True

    i = 0
    while anag_b and i < n:
        anag_b = False
        for j in range(n):
            if a[i] == b[j]:
                anag_b = True
        i += 1
    return anag_b


def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and len(A[l]) > len(A[max_ind]): max_ind = l
    if r < n and len(A[r]) > len(A[max_ind]): max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)


def len_heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def f(T):
    n = len(T)
    len_heap_sort(T)
    maks = 1
    pod_anagram = [True] * n

    i = 0
    while i < n and pod_anagram:
        j = i + 1
        cnt = 1
        len_i = len(T[i])

        while j < n and len_i == len(T[j]):
            if anagram(T[i], T[j]):
                cnt += 1
                pod_anagram[j] = False
            if maks < cnt:
                maks = cnt
            j += 1
        i += 1

    return maks

runtests( f, all_tests= True )

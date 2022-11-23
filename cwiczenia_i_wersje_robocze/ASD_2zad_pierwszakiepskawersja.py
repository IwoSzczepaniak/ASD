from zad2testy import runtests
from random import randint
# Iwo Szczepaniak


def partion(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def rand_partion(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partion(A, p, r)


def rand_quicksort(A, p, r):
    if len(A) == 1: return A
    if p < r:
        q = rand_partion(A, p, r)
        rand_quicksort(A, p,  q-1)
        rand_quicksort(A, q+1, r)


def depth(L):
    n = len(L) - 1
    rand_quicksort(L, 0, n)

    i = 0
    j = 1
    max_podprzedzialy = 0
    while j <= n:

        # curr = L[i] # domniemany nadzbior
        # nex = L[j] # domniemany podzbior

        # war. po to zeby zbiory które nastepują na pewno nie zawieraly L[i]
        old_j = j
        while L[i][0] == L[j][0] and L[i][1] <= L[j][1]:
            L[i], L[j] = L[j], L[i]
            j += 1
        j = old_j

        curr_podprzedzialy = 0
        while j <= n and L[i][1] >= L[j][0]:  # porównujemy prawy element curr z lewym nexta
            if L[i][1] >= L[j][1]:  # porównujemy prawy element curr z prawym nexta
                curr_podprzedzialy += 1
            j += 1
        if curr_podprzedzialy > max_podprzedzialy:
            max_podprzedzialy = curr_podprzedzialy
        i += 1
        j = i + 1
    return max_podprzedzialy


runtests( depth )

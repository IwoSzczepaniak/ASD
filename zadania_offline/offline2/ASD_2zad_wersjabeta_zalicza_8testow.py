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


def quicksort(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p,  q-1)
        p = q+1


def depth(L):
    n = len(L)
    quicksort(L, 0, n - 1)

    max_val = 0
    i = 0
    uber = [True] * n

    while i + 1 < n:
        j = i + 1
        val_i = 0

        if L[i][0] == L[i + 1][0]:
            uber[i] = False

        while uber[i] and j < n and L[i][1] >= L[j][0]:
            if L[i][1] >= L[j][1]:
                val_i += 1
                uber[j] = False
            j += 1

        if val_i > max_val:
            while L[i - 1][0] == L[i][0]:
                val_i += 1
                i -= 1
            max_val = val_i
        i += 1

    return max_val

runtests( depth )
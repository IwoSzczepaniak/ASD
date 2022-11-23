from zad2testy import runtests
from random import randint
# Iwo Szczepaniak


def partion(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        b = A[j][0]
        if b < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif b == x and A[j][1] > A[r][1]:
            A[r], A[j] = A[j], A[r]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p,  q-1)
        p = q + 1


def depth(L):
    n = len(L)
    quicksort(L, 0, n - 1)

    max_val = 0
    i = 0
    uber = [True] * n

    while i < n:
        if uber[i]:
            j = i + 1
            val_i = 0
            L_1_val = L[i][1]

            while j < n and L_1_val >= L[j][0]:
                if L_1_val >= L[j][1]:
                    val_i += 1
                    uber[j] = False
                j += 1
            if val_i > max_val:
                max_val = val_i
        i += 1

    return max_val

runtests( depth )
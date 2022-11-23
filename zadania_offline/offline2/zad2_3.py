from zad2testy import runtests
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



    return max_val

runtests( depth )
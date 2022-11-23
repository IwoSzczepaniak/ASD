from zad1testy import runtests
# Iwo Szczepaniak


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i-1) // 2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    min = i
    if l < n and A[l] <= A[min]:
        min = l
    if r < n and A[r] <= A[min]:
        min = r
    if min is not i:
        A[i], A[min] = A[min], A[i]
        heapify(A, n, min)


def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)


def heap_extract_min(A):
    n = len(A)
    min = A[0]
    A[0] = A[n-1]
    A[n - 1] = 100000000000000000000000000000
    n = n - 1
    heapify(A, n, 0)
    return min


def min_heap_insert(A, key):
    n = len(A) - 1
    A[n] = 10000000000000000000000000000000
    heap_key(A, n, key)


def heap_key(A, i, key):
    A[i] = key
    while i > 1 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def SortH(p, k):
    warunek = False
    if k == 0:
        return p
    else:
        tab = [0] * k
        first = p
        result = p
        for i in range(k):
            tab[i] = p.val
            p = p.next
        if p is not None: #warunek specjalnie zrobiony dla przypadku k == n, z zasady tablica rozmiaru k+1 ( promień k + dany el.)
            tab.append(p.val)
            p = p.next
            warunek = True

        while p is not None:
            build_heap(tab)
            first.val = heap_extract_min(tab)
            min_heap_insert(tab, p.val)
            p = p.next
            first = first.next

        for _ in range(k):
            build_heap(tab)
            first.val = heap_extract_min(tab)
            first = first.next
        if warunek:#warunek specjalnie zrobiony dla przypadku k == n
            build_heap(tab)
            first.val = heap_extract_min(tab)

        return result


runtests( SortH ) 

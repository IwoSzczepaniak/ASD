# Iwo Szczepaniak
'''class Node:
    def __init__(self, val):
        self.val = val
        self.next = None'''
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
    if l < n and A[l] < A[min]:
        min = l
    if r < n and A[r] < A[min]:
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


def heap_extract_and_insert(A,key):
    n = len(A)
    min = A[0]
    A[0] = A[n-1]
    A[n - 1] = 100000000000000000000000000000
    n = n - 1
    heapify(A, n, 0)
    heap_key(A, n, key)
    return min


def min_heap_insert(A, key):
    n = len(A)
    A[n-1] = 10000000000000000000000000000000
    heap_key(A, (n-1) , key)


def heap_key(A, i, key):
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def SortH(p, k):
    tab = [0] * k
    first = p
    r = p

    for i in range(k):
        tab[i] = r.val
        r = r.next
    if r is not None:  # warunek specjalnie zrobiony dla przypadku k == n, z zasady tablica wrozmiaru k+1 ( promień k + dany el.)
        tab.append(r.val)
        r = r.next
        k = k + 1

    build_heap(tab)

    while r is not None:
        first.val = heap_extract_and_insert(tab, r.val)
        r = r.next
        first = first.next

    for _ in range(k):
        first.val = heap_extract_min(tab)
        first = first.next

    return p


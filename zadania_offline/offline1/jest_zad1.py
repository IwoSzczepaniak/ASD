from zad1testy import runtests
# Iwo Szczepaniak


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        temp = Node(tab[i])
        temp.next = first
        first = temp
    return first


def print_node(first):
    while first is not None:
        print(first.val,"-> ", end="")
        first = first.next
    print("")
    return 0


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


def merge(p1, p2):
    new = Node(None)
    res = new
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            new.next = p1
            p1 = p1.next
        else:
            new.next = p2
            p2 = p2.next
        new = new.next
    if p1 is None:
        new.next = p2
    else:
        new.next = p1
    return res.next


def mid(p): # p idzie dwa razy wolniej niz r, wiec trafi na srodkowy wskaznik
    s, r = p, p.next

    while r is not None and r.next is not None:
        s = s.next
        r = r.next.next
    return s


def merge_sort(p):
    if p is None or p.next is None:
        return p

    left = p

    right = mid(p)
    tmp = right.next
    right.next = None
    right = tmp

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def SortH(p, k):

    r = p
    n = 0
    while r is not None:
        n += 1
        r = r.next

    if k == 0:
        return p
    elif k >= n:
        return merge_sort(p)

    else: #heap warunek konieczny kopca 0 < k+1 < n
        tab = [0] * (k+1)
        first = p
        result = p
        for i in range(k+1):
            tab[i] = p.val
            p = p.next


        for i in range(k+1, n):
            build_heap(tab)
            first.val = heap_extract_min(tab)
            min_heap_insert(tab, p.val)
            p = p.next
            first = first.next

        for _ in range(k+1):
            build_heap(tab)
            first.val = heap_extract_min(tab)
            first = first.next

        return result


runtests( SortH ) 

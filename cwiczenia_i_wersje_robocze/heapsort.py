# Iwo Szczepaniak

class Node:
    def __init__(self):
        self.val = None
        self.next = None


def build_tab(p):
    n = 0
    r = p
    while r.next is not None:
        n += 1
        r = r.next
    tab = n * [0]
    for i in range(n):
        tab[i] = [p.val]
        p = p.next
    return tab

def left(i):
    return 2*i + 1
def right(i):
    return 2*i
def parent(i):
    return (i-1) // 2

def heapify(A, n, i):
    l =left(i)
    r = right(i)
    max = i
    if l < n and A[l] > A[max]:
        max = l
    if r < n and A[r] > A[max]:
        max = r
    if max is not i:
        A[i],A[max] = A[max], A[i]
        heapify(A, n, max)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A,n,i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A [0]
        heapify(A,i,0)

def SortH(p,k): #p wskaźnik na pierwszy element, k mówi o ile miejsc może zostać przesunięty każdy z elementów
    pass


if __name__ == '__main__':
    print(':)')

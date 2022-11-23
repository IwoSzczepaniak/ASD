# Iwo Szczepaniak
'''LEGENDA
n - długosc listy/tablicy
p - wskaznik na pierwszy element
k - najdalsze przestawienie w liscie
j,i - pomocnicze indeksowanie
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_tab(p):
    n = 0
    r = p
    while r is not None:
        n += 1
        r = r.next
    tab = n * [0]
    for i in range(n):
        tab[i] = p.val
        p = p.next
    return tab, n

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


def build_heap(A, n):
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)


def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        temp = Node(tab[i])
        temp.next = first
        first = temp
    return first


def heap_sort(A, n):
    build_heap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def SortH(p,k): #p wskaźnik na pierwszy element, k mówi o ile miejsc może zostać przesunięty każdy z elementów
    if k == 0:
        return p
    else:
        tab, n = build_tab(p)
        heap_sort(tab, n)
        return make_linked_list(tab)





def print_node(first):
    while first is not None:
        print(first.val,"-> ", end="")
        first = first.next
    print("")
    return 0



if __name__ == '__main__':
    #l = [67, 54, 99]
    l = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
    print(l)
    head = make_linked_list(l)
    print_node(head)
    print_node(SortH(head, 8))

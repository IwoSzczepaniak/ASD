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

def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        temp = Node(tab[i])
        temp.next = first
        first = temp
    return first


def left(i):
    return 2*i + 1
def right(i):
    return 2*i
def parent(i):
    return (i-1) // 2

def build_heap(A):
    n = len(A) - 1
    for i in range(parent(n), -1, -1):
        heapify(A, i)


def heapify(A, i):
    n = len(A)
    l =left(i)
    r = right(i)
    min = i
    if l < n and A[l] < A[min]:
        min = l
    if r < n and A[r] < A[min]:
        min = r
    if min is not i:
        A[i], A[min] = A[min], A[i]
        heapify(A, min)


def heap_extract_min(A):
    n = len(A) - 1
    min = A[0]
    A[0] = A[n]
    n = n - 1
    heapify(A, 0)
    return min


def heap_key(A, i, key):
    A[i] = key
    while i > 1 and A[parent(i)] > A[i]:
        A[i], A[parent] = A[parent], A[i]
        i = parent(i)


def min_heap_insert(A, key):
    n = len(A) - 1
    A[n] = 1000
    heap_key(A, n, key)


#p wskaźnik na pierwszy element, k mówi o ile miejsc może zostać przesunięty każdy z elementów
def SortH(p, k):
    if k == 0:
        return p
    else:
        # tab to tablica k+1 elementów Dla danego elementu zasieg jedego z kierunkow, drugi kier. petle innych elementow
        tab = [0] * (k+1)
        r = p
        for i in range(k+1):
            tab[i] = r.val
            r = r.next
        build_heap(tab)
        n = k+1
        while r is not None:
            n += 1
            r = r.next
        # n po przejściu petli ma wartosc dlugosci linked listy, a p dalej jest na elemencie k+2

        ##ans = [] # ans to tablica przechowująca wynik, nizej Node
        answear = Node(None)
        result = answear
        for i in range(k+1, n):
            ##ans.append( heap_extract_min(tab) )
            answear.next = Node(heap_extract_min(tab))
            answear = answear.next
            min_heap_insert(tab, p.val)
            p = p.next
        while p is not None:
            ##ans.append(p.val)
            answear.next = p
            answear = answear.next
            p = p.next

        print("Powinno byc sortowane:")
        ##print(ans)
        return result.next




def print_node(first):
    while first is not None:
        print(first.val,"-> ", end="")
        first = first.next
    print("")
    return 0


if __name__ == '__main__':
    l = [1, 0, 3, 2, 4, 6, 5]
    #l = [67, 54, 99]
    #l = [85, 58, 31, 67, 54, 99, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
    print(l)
    head = make_linked_list(l)
    print_node(head)
    print_node(SortH(head, 1))

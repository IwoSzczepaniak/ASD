# Iwo Szczepaniak
'''LEGENDA
n - długosc listy
p - wskaznik na pierwszy element
k - najdalsze przestawienie w liscie
j,i - pomocnicze indeksowanie
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def SortH(p, k):
    n = leng_list(p)
    if k != 0:
        first = heap_sort(n, k, p)
    else:  # dla k = 0 już posortowane
        return p
    return first


# heap sort

# indeksowanie na zasadach kopca
def left(i):
    return 2*i + 1
def right(i):
    return 2*i
def parent(i):
    return (i-1) // 2


# zwraca wartosc n ostatniego elementu linked listy // dlugosc jest o jeden wieksza DZIALA
def leng_list(p):
    if p is None: return 0
    n = 0
    while p.next is not None:
        n = n + 1
        p = p.next
    return n


# zwraca wskaźnik na i-ty element linked listy
def jump_to(i, p):
    r = p
    for j in range(i):
        r = r.next
    return r


# DZIALA przepina i-ty element z j-tym linked listy| prev_i, i oraz next_i to wskaźniki
def swap(num_j, num_i, p):
    if num_i < num_j:  # num_j < num_j
        num_i, num_j = num_j, num_i

    prev_i = jump_to(num_i - 1, p) # num_i nigdy 0, więc można tak przypisać prev_i, i oraz next_i
    i = prev_i.next
    next_i = i.next

    if num_j == 0:
        j = jump_to(0, p)
        next_j = j.next

        prev_i.next = j
        j.next = next_i  # przepinamy następnik j do nastepnika i, oraz na odwrót

        p = i
        i.next = next_j



    else:
        prev_j = jump_to(num_j - 1, p) # num_j nigdy 0, więc można tak przypisać prev_j, j oraz next_j
        j = prev_j.next
        next_j = j.next

        prev_j.next = i  # przepinamy poprzednik j do i, oraz na odwrót
        prev_i.next = j
        j.next = next_i  # przepinamy następnik j do nastepnika i, oraz na odwrót
        i.next = next_j


# naprawia kopiec
def heapify(n, i, k, p):
    q = p
    le = jump_to(left(i), q)
    r = jump_to(right(i), q)
    maks_el = jump_to(i, q)
    if i-left(i) <= k:  # musi być spełnione zgodnie z warunkiem zadania
        if le.val < n and le.val > maks_el.val:
            maks_el = le
    if i-right(i) <= k:  # musi być spełnione zgodnie z warunkiem zadania
        if r.val < n and r.val > maks_el.val:
            maks_el = r
    if maks_el is not i:
        swap(i, maks_el, q)
        heapify(n, maks_el, k, q)


# tworzy kopiec
def build_heap(n, k, p):
    for i in range(parent(n-1), -1, -1):
        heapify(n, i, k, p)


# sortuje kopcowo
def heap_sort(n, k, p):
    r = p
    build_heap(n, k, r)
    for i in range(n-1, 0, -1):
        swap(0, i, r)
        heapify(i, 0, k, r)
    return p









def print_node(first):
    while first is not None:
        print(first.val,"-> ", end="")
        first = first.next
    print("")
    return 0
def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        temp = Node(tab[i])
        temp.next = first
        first = temp
    return first


if __name__ == '__main__':
    print(':)')
    l = [4,1,3,2,16,9,10,14,8,7]
    head = make_linked_list(l)
    print_node(head)


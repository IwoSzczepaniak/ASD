from zad1testy import Node, runtests
# Iwo Szczepaniak
'''
Pomysł na algorytm:
Tworzę tablicę k+1 (promień zamiany k + dany el.) elementów, z których robię kopiec,
następnie wyciągam najmniejszy element z kopca, w jego miejsce wrzucając kolejny element z listy, aż do końca listy.
Najmniejszy element za każdym razem wpisuje do listy wynikowej (którą jest de facto przekształcona pierwotna lista)

Próbując określić złożoność czasową:
O(k+1) - budowanie tablicy
O(N-(k+1)) log k - działanie właściwego algorytmu

Sumaryczna złożoność czasowa to około O(n + (n-k)logk), czyli około 2nlogk
Dla k = 1, złożoność czasowa tego algorytmu wypada gorzej niż jedno przejście bubble sort'a,
stąd jego zastosowanie w tym wyjątkowym wypadku

Dla k = 1 złożoność buble On*k = n
Dla k = log n i k = n złożonośc O(n + (n-k)logk)
'''

# trzy poniższe funkcje zostały zastąpione w kodzie konkretnymi wartościami w celu optymalizacji,
# pozostawione dla czytelności
def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i-1) // 2


# kolejnych 6 funkcji służy do obsługi kopca, pierwsza naprawia kopiec
def heapify(A, n, i):
    l = 2*i + 1
    r = 2*i + 2
    min = i
    if l < n and A[l] < A[min]:
        min = l
    if r < n and A[r] < A[min]:
        min = r
    if min is not i:
        A[i], A[min] = A[min], A[i]
        heapify(A, n, min)


# tworzy kopiec
def build_heap(A):
    n = len(A)
    for i in range((n-1-1) // 2, -1, -1): # (n-1-1) // 2 to parent(n-1)
        heapify(A, n, i)


#wyciąga najmniejszy element z kopca
def heap_extract_min(A):
    n = len(A)
    min = A[0]
    A[0] = A[n-1]
    A[n - 1] = 100000000000000000000000000000
    n = n - 1
    heapify(A, n, 0)
    return min


#wyciąga najmniejszy element z kopca i dodaje nowy element(key)
def heap_extract_and_insert(A,key):
    n = len(A)
    min = A[0]
    A[0] = A[n-1]
    A[n - 1] = 10000000000000000000000000000000
    n = n - 1
    heapify(A, n, 0)
    heap_key(A, n, key)
    return min


# "wpycha" key jak najwyżej można w kopcu, pomocnicza do insert
def heap_key(A, i, key):
    A[i] = key
    while i > 0 and A[(i-1) // 2] > A[i]: # (i-1) // 2 to parent
        A[i], A[(i-1) // 2] = A[(i-1) // 2], A[i]
        i = (i-1) // 2


# funkcja jest podfunkcją heap_extract_and_insert, zostawiona dla czytelności, dodaje nowy element(key)
def min_heap_insert(A, key):
    n = len(A)
    A[n-1] = 10000000000000000000000000000000
    heap_key(A, (n-1) , key)


# jedno przejście bubble sort'a po liście
# wykorzystany tylko do przypadku k = 1 jako znacznie efektywniejszy algorytm dla tak małego k
def bubble_for_k1(p):
    first = p
    if p.next.val < p.val: # jako wyjątkowe przepięcie sprawdzamy pierwsze dwa elementy osobno
        nextify = p.next
        tmp = nextify.next
        nextify.next = p
        first = nextify
        nextify = nextify.next
        nextify.next = tmp
        p = first.next

    prev = first
    while p.next is not None: # zamiana pozostałych elementów listy
        nextify = p.next
        if nextify.val < p.val:
            tmp = nextify.next
            prev.next = nextify
            nextify.next = p
            p.next = tmp
            prev = prev.next
        else:
            prev = p
            p = p.next
    return first


def SortH(p, k):
    if k == 0: #kopiec jest już posortowany
        return p
    if k == 1: # w tym wypadku bubble sort jest efektywniejszym algorytmem (złożoność n)
        return bubble_for_k1(p)

    # w pozostałych przypadkach tworzę tablicę k+1 (promień zamiany k + dany el.) elementów, z których robię kopiec
    # następnie wyciągam najmniejszy element z kopca, w jego miejsce wrzucając kolejny element z listy, aż do końca listy
    # najmniejszy element za każdym razem wpisuje do listy wynikowej (którą jest de facto przekształcona pierwotna lista)

    tab = []
    first = p
    r = p

    for i in range(k): # dodaje k lub k+1 elementów do tablicy, z której robimy kopiec
        tab.append(r.val)
        r = r.next
    if r is not None:  # warunek specjalnie zrobiony dla przypadku k == n, z zasady tablica wrozmiaru k+1 ( promień k + dany el.)
        tab.append(r.val)
        r = r.next
        k = k + 1

    build_heap(tab) # tworzy kopiec

    while r is not None: # pętla dodaje i wyciąga //(n - k+1)// elementów, // poza przypadkiem n = k //
        first.val = heap_extract_and_insert(tab, r.val)
        r = r.next
        first = first.next

    for _ in range(k): # pętla dodaje do listy wynikowej //k+1// elementów z ostatniej tablicy // poza przypadkiem n = k //
        first.val = heap_extract_min(tab)
        first = first.next

    return p

runtests( SortH ) 

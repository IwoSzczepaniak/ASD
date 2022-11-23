from zad1testy import runtests


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


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


def SortH(p, k): #p wskaźnik na pierwszy element, k mówi o ile miejsc może zostać przesunięty każdy z elementów
    if k == 0:
        return p
    else:
        return merge_sort(p)


runtests( SortH ) 

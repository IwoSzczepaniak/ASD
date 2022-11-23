# Iwo Szczepaniak
'''LEGENDA

'''


'''
def merge(n1, n2):
    if n1 is None:
        return n2
    if n2 is None:
        return n1
    if n1.val > n2.val:
        n2.next = merge(n1, n2.next)
        return n2
    else:
        n1.next = merge(n1.next, n2)
        return n1
'''


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


if __name__ == '__main__':
    l = [67, 54, 99]
    #l = [7, 8, 32, 5, 2, 1, 7, 3, 16]
    #l = [85, 58, 31, 67, 54, 99, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
    head = make_linked_list(l)
    print_node(head)
    '''
    w = [5, 6, 8]
    headw = make_linked_list(w)
    print_node(headw)
    print_node(merge(head, headw))'''
    print_node(merge_sort(head))

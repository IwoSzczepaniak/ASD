class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None


def insert(root, x):
    curr = root
    while True:
        if curr.key == x:
            return
        elif curr.key > x:
            if curr.left:
                curr = curr.left
            else:
                curr.left = Node(x)
                curr.left.parent = curr
                return
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = Node(x)
                curr.right.parent = curr
                return


####################################
def min_BST(root):
    res = - 10**10
    while root:
        res = root
        root = root.left
    return res
####################################


def right_child(node):
    if node.parent is None:
        return False
    return node.parent.right is node


def successor(root):
    if root.right is not None:
        return min_BST(root.right)
    while right_child(root): # cofamy się do góry aż jesteśmy lewym synem
        root = root.parent
    return root.parent
###################################
# wypisanie indeksu na którym by był i-ty element po posortowaniu elementów np. w tablicy

def left_size(node):
    if node.left:
        return node.left.size
    else:
        return 0

def index(node):
    i = left_size(node) # bezpośrednio mniejsze
    while node.parent:
        if node.parent.right == node:
            i += left.size(node.parent) + 1
        node = node.parent
    return i

#################################
####### spadające klocki w podanej kolejności - jaka wysokość
##  bierzemy wszystkie końce i początki i badamy ich maxa
### Tworzymy listę o długości n i dodajemy kolejno klocki na najniższe możliwe miejce idąc od góry,
### return to indeks najwyższej niepustej listy



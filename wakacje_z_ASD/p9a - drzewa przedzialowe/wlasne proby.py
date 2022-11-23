from egzP9atesty import runtests


def smaller(x):
    if x.left is not None:
        x = x.left
        while x.right is not None:
            x = x.right
        return x.key
    else:
        par = x.parent
        while par.right != x:
            x = par
            par = par.parent
        return par.key


def larger(x):
    if x.right is not None:
        x = x.right
        while x.left is not None:
            x = x.left
        return x.key
    else:
        par = x.parent
        while par.left != x:
            x = par
            par = par.parent
        return par.key


class Node:
  def __init__(self, val, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.val = val


def querry():
    pass


def depth(p):
    tmp = p
    i = 0
    while tmp <= 0:
        tmp -= 2*i
        i += 1
    return i + 1


def create_l(x, dep, i):
    if i <= dep:
        x.left(0, x)


def create_r(x, dep, i):
    if i <= dep:
        x.right(0, x)


def ASD(T, p, Q, n):
    dep = depth(p)
    root = Node(0, None)
    x = root
    create_r(x.left, dep, 1)
    create_l(x.right, dep, 1)
    for i in range(2, dep):
        x.left


runtests(ASD, all_tests = True)


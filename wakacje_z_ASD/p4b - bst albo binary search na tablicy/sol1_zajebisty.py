from egzP4btesty import runtests 


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


def if_beauty(x):
    if x.key * 2 == larger(x)+smaller(x):
        return x.key
    else:
        return 0


class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None


def sol(root, T):
    summ = 0
    for x in T:
        summ += if_beauty(x)
    return summ


runtests(sol, all_tests = True)
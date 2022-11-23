from egzP4btesty import runtests 
from bisect import bisect


class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None


# O(n)
def walk(root, tab):
    if root.left:
        walk(root.left, tab)
    tab.append(root.key)
    if root.right:
        walk(root.right, tab)


def bisect_r(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

# O(n + q logn)
def sol(root, T):
    val = []
    walk(root, val)
    output = 0
    for el in T:
        x = bisect_r(val, el.key - 1)
        if val[x-1] + val[x+1] == 2* val[x]:
            output += val[x]
    return output




runtests(sol, all_tests = True)
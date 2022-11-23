from egzP2btesty import runtests
from math import log10



def bisect_right(a, x, lo = 0, hi = None):
    if lo < 0:
        return None
    if hi is None: hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bisect_left(a, x, lo = 0, hi = None):
    if lo < 0:
        return None
    if hi is None: hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def kryptograf( D, Q ):
    n = len(D)
    q = len(Q)
    # O(nm)
    for i in range(n):
        D[i] = D[i][::-1]
    # O(qm)
    for i in range(q):
        Q[i] = Q[i][::-1]
    # O(nm lognm) < n^2 logn
    D = sorted(D)

    final_res = 1
    # O(qmlogn)
    for i in Q:
        lo = bisect_left(D, i)
        hi = bisect_right(D, i + "2")
        final_res *= hi-lo

    return log10(final_res)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 2)
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


def radix_sort(tab, x):
    if x == -1:
        return tab

    it = x
    output_0 = []
    output_1 = []

    for i in tab:
        if len(i) <= it:
            output_0 = [i] + output_0
        elif i[it] == "0":
            output_0.append(i)
        else:
            output_1.append(i)
    return radix_sort(output_0 + output_1, x - 1)


def kryptograf( D, Q ):
    n = len(D)
    q = len(Q)
    x = 0
    # O(nm)
    for i in range(n):
        D[i] = D[i][::-1]
        x = max(x, len(D[i]))
    # O(qm)
    for i in range(q):
        Q[i] = Q[i][::-1]

    # O(nm)
    D = radix_sort(D, x)

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
runtests(kryptograf, all_tests = 3)
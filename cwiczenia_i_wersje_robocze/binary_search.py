def bisect_r(a, key, lo):
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if key >= a[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_l(a, key, lo):
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if key > a[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo



# ___________________________________________________

# z zadania 4aa z wakacji, element na prawo od środka
def ceil_index(A, l, r, key):
    while r - l > 1: # interesuje nas pozycja dopóki są dwa miejsca
        m = (r+l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r # i wybieramy prawe

# ------------------------------------------------


def binary_s(A, l, r, key):
    while r >= l:
        m = (r+l) // 2
        if A[m] > key:
            r = m + 1
        elif A[m] < key:
            l = m - 1
        else:
            return m
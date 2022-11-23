def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1



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
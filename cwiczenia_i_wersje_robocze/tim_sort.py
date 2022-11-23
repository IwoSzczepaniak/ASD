# Iwo Szczepaniak

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


def merge(arr, l, m, r): #l indeks lewy, p indeks prawy, m środek
    len1 = m-l+1
    len2 = r-m
    left, right = [], [] # tablice do złączenia
    for i in range(0, len1):
        left.append(arr[l+i])
    for i in range(0, len2):
        right.append(arr[m+i+1])

    i,j,k = 0, 0, 0
    while i < len1 and j< len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while i < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def insert_sort(arr, l, r):
    for i in range(l+1, r+1):
        j = i
        while j>l and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


def tim_sort(arr):
    n = len(arr)
    minRun = 32

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insert_sort(arr, start, end)
    size = minRun
    while size < n:

        for left in range(0, n, 2*size):
            mid = min((left + size - 1), (n-1))
            right = min((left+2*size-1), (n-1))

            if mid < right:
                merge(arr, left, mid, right)
        size *= 2


if __name__ == '__main__':
    print("wohoa")
    #l = [7, 8, 32, 5, 2, 1, 7, 3, 16]
    l = [85, 58, 31, 67, 54, 99, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
    print(l)
    tim_sort(l)
    print(l)

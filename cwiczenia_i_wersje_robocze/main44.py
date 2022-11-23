def partion1(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j][0] == x and A[r][1] > A[j][1]:
            A[j], A[r] = A[j], A[r]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort1(A, p, r):
    while p < r:
        q = partion1(A, p, r)
        quicksort1(A, p,  q-1)
        p = q+1


#######################################################################################################################

def partion(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        b = A[j][0]
        if b < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif b == x and A[j][1] > A[r][1]:
            A[r], A[j] = A[j], A[r]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p,  q-1)
        p = q + 1

if __name__ == '__main__':
    # = [[1, 6], [5, 6], [2, 5], [5, 10], [8, 9], [3,1], [1, 6]]
    #P = [[1,4], [1,6], [99,8], [1,0], [1,10], [1,9], [1,5], [2,5], [99,5], [99,3], [99,99], [1,1]]
    P = [[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64], [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76], [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41], [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74], [24, 51], [17, 90], [28, 71]]
    L = [[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64], [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76], [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41], [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74], [24, 51], [17, 90], [28, 71]]
    n = len(P)
    quicksort1(L, 0, n - 1)
    print(L)
    quicksort(P, 0, n - 1)
    print(P)

    n = len(L)
    quicksort(L, 0, n - 1)

    max_val = 0
    i = 0
    uber = [True] * n

    while i + 1 < n:
        j = i + 1
        val_i = 0
        L_1_val = L[i][1]

        while uber[i] and j < n and L_1_val >= L[j][0]:
            if L_1_val >= L[j][1]:
                val_i += 1
                uber[j] = False
            j += 1
            if val_i > max_val:
                max_val = val_i
        i += 1
    print(max_val)

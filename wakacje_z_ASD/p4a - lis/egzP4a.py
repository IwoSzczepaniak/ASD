from egzP4atesty import runtests


def ceil_index(A, l, r, key):
    while r - l > 1: # interesuje nas pozycja dopóki są dwa miejsca
        m = (r+l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r # i wybieramy prawe


def lis(T):
    n = len(T)
    S = []
    S.append(T[0])

    for i in range(1, n):
        if T[i] >= S[len(S)-1]:
            S.append(T[i])
        else:
            S[ceil_index(S, -1, len(S)-1, T[i])] = T[i]
    return len(S)


def mosty ( T ):
    T.sort(key = lambda x: (x[0], x[1]))
    T2 = [T[i][1] for i in range(len(T))]
    return lis(T2)

runtests ( mosty, all_tests=True )

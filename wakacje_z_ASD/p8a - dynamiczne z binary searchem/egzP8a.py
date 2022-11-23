from egzP8atesty import runtests


def bisect_r(a, key, lo):
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if key >= a[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def reklamy ( T, S, o ):
    n = len(T)
    P = [(T[i][0], T[i][1], S[i]) for i in range(n)]
    P.sort(key = lambda x: x[0])
    result = 0

    M = [0 for _ in range(n)] # dynamik, patrzymy na największy zysk na prawo
    M[n-1] = P[n-1][2]
    for i in range(n-2, -1, -1):
        M[i] = max(M[i+1], P[i][2])

    S = [P[i][0] for i in range(n)] # starty

    for i in range(n):
        end_first = P[i][1]
        second = 0
        idx = bisect_r(S, end_first, i + 1) # znajdujemy pierwszy większy od end_first
        if idx < n and S[idx] != end_first:
            second = M[idx]
        result = max(result, P[i][2] + second)
    return result


runtests ( reklamy, all_tests=True)

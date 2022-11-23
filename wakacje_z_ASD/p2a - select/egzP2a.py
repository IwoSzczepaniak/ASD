from egzP2atesty import runtests 


def select(T, IND, p, k, r):
    if p < r:
        q = partition(T, IND, p, r)
        if q < k:
            select(T, IND, q+1, k, r)
        elif q > k:
            select(T, IND, p, k, q - 1)
        return


def partition(T, IND, p, r):
    pivot = T[IND[r]][1]
    i = p-1
    for j in range(p, r):
        if T[IND[j]][1] >= pivot:
            i += 1
            T[IND[i]], T[IND[j]] = T[IND[j]], T[IND[i]]
    T[IND[i+1]], T[IND[r]] = T[IND[r]], T[IND[i+1]]
    return i+1


def zdjecie(T, m, k):
    n = len(T)
    START = [0 for _ in range(m)]
    END = [0 for _ in range(m)]
    akt_wid = m+k-1
    akt_end = -1

    for i in range(m):
        START[i] = akt_end + 1
        akt_end += akt_wid
        END[i] = akt_end
        akt_wid -= 1

    IND = [0 for _ in range(n)]
    items = 0
    kolumna = 0
    rzad = 0

    while items < n:
        if START[rzad] + kolumna <= END[rzad]:
            IND[START[rzad] + kolumna] = items
            items += 1
        rzad += 1
        if rzad >= m:
            rzad = 0
            kolumna += 1

    last_end = END[m-1]
    for i in range(m-2, -1, -1):
        select(T, IND, 0, END[i], last_end)
        last_end = END[i] - 1

    return None


runtests ( zdjecie, all_tests=False )
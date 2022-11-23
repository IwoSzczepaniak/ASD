from egzP6atesty import runtests


def ile_cyfr(str):
    cnt = 0
    for i in str:
        if i.isdigit():
            cnt += 1
    return cnt


def partition(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def select(A, p, k, r):
    if p < r:
        q = partition(A, p, r)
        if q < k:
            select(A, q+1, k, r)
        elif q > k:
            select(A, p, k, q-1)
        else:
            return


def google ( H, s ):
    max_len = 0
    for x in H: max_len = max(len(x), max_len) # znajdywanie max len
    elements = [[] for _ in range(max_len+1)]
    for x in H: elements[len(x)].append(x) # wpisywanie do tablicy ze względu na długość

    summ = 0
    i = max_len + 1
    while s > summ:
        i -= 1
        summ += len(elements[i]) # skipowanie ostatnich elementów które są lepsze niezależnie od ilości cyfr

    number = s - summ
    if number == 0: # najgorsze haslo z itego koszyka
        max_cyfr = 0
        index_max_cyfr = 0
        for j in range(len(elements[i])):
            cyfry = ile_cyfr(elements[i][j])
            if max_cyfr < cyfry:
                max_cyfr = cyfry
                index_max_cyfr = j
        return elements[i][index_max_cyfr]

    else: # dla itego koszyka number dobrych haseł, wiec biore pierwsze niedobre
        for j in range(len(elements[i])):
            elements[i][j] = (ile_cyfr(elements[i][j]), elements[i][j])

        select(elements[i], 0, number - 1, len(elements[i])-1)
        return elements[i][number-1][1]
        # dla komórki i, number najlepszych haseł

runtests ( google, all_tests=True )
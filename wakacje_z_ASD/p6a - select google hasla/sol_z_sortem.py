from egzP6atesty import runtests


def ile_cyfr(str):
    cnt = 0
    for i in str:
        if i.isdigit():
            cnt += 1
    return cnt


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
        for j in range (len(elements[i])):
            cyfry = ile_cyfr(elements[i][j])
            if max_cyfr < cyfry:
                max_cyfr = cyfry
                index_max_cyfr = j
        return elements[i][index_max_cyfr]

    else: # dla itego koszyka number najlepszych haseł, wiec biore ostatnie dobre
        for j in range(len(elements[i])):
            elements[i][j] = (ile_cyfr(elements[i][j]), elements[i][j])
        elements[i].sort()
        return elements[i][number-1][1]
        # dla komórki i, number najlepszych haseł

runtests ( google, all_tests=True )
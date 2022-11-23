from egzP9atesty import runtests


def UPDATE(T, index, value):
    T.set(index, value + T.get(index))
    while index//2:
        index = index//2
        T.set(index, T.get(2*index + 1) + T.get(2 * index))


def GETSUM(T, a, b):
    output = 0
    while a + 1 < b:
        if a % 2 == 1: # jeśli a prawy syn dodajemy go osobno
            output += T.get(a)
            a += 1
        if b % 2 == 0: # jeśli b lewy syn dodajemy go osobno
            output += T.get(b)
            b -= 1
        a //= 2
        b //= 2
    if a != b:
        output += T.get(a) + T.get(b)
    elif a != 0:
        output += T.get(a)

    return output


def ASD(T, p, Q, n):
    result = 0
    index_set = n//2
    for el in Q:
        if el[0] == 0:
            UPDATE(T, index_set + el[1], el[2])
        else:
            result += GETSUM(T, index_set + el[1], index_set + el[2])
    return result


runtests(ASD, all_tests = True)


from egzP9atesty import runtests


def UPDATE(T, index, value):
    T.set(index, value + T.get(index))


def GETSUM(T, a, b):
    output = 0
    for i in range(a, b+1):
        output += T.get(i)
    return output


def ASD(T, p, Q, n):
    result = 0
    for el in Q:
        if el[0] == 0:
            UPDATE(T, el[1], el[2])
        else:
            result += GETSUM(T, el[1], el[2])
    return result

runtests(ASD, all_tests = True)


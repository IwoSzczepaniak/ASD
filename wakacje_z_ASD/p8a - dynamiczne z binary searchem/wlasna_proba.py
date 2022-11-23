from egzP8atesty import runtests 


def prev(T, i):
    for j in range(i - 1, -1, -1):
        a = T[j][0][1]
        b = T[i][0][0]
        if a < b:
            return j
    return None


def f(T, PREVS):
    F = [[T[x][1], 1] for x in range(len(T))]

    for i in range(1, len(T)):

        if PREVS[i] is not None:
            F[i][0] = T[i][1]+F[PREVS[i]][0]
            F[i][1] += 1

    max_wynik = 0
    for i in range(len(T)):
        if F[i][1] < 3:
            if max_wynik < F[i][0]:
                max_wynik = F[i][0]
    return max_wynik


def reklamy ( T, S, o ):
    for i in range(len(S)):
        T[i] = (T[i], S[i])
    T.sort()

    PREVS = [None for _ in range(len(T))]
    for i in range(len(T) - 1, -1, -1):
        PREVS[i] = prev(T, i)

    return f(T, PREVS)


runtests ( reklamy, all_tests=True)

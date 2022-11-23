from zad4testy import runtests


def profit(T, i):
    return T[i][0] * (T[i][2] - T[i][1])


def Knapsack(F, T, p, i):
    w_i = T[i][3]
    result = -1

    if F[p][i] != -1:
        return F[p][i]
    if i == 0 or p == 0:
        return 0
    if p - w_i >= 0:
        if T[i][1] > T[i-1][2]:
            result = max(Knapsack(F, T, p, i-1), profit(T, i) + Knapsack(F, T, p - w_i, i-1))
    else:
        j = i-1
        while j > 0 and T[i][1] < T[j][2]:
            j -= 1

        if T[i][1] > T[j][2]:
            result = Knapsack(F, T, p, j) + profit(T, j)

    F[p][i] = result
    return result

def select_buildings(T, p):
    n = len(T)
    F = [[-1 for b in range(p + 1)] for i in range(n)]

    return 0

runtests( select_buildings )
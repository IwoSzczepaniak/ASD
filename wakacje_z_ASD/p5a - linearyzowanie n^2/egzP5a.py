from egzP5atesty import runtests 

def max_area(T):
    s = [-1, 0]
    n = len(T)

    LS = [-1 for _ in range(n)]
    RS = [n for _ in range(n)]

    for i in range(-1, n):
        while s[len(s) - 1] != -1 and T[s[len(s) - 1]] > T[i]:
            RS[s[len(s) - 1]] = i
            s.pop()

        if T[i] == T[i-1]:
            LS[i] = LS[i-1]
        else:
            LS[i] = s[len(s) - 1]
        s.append(i)

    area = 0
    for j in range(n):
        area = max(area, T[j]*(RS[j]- LS[j] - 1))
    return area


def inwestor ( T ):
    return max_area(T)


runtests ( inwestor, all_tests=True )
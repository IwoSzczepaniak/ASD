from egzP2btesty import runtests
from math import log10


def kryptograf( D, Q ):
    n = len(D)
    q = len(Q)
    final_res = 1
    for i in range(q):
        Q[i] = [Q[i], 0]
    # O(qnm)
    for i in range(q):
        result = 0
        sufix = Q[i][0]

        if sufix == "":
            result += n
        else:
            m = len(sufix)
            # O(nm)
            for j in range(n):
                # O(m)
                if D[j][-m:] == sufix:
                    result += 1
                    Q[i][1] += 1

        final_res *= result
    return log10(final_res)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 0)
'''
Dana jest tablica n liczb naturalnych a. Czy da się wybrać podciąg sumujący się do wartości T.
f(i,t) - funkcja sprawdzająca czy sumuje się do t       t < T

'''
def subsetsum(A, T):
    n = len(A)
    d = [[False]*(T+1) for _ in range(n)]
    for i in range(1,n):
        d[i][0] = True
    for i in range(1,n):
        for j in range(1,T+1):
            if j >= A[i]:
                d[i][j] = d[i-1][j] or d[i-1][j-A[i]]
            else:
                d[i][j] = d[i-1][j]
    return d[n-1][T]

'''
szukamy najdluzszego podciagu wspolnego dla A i B
'''

def lcs(A,B):
    n = len(A)
    m = len(B)
    t = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, n):
        for j in range(1, m):
            tmp = 0 # maks
            if A[i-1] == B[j-1]:
                tmp = t[i-1][j-1] + 1
            tmp = max(tmp, t[i-1][j], t[i][j-1])
            t[i][j] = tmp
    return t[n][m]


def rising_lcs(A):
    X = sorted(A)
    lcs(A, X)

##


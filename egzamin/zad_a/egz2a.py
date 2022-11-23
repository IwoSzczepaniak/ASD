# Iwo Szczepaniak
from egz2atesty import runtests

# Algorytm polega na najbardziej prostolinijnym podejściu do problemu: Tworzymy tablicę magazynów - M, długości len(A),
# bo tyle może mieć najgorszy przypadek. Następnie iterujemy po transportach przychodzących do elektrowni - tablicy A
# i szukamy  pierwszego wolnego miejsca w tablicy M iterując po j. Proces powtażamy aż do ostatniego elementu w A
# -> do momentu gdy i == len(A)
# Szacowana złożoność: n^2

# Drugi algorytm, wykomentowany - niestety nie działający opierający się na strukturze drzewa przedziałowego na tablicy.
# Dzięki wykorzystaniu struktury drzewa oszczędzamy dużo czasu nie przeszukując każdego magazynu pojedynczo
# Pozwalałoby to bez błędów w implementacji na złożoność wzorcową : nlogn.
'''
def left(i): return 2*i+1
def right(i): return 2*i+2


def coal( A, T ):
    n = len(A)
    M = [T for _ in range(2*n + 2)]
    for i in range(n):
        M[i] = 0
    j = n
    while j > 0:
        j = j//2
        M[j] = M[left(j)] + M[right(j)]

    for i in range(len(A)):
        j = 0
        while n < j < 2*n:
            if M[left(j)] > A[i]:
                j = left(j)
            elif M[right(j)] > A[i]:
                j = right(j)
        if i == n-1:
            return j
        M[j] -= A[i]
        while j > 0:
            j = j // 2
            M[j] -= A[i]
'''


def coal( A, T ):
    M = [T for _ in range(len(A))]

    i = 0
    j = 0
    while i < len(M):
        if A[i] <= M[j]:
            M[j] -= A[i]
            i += 1
            if i == len(A):
                return j
            j = 0
        else:
            j += 1
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )

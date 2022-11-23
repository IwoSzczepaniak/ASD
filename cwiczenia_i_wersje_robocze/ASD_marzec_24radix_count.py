def radix_sort(tab):
    n = len(tab)
    for x in range(n):
        tab[x] = (tab[x] // n, tab[x] % n)
    count_sort(tab, n,  1)
    count_sort(tab, n,  0)
    for x in range(n):
        tab[x] = tab[x][0] * n + tab[x][1]
    return tab


def count_sort(tab, n, index):
    B = [0] * n
    C = [0] * n
    for x in range(n):
        B[tab[x][index]] += 1
    for x in range(1, n):
        B[x] += B[x-1]
    for x in range(n):
        C[B[tab[x][index]] - 1] = tab[x]
        B[tab[x][index]] -= 1
    for x in range(n):
        tab[x] = C[x]
    return tab



if __name__ == '__main__':
    #l = [7, 8, 32, 5, 2, 1, 7, 3, 16]
    l = [85, 58, 31, 67, 54, 99, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]

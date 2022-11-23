def bubble_dso(tab, p, r):
    for i in range(p, r + 1):
        for j in range(0, r - i):
            if tab[p+j][1] < tab[p+j+1][1]:
                tab[p + j][1], tab[p + j + 1][1] = tab[p + j + 1][1], tab[p + j][1]

if __name__ == '__main__':
    l = [6, 93], [6, 72], [6, 38], [6, 55], [6, 77], [6, 64]
    bubble(l, 0, len(l) - 1)
    print(l)

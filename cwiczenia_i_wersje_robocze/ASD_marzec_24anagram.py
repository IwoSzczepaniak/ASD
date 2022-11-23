# ilość wartości w A jest równa B = log n
# tworzymy tablice wielkosci log n i zliczamy czestosc wystepowania elementow, wstawiajac nowy sortujemy binarnie


# dwa slowa a i b o dlugosci n, alfabet dlugosci k, który sprawdza czy sa anagramami(te same litery)

def anagram(a,b,k):
    n = len(a)
    letters = [0] * k
    for i in range(n):
        letters[a[i]] += 1
        letters[b[i]] -= 1
    for j in range(k):
        if letters(j) != 0:
            return False
    return True

# tablica A, n liczb parami różnych. szukamy x i y z A, takie że gdy posortowana x i y są najdalszymi sąsiadami.
# robimy kubełki i sprawdzamy min z poprzednika dziur i maks z nastepnika dziury dla dziur wielkosci p i p-1
# wtedy znajdziemy maks odległość


# otoczka, algorytm do robienia otoczki z losowo rozrzuconych punktów



if __name__ == '__main__':
    # l = [7, 8, 32, 5, 2, 1, 7, 3, 16]
    l = [85, 58, 31, 67, 54, 99, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]

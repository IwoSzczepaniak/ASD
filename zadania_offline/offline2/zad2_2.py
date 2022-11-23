from zad2testy import runtests
# Iwo Szczepaniak
'''
Pomysł na algorytm:
1) Sortowanie
Sortuję tablicę przedziałów rosnąco względem indeksu 0, gdy wartość indeksu 0 równa, sortuję zbiory względem indeksu 1
malejąco. Odwrócona kolejność przyspiesza działanie algorytmu (jeśli mamy podzbiory [a,3], [a,6], [a,8],
to na pewno [a,8] zawiera wszyskie poprzednie zbiory. Stąd sortowanie takiego zbioru [a,8], [a,6], [a,3] jest opłacalne,
a odbywa się bardzo małym kosztem.

2) Początkowe założenie, że wszystkie ziory są nadzbiorami ( nie są podzbiorami pozostałych zbiorów )
Program tworzy tablicę uber, któa początkowo ma wartość True dla wszystkich indeksów

3) Szukanie podzbiorów dla kolejnych nadzbiorów
W momencie, gdy okazuje się, że dany zbiór jest jednak podzbiorem innego zbioru, tablica uber pod danym indeksem zmienia
wartość na False, przez co nie będzie liczona dla niego ilość podzbiorów (skoro istnieje nadzbiór zawierający dany zbiór,
to będzie on również zawierał wszystkie podzbiory danego zbioru). Dla pozostałych zbiorów liczymy ilość podzbiorów 
oznaczone jako val_i. Na koniec sprawdzamy czy val_i większe niż max. Jeśli tak, to val_i jest nową wartością max.

Algorytm "idzie w prawo" po posortowanych zbiorach, zatem nigdy nie przeoczy on zbioru zawierającego się w 
konkretnym zbiorze, gdyż zbiór znajdujący się na lewo ma pierwszą wartość mniejszą niż dany lub jeśli ten element
jest równy, to poprzedni ma większą wartość drugą, więc też nie może się w nim zawierać, zatem algorytm prawidłowo
wylicza ilość podzbiorów, a dzięki zmiennej max, poprawnie zwraca maksymalną ilość podzbiorów.

Złożoność czasowa:
1)Pesymistyczna: O = n^2 + n^2  = 2n^2
Dla pechowych danych wejściowych, dane mogą być posortowane i nie zawierać się w sobie, więc oba algorytmy dają n^2

2)Oczekiwana: nlogn + n*k, gdzie k to liczba nadzbiorów w tablicy L ----> Około O = nlogn + n
W miażdżącej większości przypadków sortowanie quicksortem przebiega w czasie nlogn, a ilość wejść do drugiej pętli for -
- k jest zazwyczaj znacznie mniejsza niż n.

3)Optymistyczna: 0 = nlogn + n


'''

# zmodyfikowana funkcja partition tak, by gdy w sortowaniu rosnącym występują liczby o tej samej liczbie pod indeksem 0,
# indeks 1 był sortowany malejąco [2,5] , [2,7] , [1,2] ---> [1,2],  [2,7] , [2,5]
def partion(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        b = A[j][0]
        if b < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif b == x and A[j][1] >= A[r][1]:
            A[r], A[j] = A[j], A[r]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

#quicksort z wykorzystaniem zmodyfikowanej funkcji partion
def quicksort(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p,  q-1)
        p = q + 1


def depth(L):
    # pierwszy krok to posortowanie indeksów zgodnie z założonym porządkiem i stworzenie tablicy bool'ów
    n = len(L)
    quicksort(L, 0, n - 1)
    max_val = 0
    uber = [True] * n

    for i in range(n):
        # sprawdzenie czy zbiór pod indeksem i jest sklasyfikowany jako nadzbiór
        if uber[i]:
            val_i = 0
            L_1_val = L[i][1]

            # szukanie wszystkich możliwych podzbiorów dla i-tego elementu
            for j in range(i + 1, n):
                if L_1_val >= L[j][0]:
                    if L_1_val >= L[j][1]:
                        val_i += 1
                        uber[j] = False
            # jeśli ilość podzbiorów większa niż max, następuje przypisanie nowej wartosci dla max
            if val_i >= max_val:
                max_val = val_i
    return max_val

runtests( depth )

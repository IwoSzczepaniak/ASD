#Iwo Szczepaniak
from kol2atesty import runtests

# Algorytm zachłanny liczący zadany problem
# Na początek tworzymy tablicę przesiadki, w której umieścimy możliwe miejsca przesiadki, wraz z ilością punktów
# kontrolnych przez które należy przejechać jadąc do tego miejsca, oraz stary index, w oryginalnej tablicy.
# Następnie w funcji driver change szukamy najkorzystniejszego miejsca w zasięgu (trzy następne punkty kontrolne)
# w którym warto, żeby jazdę zakończył Marian(tzn jechał on od i-1 do i). Następnie w pętli while, wykonujemy
# funkcję driver_change dopóki zasięg nie przekroczy B.
# Zakładamy, tak jakby zawsze w zasięgu range_in_original jechał Jacek. Następnie staje on na stacji i patrzy za plecy
# na którym punkcie zamiany należało wpuścić Mariana. Wtedy cofa się maszyną czasu do tego momentu i zamienia się.
# Marian przejeżdża do najbliżeszej stacji i algorytm znowu może wykonać się tak jakby z tego miejsca jechał Jacek
# (co niekoniecznie musi mieć miejsce)
# Złożoność pamięciowa: n
# Złożoność czasowa: n


def driver_change(i, przesiadki):
    change = przesiadki[i+1]
    ret = i+1

    for j in range(i + 1, i+4):
        if przesiadki[j] < change:
            change = przesiadki[j]
            ret = j
    return ret


def drivers( P, B ):
    n = len(P)
    przesiadki = []
    controle_points = 0
    ret_org_index_tab = []

    for i in range(n):
        if P[i][1]:
            przesiadki.append((controle_points, i))
            controle_points = 0
        else:
            controle_points += 1

    range_in_original = przesiadki[3][1]
    index_in_przesiadki = -1 # punkt 0 nie jest punktem przesiadkowym
    last_przesiadki = -5

    while range_in_original <= B:
        i_in_przesiadki = driver_change(index_in_przesiadki, przesiadki)
        if last_przesiadki + 1 != i_in_przesiadki: #żeby uniknąć przesiadki Mariana na Mariana
            ret_org_index_tab.append(przesiadki[i_in_przesiadki][1])
            last_przesiadki = i_in_przesiadki
        index_in_przesiadki = i_in_przesiadki
        if i_in_przesiadki + 3 >= len(przesiadki):
            return ret_org_index_tab
        else:
            range_in_original = przesiadki[i_in_przesiadki + 3][1]

    return ret_org_index_tab

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
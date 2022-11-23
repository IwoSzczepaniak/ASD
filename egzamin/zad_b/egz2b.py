# Iwo Szczepaniak
from egz2btesty import runtests
# Algorytm dynamiczny polegający na wykorzystaniu funkcji F(i) - na i-tym poziomie maksymalna ilość monet
# w sakwie wojownika. Wartością graniczną tej funkcji jest F(0) = 0 (przed wykonaniem 1 kroku pętli),
# rycerz startuje z pustą sakwiewką. Iterując przez wszystkie piętra, oraz iterując po drzwiach
#  dzięki funkcji door obliczamy jakie możliwości dają nam konkretne drzwi i jeśli jest to lepsza oferta
#  niż ta do tej pory na polu przez te drzwi wskazywane, to wpisujemy tę opcję do tablicy F.
#  Na koniec zwracamy ostatni indeks tablicy F

# Prawdopodobny błąd w testach, szczególnie w nr2: wybierając ścieżkę 0->6->7->8->9 wynik powinien byc 14
# Szacowana złożoność: n

def door(C, possesion, lvl, i):
    next_lvl = C[lvl][i][1]
    if next_lvl == -1: return -1, -1
    in_chest = C[lvl][0]
    cost = C[lvl][i][0]
    if cost <= in_chest + possesion:
        if cost + 10 <= in_chest:
            return possesion + 10, next_lvl
        else:
            return possesion + in_chest - cost, next_lvl
    return -1, next_lvl


def magic( C ):
    F = [-1 for _ in range(len(C))]
    F[0] = 0
    # result = 0
    for lvl in range(len(C)):
        possesion_on_lvl = F[lvl]
        if possesion_on_lvl != -1:
            for i in range(1, 4):
                next_lvl_possesion, next_lvl = door(C, possesion_on_lvl, lvl, i)
                if next_lvl != -1 and F[next_lvl] < next_lvl_possesion:
                    F[next_lvl] = next_lvl_possesion
    return F[len(C)-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
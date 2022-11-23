#Iwo Szczepaniak
from zad5testy import runtests
from queue import PriorityQueue

# Algorytm zachłanny liczący zadany problem.
# Pomysł na algorytm: Dojeżdżamy w miejsce w którym braknie nam paliwa i mówimy: ah, powinienem wcześniej zatankować,
# cofamy się w czasie do momentu mijania plamy o najwięszkej pojemności i tankujemy. Schemat powtarzamy aż do
# dojechania do miasta B
# Opis algorytmu:
# Tworzymy tablicę Tank, zwracającą indeksy punktów tankowania. Tworzymy też priority queue station_q, na której będą
# umieszczane plamy na których można było tankować. Chcemy tankować na najbardziej opłacalnej stacji w zasięgu, tak więc
# żeby ściągać z pq plamy w poprawnej kolejności, wpisujemy ich objętość z ujemnymi indeksami. Dzięki temu funkcja get
# wyciąga plamę o największej pojemności w aktualnym range'u(curr_range), a do curr_range jest odejmowana ujemna
# wartość - czyli dodawana odpowiednia.
# Uzasadnienie poprawności: Ponieważ zawsze tankujemy na najbardziej pojemnej stacji, gwarantuje nam to
# zebranie największej możliwej w danym momencie plamy. Dzięki temu nie ma takiego tankowania, które dałoby lepszy
# zasięg. Każda inna stacja da mniejszy zasięg, przez co mniej możliwości na tankowanie, a największy zasięg pokrywa
# wszystkie tankowania możliwe dla mniejszych plam.
# Szacowana złożoność czasowa: n^2
# Złożoność pamięciowa: n


def plan(T):
    n = len(T)
    Tank = [0]
    station_q = PriorityQueue()
    curr_range = T[0]
    i = 1
    while curr_range < n-1:
        while i <= curr_range:
            if T[i] != 0:
                station_q.put(((-1)*T[i], i))
            i += 1
        tmp = station_q.get()
        curr_range -= tmp[0]
        Tank.append(tmp[1])
    Tank.sort()
    return Tank

runtests( plan, all_tests = True )

from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None


def choice(DP, S, P, W, i):
    if S < 0:
        return -inf
    if i >= len(P):
        return 0
    if DP[i][S] is not None:
        return DP[i][S]
    d1 = choice(DP, S-W[i], P, W, i+1) + P[i]
    d2 = choice(DP, S, P, W, i+1)
    DP[i][S] = max(d1, d2)
    return DP[i][S]


def wybory(T):
    summ = 0
    for el in T:
        S = el.fundusze
        P = []
        W = []
        pp = el
        while pp is not None:
            P.append(pp.wyborcy)
            W.append(pp.koszt)
            pp = pp.next
        DP = [[None for _ in range(S+1)] for _ in range(len(P))]
        summ += choice(DP, S, P, W, 0)

    return summ

runtests(wybory, all_tests = True)
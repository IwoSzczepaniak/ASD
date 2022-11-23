from egzP7atesty import runtests 


def akademik( T ):
    n = len(T)
    happy = 0
    for i in T:
        if i == (None, None, None):
            happy += 1

    graph_happy = 0

    return n-happy-graph_happy

    # rooms_nr = 0
    # for i in range(len(T)):
    #     for j in range(3):
    #         if T[i][j] is not None and rooms_nr < T[i][j]:
    #             rooms_nr = T[i][j]
    #
    # R = [[] for _ in range(rooms_nr+1)]
    # for i in range(len(T)):
    #     for j in range(3):
    #         if T[i][j] is not None:
    #             R[T[i][j]].append(i)
    # R.sort(key = lambda x: (len(x)))



runtests ( akademik )

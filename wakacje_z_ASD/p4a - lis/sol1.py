from egzP4atesty import runtests 


def mosty ( T ):
    n = len(T)
    T.sort(key = lambda x: (x[0], x[1]))
    max_i = 0
    sequence_len = [1 for _ in range(n)]
    moment_len = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if T[j][1] < T[i][1] and sequence_len[j]+1 > sequence_len[i]:
                sequence_len[i] = sequence_len[j] + 1
        if sequence_len[i] > sequence_len[max_i]:
            max_i = i
    return sequence_len[max_i]

runtests ( mosty, all_tests=True )
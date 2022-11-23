from egzP9btesty import runtests


def dfs_visit(G, i, path):
    while len(G[i]) != 0:
        w = G[i][0]
        G[i].pop(0)
        dfs_visit(G, w, path)
    path.append(i)


def dfs(G, s):
    path = []
    dfs_visit(G, s, path)
    return path[::-1]


def dyrektor( G, R ):
    for v in range(len(R)):
        for x in R[v]:
            G[v].remove(x)
    return dfs(G, 0)


runtests(dyrektor, all_tests=True)

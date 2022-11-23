############ GRAF PRZECHODNI, SPRAWDZAMY CZY

def dm(M):
    n = len(M)
    DM = [[True if M[i][j] else False for j in range(n)]for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                DM[i][j] = DM[i][j] or (DM[i][k] and DM[j][k])


####################### Krawędzie malejące

# w dfs szukamy tylko malejących ścieżek. Zapisujemy je i wybieramy tę najmniejszą

from egzP1atesty import runtests


def length_of_the_longest_letter(M, D, message):
    if len(message) > 4:
        r = 4
    elif len(message) < 1:
        return -1
    else:
        r = len(message)
    code = message[0]
    if len(message) > 1:
        for i in range(1, r - 1):
            code += message[i]

    j = len(code)
    while j > 0:
        for i in range(len(D)):
            if code == M[D[i]][1]:
                return j # j to długość wyrazu
        code = code[:-1]
        j -= 1


def titanic( W, M, D ):
    letters = {}
    for i in range(len(M)): letters[M[i][0]] = M[i][1]
    # available = {}
    # for i in range(len(D)): available[M[D[i]][0]] = M[i][1]

    message = letters[W[0]]
    for i in range(1, len(W)): message += letters[W[i]]


    leng = 0
    cnt = 0
    while leng < len(message):
        leng = length_of_the_longest_letter(M, D, message)
        message = message[leng:]
        cnt += 1

    return cnt

runtests ( titanic, recursion=False)
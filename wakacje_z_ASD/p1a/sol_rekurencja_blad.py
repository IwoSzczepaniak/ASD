from egzP1atesty import runtests
from math import inf


def exist(M, D, message, leng):
    if len(message) < leng:
        return False
    code = message[0]
    if leng > 1:
        for i in range(1, leng):
            code += message[i]
    for i in range(len(D)):
        if code == M[D[i]][1]:
            return True
    return None


def rec(message, M, D, cnt, answers):
    if len(message) == 0:
        answers.append(cnt)
        return
    elif 0 < len(message):
        possibilities = [1]
        if exist(M, D, message, 4) is not None:
            possibilities.append(4)
        if exist(M, D, message, 3) is not None:
            possibilities.append(3)
        if exist(M, D, message, 2) is not None:
            possibilities.append(2)

        while possibilities:
            x = possibilities.pop()
            cnt += 1
            message = message[x:]
            rec(message, M, D, cnt, answers)

    return cnt


def titanic( W, M, D ):
    letters = {}
    for i in range(len(M)): letters[M[i][0]] = M[i][1]
    message = letters[W[0]]
    for i in range(1, len(W)): message += letters[W[i]]
    cnt = 0
    answers = []
    rec(message, M, D, cnt, answers)

    mini = inf
    for i in range(len(answers)):
        if mini > answers[i]:
            mini = answers[i]
    return mini
runtests ( titanic, recursion=False)
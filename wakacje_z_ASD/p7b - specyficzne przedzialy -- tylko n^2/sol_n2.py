from egzP7btesty import runtests
UNPICKED = 0
PICKED = 1
OVERPICKED = 2


def ogrod( S, V ):
    n = len(S)
    m = len(V)
    output = 0
    for i in range(n):
        S[i] -= 1

    for i in range(n):
        is_taken = [UNPICKED for _ in range(m)]
        tem_output = 0

        for j in range(i, n):
            if is_taken[S[j]] == UNPICKED: #zbieramy niezebrane owoce
                is_taken[S[j]] = PICKED
                tem_output += V[S[j]]

            elif is_taken[S[j]] == PICKED: # potem kasujemy jeśli napotykamy ten owoc znowu
                output = max(output, tem_output)
                tem_output -= V[S[j]]
                is_taken[S[j]] = OVERPICKED

            elif is_taken[S[j]] == OVERPICKED:
                pass

        output = max(output, tem_output) # dla ostatniego elementu
    return output
    
runtests(ogrod, all_tests = True)
from egzP8atesty import runtests


def reklamy ( T, S, o ):
    for i in range(len(S)):
        T[i] = (T[i], S[i])
    T.sort()
    result = 0
    for i in range(len(T)):
        begg = T[i][0][0]
        end = T[i][0][1]
        length = end - begg
        income = T[i][1]
        result = max(result, income)
        for j in range(i+1,len(T)):
            begg2 = T[j][0][0]
            end2 = T[j][0][1]
            length2 = end - begg
            income2 = T[j][1]
            if end < begg2 and o >= length2 + length and income2+income > result:
                result = income2+income

    return result


runtests ( reklamy, all_tests=True)

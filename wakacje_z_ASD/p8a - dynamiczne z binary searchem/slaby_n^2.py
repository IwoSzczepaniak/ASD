from egzP8atesty import runtests 


def reklamy ( T, S, o ):
    result = 0
    for i in range(len(T)):
        begg = T[i][0]
        end = T[i][1]
        length = end - begg
        income = S[i]
        result = max(result, income)
        for j in range(len(T)):
            begg2 = T[j][0]
            end2 = T[j][1]
            length2 = end2 - begg2
            income2 = S[j]
            if end<begg2 or end2<begg:
                if j != i and o >= length2 + length and income2+income > result:
                    result = income2+income
    return result


runtests ( reklamy, all_tests=True)

from egzP5atesty import runtests 


def inwestor ( T ):
    n = len(T)
    maxi = 0
    for i in range(n):
        min = T[i]
        output = min

        j = i - 1
        while j >= 0:
            if T[j] >= min:
                output += min
                j -= 1
            else:
                break

        j = i + 1
        while j < n:
            if T[j] >= min:
                output += min
                j += 1
            else:
                break

        maxi = max(maxi, output)

    return maxi


runtests ( inwestor, all_tests=True )
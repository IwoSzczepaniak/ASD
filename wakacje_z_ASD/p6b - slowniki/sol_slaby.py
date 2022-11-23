from egzP6btesty import runtests 


def jump ( M ):
    ruchy = {"UR":(1,2), "RU":(2,1), "RD":(2,-1), "DR":(1,-2), "DL":(-1,-2), "LD":(-2,-1), "LU":(-2,1), "UL":(-1,2)}
    zapalone = [(0,0)]
    position = [0,0]

    for el in M:
        position[0] += ruchy[el][0]
        position[1] += ruchy[el][1]
        new = (position[0], position[1])
        if new not in zapalone:
            zapalone.append(new)
        else:
            zapalone.remove(new)

    return len(zapalone)
    
runtests(jump, all_tests = True)
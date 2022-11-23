from queue import PriorityQueue


class Vertex:
    def __init__(self, index, cords):
        self.index = index
        self.cords = cords
        self.val = float('inf')
        self.parent = None
        self.visited = False

    def __str__(self):
        return f'Index: {self.index}, len: {self.val}, parent: {self.parent}, visited: {self.visited}'


def find_len(city_a, city_b):
    val = ((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2) ** (0.5)
    if int(val) < val:
        return int(val) + 1
    else:
        return int(val)



def algPrim(ListOfCities, A, GraphList):
    n = len(A)
    LenBetweenCities = [[find_len(A[i], A[j]) for j in range(n)] for i in range(n)]
    Q = PriorityQueue()
    Q.put((0, 0))
    times = []
    for elem in ListOfCities:
        elem.val = float('inf')
        elem.parent = None
        elem.visited = False
    while not Q.empty():
        nic, t = Q.get()
        if not ListOfCities[t].visited:
            for i in GraphList[t]:
                elem = ListOfCities[i]
                if elem.index != t and elem.index != ListOfCities[t].parent:
                    curr_time = LenBetweenCities[t][elem.index]
                    if elem.parent is not None:
                        if curr_time < elem.val:
                            times.remove(elem.val)
                            elem.parent = t
                            elem.val = curr_time
                            if elem.index != ListOfCities[t].parent:
                                times.append(curr_time)
                        if not elem.visited:
                            Q.put((curr_time, elem.index))
                    else:
                        if not elem.visited:
                            elem.parent = t
                            elem.val = curr_time
                            times.append(curr_time)
                            if not elem.visited:
                                Q.put((curr_time, elem.index))
            ListOfCities[t].visited = True
    min_time = min(times)
    max_time = max(times)
    return max_time - min_time
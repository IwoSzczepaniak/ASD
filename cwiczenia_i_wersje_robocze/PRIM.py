from queue import PriorityQueue


class Node:
    def __init__(self, index):
        self.index = index
        self.key = 10**10
        self.parent = None
        self.visited = False

    def __str__(self):
        return f'Index: {self.index}, len: {self.key}, parent: {self.parent}, visited: {self.visited}'


def extract_min(H):
    # tmp = H.get()
    # if not vis[tmp[2]]:
    #     return tmp[2]
    #
    # while vis[tmp[2]]:
    #     tmp = H.get()
    #     if not vis[tmp[2]]:
    #         return tmp[2]

    return None


def prim(G, s):
    H = PriorityQueue()
    for i in range(n):
        if i == s:
            x = Node(s)
            x.key = 0
            x.prev = -1
            x.vis = True
            H.put(x)
        else:
            H.put(Node(i))

    while H:
        v = extract_min(H)
        if v:
            for x in range(n):
                if G[v][x] != 0 and x.cost > G[v][x]:
                    x.cost = G[v][x]
                    x.prev = v

                    for i in range(n):
                        if G[x][i] != 0:
                            H.put((G[x][i], x, i))


if __name__ == '__main__':
    n = 7
    graph = [ [0, 2, 3, 3, 0, 0, 0],
              [2, 0, 4, 0, 3, 0, 0],
              [3, 4, 0, 5, 1, 6, 0],
              [3, 0, 5, 0, 0, 7, 0],
              [0, 3, 1, 0, 0, 8, 0],
              [0, 0, 6, 7, 8, 0, 9],
              [0, 0, 0, 0, 0, 9, 0]]
    s = 0

    prim(graph, s)

    # res = [n]
    # child = n
    # father = prev[n]
    # for i in range(n-1):
    #     res.append(father)
    #     child = prev[child]
    #     father = prev[child]
    # print(res)

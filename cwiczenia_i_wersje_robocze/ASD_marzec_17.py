def foo(heap, element):
    heap[heap[0]+1] = element
    heap[0] += 1
    i = heap[0]
    while i > 0 and heap[i] > heap[i//2]:
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i = i//2

#####################################################################################################################


def partion(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quciksort_heap(t):
    parts = []
    n = len(t)
    parts.append((0, n-1))
    while len(parts) > 0:
        n, k = parts.pop()
        if n<k:
            q = partion(t, n, k)
            parts.append((n, q-1))
            parts.append((q+1, k))

######################################################################################################################


if __name__ == '__main__':
    pass

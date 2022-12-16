import numpy as np

# function bellmanFord
# input: adjacency matrix numpy
# output: matrix numpy with shortest path from all nodes to all other nodes

def Bellman_Ford(C : np.matrix ) -> np.matrix:
    size = C.shape[0]

    D = np.matrix(np.ones(C.shape) * np.inf)

    for src in range(size):
        D[src, src] = 0

        for _ in range((size * size) - 1):
            for row in range(size):
                for col in range(size):
                    if D[src, row] != np.inf and D[src, row] + C[row, col] < D[src, col]:
                        D[src, col] = D[src, row] + C[row, col]

    return D
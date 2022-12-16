import numpy as np

# function bellmanFord
# input: adjacency matrix numpy
# output: matrix numpy with shortest path from all nodes to all other nodes

def bellman_ford(matrix):
    size = matrix.shape[0]

    # initialize distance matrix
    distance = np.matrix(np.ones(matrix.shape) * np.inf)

    for src in range(size):
        distance[src, src] = 0

        for _ in range((size * size) - 1):
            for row in range(size):
                for col in range(size):
                    if distance[src, row] != np.inf and distance[src, row] + matrix[row, col] < distance[src, col]:
                        distance[src, col] = distance[src, row] + matrix[row, col]

    return distance
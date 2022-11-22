import numpy as np


# function bellmanFord
# input: adjacency matrix numpy
# output: matrix numpy with shortest path from all nodes to all other nodes

def bellman_ford(matrix):
    size = matrix.shape[0]

    # initialize distance matrix
    distance = np.zeros((size, size), dtype=int)
    distance.fill(np.inf)

    # set distance from node to itself to 0
    for i in range(size):
        distance[i][i] = 0

    # for each node
    for i in range(size):
        # for each edge
        for j in range(size):
            for k in range(size):
                # if there is an edge

                matrixJK = matrix[j][k]
                distanceIK = distance[i][k]
                distanceIJ = distance[i][j]


                if matrix[j][k] != 0:
                    # if the distance from node i to node k is greater than the distance from node i to node j + the distance from node j to node k
                    if distance[i][k] > distance[i][j] + matrix[j][k] & distance[i][j] != np.inf:
                        # set the distance from node i to node k to the distance from node i to node j + the distance from node j to node k
                        distance[i][k] = distance[i][j] + matrix[j][k]
    return distance
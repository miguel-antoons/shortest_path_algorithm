import numpy as np


def find_min(row, fridge):
    min = np.inf
    index = None
    for col in range(row):
        if row[col] < min and col not in fridge:
            min = row[col]
            index = col

    return index


def Dijkstra(C: np.matrix) -> np.matrix:
    D = np.matrix(np.ones(C.shape) * np.inf)

    for row in range(C):
        fridge = []
        D[row] = [np.inf for _ in range(D[row])]
        D[row, row] = 0

        for i in range(C):
            min = find_min(D[row], fridge)
            fridge.append(min)

            for j in range(C):
                # if the path from the minimal node is a neighbor of the
                # current node and the current node is not in the fridge
                if C[min, j] > 0 and j not in fridge:
                    # update the minimal distance with the the minimal node
                    # and the distance from the minimal node to the current
                    # path if that distance is smaller than the current
                    # minimal distance
                    D[row, j] = min(D[row, j], D[row, min] + C[min, j])

    return D

import numpy as np


def find_min(row, fridge):
    min = np.inf
    index = None
    for col in range(row.size):
        if row[col] < min and col not in fridge:
            min = row[col]
            index = col

    return index


def Dijkstra(C: np.matrix) -> np.matrix:
    size = C.shape[0]
    D = np.matrix(np.ones(C.shape) * np.inf)

    for row in range(size):
        fridge = []
        D[row, row] = 0

        for _ in range(size):
            min = find_min(np.array(D[row])[0], fridge)
            fridge.append(min)

            for j in range(size):
                # if the path from the minimal node is a neighbor of the
                # current node and the current node is not in the fridge
                if j not in fridge:
                    # update the minimal distance with the the minimal node
                    # and the distance from the minimal node to the current
                    # path if that distance is smaller than the current
                    # minimal distance
                    D[row, j] = D[row, min] + C[min, j] if D[row, j] > D[row, min] + C[min, j] else D[row, j]
                    # D[row, j] = min(D[row, j], D[row, min] + C[min, j])

    return D

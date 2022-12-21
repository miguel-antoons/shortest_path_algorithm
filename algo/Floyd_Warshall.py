import numpy as np


def Floyd_Warshall(C: np.matrix) -> np.matrix:
    """Floyd_Warshall algorithm

    Args:
        C (np.matrix): Cost matrix

    Returns:
        np.matrix: Distance matrix
    """
    n = C.shape[0]
    D = C.copy()

    for v in range(n):
        D[v, v] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                add = D[i, k] + D[k, j]
                if D[i, j] != 0 and add < D[i, j]:
                    D[i, j] = add

    return D

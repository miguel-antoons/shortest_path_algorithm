import numpy as np


def Bellman_Ford(C: np.matrix) -> np.matrix:
    """Bellman Ford Algorithm

    Parameters
    ----------
    C : np.matrix
        Cost matrix

    Returns
    -------
    np.matrix
        Distance matrix
    """

    # get size of input matrix
    size = C.shape[0]

    # create output matrix with infinite values
    D = np.matrix(np.ones(C.shape) * np.inf)

    # iterate over all source nodes
    for src in range(size):
        # set distance from source to source to 0
        D[src, src] = 0

        for _ in range((size * size) - 1):
            for row in range(size):
                for col in range(size):
                    # if the distance from the source to the current node is
                    # not infinite and the distance from the source to the
                    # current node plus the distance from the current node to
                    # the destination node is smaller than the distance from
                    # the source to the destination node
                    if (
                        D[src, row] != np.inf
                        and D[src, row] + C[row, col] < D[src, col]
                    ):
                        # update the distance from the source to the
                        # destination
                        D[src, col] = D[src, row] + C[row, col]

    return D

import numpy as np


def find_min(row, fridge):
    """
    Find the shortest path from the source node to one of its adjacent nodes
    that is not already in the fridge.

    Parameters
    ----------
    row : np.array
        row with all the path lengths from the source node to all other nodes
    fridge : list
        list with all the nodes whose path length cannot be changed anymore

    Returns
    -------
    int
        index of the shortest path from the source node to one of its adjacent
        nodes
    """
    min = np.inf
    index = None
    for col in range(row.size):
        if row[col] < min and col not in fridge:
            min = row[col]
            index = col

    return index


def Dijkstra(C: np.matrix) -> np.matrix:
    """
    Function finds the shortest path from all nodes to all other nodes
    using Dijkstra's algorithm.

    Parameters
    ----------
    C : np.matrix
        The adjacency matrix of the graph.

    Returns
    -------
    np.matrix
        The matrix with the shortest path from all nodes to all other nodes.
    """
    size = C.shape[0]
    D = np.matrix(np.ones(C.shape) * np.inf)

    # find shortest path from all nodes to all other nodes
    for src in range(size):
        fridge = []
        D[src, src] = 0

        for _ in range(size):
            # find the shortest path from the source node to one of its
            # adjacent nodes
            min = find_min(np.array(D[src])[0], fridge)
            fridge.append(min)

            for j in range(size):
                # if the path from the source node to the current node (j),
                # passing to the minimal node (min) is shorter than the
                # current path from the source node to the current node (j),
                # update the path weight.
                # This applies only for all the nodes that were not already in
                # the fridge.
                if j not in fridge:
                    D[src, j] = (
                        D[src, min] + C[min, j]
                        if D[src, j] > D[src, min] + C[min, j]
                        else D[src, j]
                    )

    return D

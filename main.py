import numpy as np
from algo.bellmanFord import bellman_ford
from algo.dijkstra import Dijkstra


def main():
    test   = open_csv("csv/graph_clem.csv")
    # result = bellman_ford(test)
    result = Dijkstra(test)
    print(result)

# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=float)
    return matrix

if __name__ == '__main__':
    main()

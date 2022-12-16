import numpy as np
from algo.bellmanFord import bellman_ford
from algo.Floyd_Warshall import Floyd_Warshall
from algo.dijkstra import Dijkstra

def main():
    test   = open_csv("csv/graph_clem.csv")
    # result1 = bellman_ford(test)
    # print(result1)
    result2 = Dijkstra(test)
    print(result2)
    result3 = Floyd_Warshall(test)
    print(result3)

# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=float)
    return matrix

if __name__ == '__main__':
    main()

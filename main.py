import numpy as np
from algo.bellmanFord import Bellman_Ford
from algo.Floyd_Warshall import Floyd_Warshall
from algo.dijkstra import Dijkstra

csv_path = "csv/graph44.csv"


def main():
    graph = open_csv(csv_path)
    print(graph, "\n")
    result = Bellman_Ford(graph)
    print(result, "\n")
    result2 = Dijkstra(graph)
    print(result2, "\n")
    result3 = Floyd_Warshall(graph)
    print(result3, "\n")

    print("Compare results :")

    if np.array_equal(result, result2) and np.array_equal(result, result3):
        print("All result matrices are equal :D", "\n")
    else:
        print("Result matrices are not equal :(", "\n")


# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=float)
    return matrix


if __name__ == '__main__':
    main()

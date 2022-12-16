import numpy as np
from algo.bellmanFord import Bellman_Ford
from algo.Floyd_Warshall import Floyd_Warshall
from algo.dijkstra import Dijkstra

def main():
    test   = open_csv("csv/graph44.csv")
    result = Bellman_Ford(test)
    print(result , "\n")
    result2 = Dijkstra(test)
    print(result2, "\n")
    result3 = Floyd_Warshall(test)
    print(result3 , "\n")

    print("Compare results", "\n")

    if np.array_equal(result, result2) and np.array_equal(result, result3):
        print("All algorithms are equal :D")
    else:
        print("Algorithms are not equal :(")

# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=float)
    return matrix

if __name__ == '__main__':
    main()

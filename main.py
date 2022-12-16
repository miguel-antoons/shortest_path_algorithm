import numpy as np
from algo.bellmanFord import bellman_ford
from algo.Floyd_Warshall import Floyd_Warshall

def main():
    test   = open_csv("csv/graph44.csv")
    # result = bellman_ford(test)
    # print(result)
    result = Floyd_Warshall(test)
    print(result)

# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=float)
    return matrix

if __name__ == '__main__':
    main()

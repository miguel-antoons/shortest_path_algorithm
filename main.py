import numpy as np
from algo.bellmanFord import bellman_ford

def main():
    test   = open_csv("csv/graph44.csv")
    result = bellman_ford(test)
    print(result)

# function to open csv and return matrix of int
def open_csv(file):
    matrix = np.genfromtxt(file, delimiter=',', dtype=int)
    return matrix

if __name__ == '__main__':
    main()

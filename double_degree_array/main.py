#!/usr/bin/python3

"""
Double Degree Array

Given: A simple graph with n <= 10^3 vertices in edge list format.

Return: An array D[1..n] where D[i] is the sum of the degree of vertex i's
neighbors.
"""

def main():
    n = 0   # number of vertices
    m = 0   # number of edges
    graph = {}

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n, m = (int(x) for x in line.split())
                graph = dict.fromkeys(list(range(1,n+1)))
                graph = {key: [] for key in graph}
            else:
                v1, v2 = (int(x) for x in line.split())
                
                # Need to add both as we are dealing with undirected graph
                graph[v1].append(v2)
                graph[v2].append(v1)

    # Get the degrees of the graph
    degree = {key: len(graph[key]) for key in graph}

    # Iterate over the nodes in the graph to find the neighbors
    # Use the degree dictionary to get the degress of the neighbors
    # Get the sum of the degree of the neighbors
    for node, neighbors in graph.items():
        neighbor_degree = 0
        for n in neighbors:
            neighbor_degree += degree[n]
        print(neighbor_degree, end=" ")
    print()

if __name__ == '__main__':
    main()

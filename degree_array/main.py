#!/usr/bin/python3

"""
Degree Array

Given: A simple graph with n <= 10^3 vertices in edge list format.

Return: An array D[1..n] where D[i] is the degree of vertex i.
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

    for key in graph:
        print(len(graph[key]), end=" ")
    print()

if __name__ == '__main__':
    main()

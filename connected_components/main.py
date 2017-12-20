#!/usr/bin/python3

"""
Connected Components

Given: A simple graph with n <= 10^3 vertices in the edge list format.

Return: The number of connected components in a graph.
"""
def main():
    n = 0   # number of vertices
    m = 0   # number of edges
    graph = {}
    not_visited = []
    connected = []

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n, m = (int(x) for x in line.split())
                graph = {x: list() for x in range(1, n+1)}
                not_visited = [x for x in range(1, n+1)]
            else:
                v1, v2 = (int(x) for x in line.split())
                graph[v1].append(v2)
                graph[v2].append(v1)

    #print(graph)
    print(connected_component(graph, not_visited))


def connected_component(graph, not_visited):
    component = 0
    while not_visited:
        root = not_visited.pop(0)
        dfs(graph, root, not_visited)
        component += 1
    return component 


def dfs(graph, root, not_visited):
    if graph[root]:
        children = graph[root]
        for child in children:
            if child in not_visited:
                not_visited.remove(child)
                dfs(graph, child, not_visited)


if __name__ == '__main__':
    main()

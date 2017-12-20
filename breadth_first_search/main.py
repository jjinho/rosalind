#!/usr/bin/python3

"""
Breadth-First Search

Given: A simple directed graph with n <= 10^3 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the length of a shortest path from the
vertex 1 to the vertex i (D[1] = 0). If i is not reachable from 1 set D[i] to
-1.
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
            else:
                v1, v2 = (int(x) for x in line.split())
                if not v1 in graph:
                    graph[v1] = [v2]
                else:
                    graph[v1].append(v2)
      
        # Distance of the nodes from the root (1)
        distances = {x:-1 for x in range(1, n+1)}

        # Tell us if the node has been visited
        visited = {x:False for x in range(1, n+1)}

        # No guarantee that node 1 will be visited
        root = sorted(graph.keys())[0]
        print(root)

        if root == 1:
            distances[root] = 0
            visited[root] = True
        
            queue = [root]
            distance = 0
            while queue:
                root = queue.pop(0)
                if root in graph:
                    children = graph[root]
                    
                    for child in children:
                        if not visited[child]:
                            visited[child] = True
                            # This is the key
                            distances[child] = distances[root] + 1
                            queue += [child]

        for k,v in distances.items():
            #print('{0}: {1}'.format(k, v), end=" ")
            print(v, end=" ")
        print()

if __name__ == '__main__':
    main()

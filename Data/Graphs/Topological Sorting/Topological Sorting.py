'''
#### Name:  Topological Sorting
Link: [link](https://www.geeksforgeeks.org/topological-sorting/)

* The graph needs to be **DAG**(Directed Acyclic Graph)
* The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).
* Topological Sorting is not uniuqe
* examples: downloading dependencies before the actual package, by pip

- We first recursively call topological sorting for all its adjacent vertices
- Push it into  stack (temporary stack)
-.Finally, print contents of stack
- **Note**: A vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in stack


'''


from collections import defaultdict 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex  of stack which stores result
        stack.append(v)


    def topologicalSort(self):
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack from bottom to top(index 0 to index -1)
        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


g.topologicalSort()
# This code is contr
## [0, 1, 3, 2, 4, 5]
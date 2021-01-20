'''
# Name:  Topological Sorting
Link: [link]()

# Sub_question_name: Topo Sort Adjacency
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


def topo_sort(n, graph, src,  visited, stack):
    visited[src] = True  # Set new vertex as visited

    for i in range(n):      # Visit all its adjacent vertices and recursively call them

        if graph[src][i] == 1 and visited[i] == False:
            topo_sort(n, graph, i, visited, stack)

    stack.append(src)


graph = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0]
         ]

n = 6
visited = [False]*n
src = 0
stack = []

for src in range(n):
    if visited[src] == False:
        topo_sort(n, graph, src, visited, stack)

print(stack[::-1])   # [5, 4, 2, 3, 1, 0]

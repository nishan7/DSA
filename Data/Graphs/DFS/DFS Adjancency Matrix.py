'''
#### Name:  DFS
Link: [link]()

#### Sub_question_name: DFS Adjancency Matrix 
Link: [link]()

Based on stack
* Depth First Search or DFS for a Graph
* The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
* So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node.
* Then backtrack and check for other unmarked nodes and traverse them. Finally print the nodes in the path.

Info
* Visit (put in stack)
* Print
* Find adj (not -1 and not visited)
* Recurse

***

Alg:
* Rule 1 : Visit the adjacent unvisited vertex. Mark it as visited. Display it. Push it in a stack.
* Rule 2 : If no adjacent vertex is found, pop up a vertex from the stack. (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
* Rule 3 : Repeat Rule 1 and Rule 2 until the stack is empty.


***

- Create a recursive function that takes the index of node and a visited array.
- Mark the current node as visited and print the node.
- Traverse all the adjacent and unmarked nodes and call the recursive function with index of adjacent node.

>**Time O(V + E) for Adjacency list, O(V*V) for adjacency matrix Space: O(V)** (E is total number of edges)
'''


def DFS(n, graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for adj in range(n):
        if visited[adj] == True:
            continue

        if graph[v][adj] == 0:  # There is not connection
            continue
        
        DFS(n, graph, adj, visited)

n = 5
graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]
v = 0
visited = [False] * n

DFS(n, graph, v, visited)   # output = [0 2 1 4 3]

'''
#### Name:  DFS
Link: [link]()

Based on stack
* Depth First Search or DFS for a Graph
* The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
* So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node.
* Then backtrack and check for other unmarked nodes and traverse them. Finally print the nodes in the path.

***

Alg:
* Rule 1 : Visit the adjacent unvisited vertex. Mark it as visited. Display it. Push it in a stack.
* Rule 2 : If no adjacent vertex is found, pop up a vertex from the stack. (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
* Rule 3 : Repeat Rule 1 and Rule 2 until the stack is empty.

***

- Create a recursive function that takes the index of node and a visited array.
- Mark the current node as visited and print the node.
- Traverse all the adjacent and unmarked nodes and call the recursive function with index of adjacent node.

>**Time O(V + E)  Space: O(V)**

'''

from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def vist_vertex(self, vertex, visited):

        # Mark the current node as visited and print it
        visited[vertex] = True
        print(vertex, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.vist_vertex(i, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, vertex):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Call the recursive helper function to print DFS traversal
        self.vist_vertex(vertex, visited)


g = Graph(5); # Total 5 vertices in graph  
# g.addEdge(1, 0);  
g.addEdge(0, 2);  
g.addEdge(2, 1);  
g.addEdge(0, 3);  
g.addEdge(1, 4);  
  
print("Following is Depth First Traversal")  
g.DFS(0) 

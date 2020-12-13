'''
#### Name:  BFS
Link: [link]()

Based on queues
It starts from top and move to level by level, it complete all the adjacent vertices, then next level

* Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.
* Rule 2 − If no adjacent vertex is found, remove the first vertex from the queue.
* Rule 3 − Repeat Rule 1 and Rule 2 until the queue is empty.

> **TE: O(E+V)**  
*Same as DFS iterative but replace stack with queues*

'''


from collections import defaultdict 
  
class Graph: 
    def __init__(self,V):
        self.V = V 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s):
        visited = [False] * self.V
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph(5) 
g.graph={0:[1,2,3],
        1:[0],
        2:[0,3],
        3:[0,2]}
  
g.BFS(0) 
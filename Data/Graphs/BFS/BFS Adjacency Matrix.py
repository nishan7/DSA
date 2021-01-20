'''
#### Name:  BFS
Link: [link]()

#### Sub_question_name: BFS Adjacency Matrix 
Link: [link]()

Based on queues
It starts from top and move to level by level, it complete all the adjacent vertices, then next level

* Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.
* Rule 2 − If no adjacent vertex is found, remove the first vertex from the queue.
* Rule 3 − Repeat Rule 1 and Rule 2 until the queue is empty.

> **TE: O(E+V)**  
*Same as DFS iterative but replace stack with queues*
'''


def BFS(n, graph, v, visited):
    queue = [v]

    while len(queue) > 0:
        src = queue.pop(0)
        print(src, end=" ")

        for adj in range(n):
            if visited[adj] == False and graph[src][adj] == 1:  # Not visited and has a link, then add to queue
                queue.append(adj)


n = 5
graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]
v = 0
visited = [False] * n

BFS(n, graph, v, visited)   # output = [0 2 1 4 3]

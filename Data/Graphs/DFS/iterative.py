'''
#### Name:  DFS
Link: [link]()

a

#### Sub_question_name: iterative 
Link: [link]()

Instead of recursive call, the vertices are placed in a stack
 '''


def DFS(n, graph, v, visited):
    stack = [v]
    visited[v] = True
    # print(v)

    while len(stack) > 0:
        src = stack.pop()
        print(src, end=" ")  # In recursive printing was done when it was called

        # Correct the order so , second one is selected
        for adj in reversed(range(n)):  # n is adjancent vertices for adjancency list and (all vertices)*(All their ajdacent vertices) = All edges
            if visited[adj] == True:
                continue

            if graph[src][adj] == 0:
                continue

            stack.append(adj)


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

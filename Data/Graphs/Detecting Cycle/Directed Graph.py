'''
#### Name:  Detecting Cycle
Link: [link]()

#### Sub_question_name: Directed Graph 
Link: [link]()


** O(E+V) SC: O(V) Recursion Stack **
 '''


def utility(n, start, graph, visited, recur):
    visited[start] = True
    recur[start] = True

    for neigbour in graph[start]:
        if visited[neigbour] == False:
            if utility(n, neigbour, graph, visited, recur) == True:
                return True
        elif recur[neigbour] == True:
            return True

    recur[start] = False
    return False


def is_cyclic(n, start, graph, visited):
    visited[start] = True
    recur = [False] * n

    for neigbour in graph[start]:   # Maybe for disconneted
        if not visited[neigbour]:
            if utility(n, neigbour, graph, visited, recur) == True:
                return True

    return False


def create_graph(n, edges):
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)
    return graph


n = 4
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
graph = create_graph(n, edges)

visited = [False] * n
recur = [False]*n
start = 0
print(is_cyclic(n, start, graph, visited))              # If disconnected graph

visited = [False] * n
recur = [False]*n
start = 0
# For simple ones this one will also work
print(utility(n, start, graph, visited, recur))

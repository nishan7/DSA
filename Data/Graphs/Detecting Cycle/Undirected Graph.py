'''
#### Name:  Detecting Cycle
Link: [link]()

#### Sub_question_name: Undirected Graph 
Link: [link]()


** O(E+V) SC: O(V) Recursion Stack **
 '''


def utility(n, start, graph, visited, parent):
    visited[start] = True

    for neigbour in graph[start]:
        if visited[neigbour] == False:
            if utility(n, neigbour, graph, visited, start) == True:
                return True
        elif neigbour != parent:  # In undirected graph as there is self link so neighbour == parent can happen
            return True

    return False


def is_cyclic(n, start, graph, visited):
    visited[start] = True

    for neigbour in graph[start]:   # Maybe for disconneted
        if not visited[neigbour]:
            if utility(n, neigbour, graph, visited, start) == True:
                return True

    return False


def create_graph(n, edges):
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph


n = 5
edges = [(1, 0), (1, 2), (2, 0), (0, 3), (3, 4)]
graph = create_graph(n, edges)
visited = [False] * n
recur = [False]*n
start = 0
print(is_cyclic(n, start, graph, visited))              # If disconnected graph

n = 3
edges = [(0, 1), (1, 2)]
graph = create_graph(n, edges)
visited = [False] * n
start = 0
print(utility(n, start, graph, visited, None))

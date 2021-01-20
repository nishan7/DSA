'''
#### Name:  Dijkskra Alg
Link: [link]()

A) Given a source vertex and graph, It is find shortest paths from source to all vertices in the given graph
B) Both for directed and undirected graphs
**TE: O(V^2)**
Can’t use for negative weight, negative weights is handled by bellman ford’s

Alg
1) Create a dist array with 0 on the source vertex
2) Create a sptTree array stating whether a there is  minimum distance from source to the vertex or not
3) Get the next closest vertex
5) Update the dist vertex using the closest vertex
6) Repeat above 2 steps for all the vertex in the graph


'''


def find_closest(n, graph, src, distance, visited):
    min_value = float('inf')
    min_index = src

    for i in range(n):
        if visited[i] == False and distance[i] < min_value:
            min_value = distance[i]
            min_index = i

    return min_index


def dijk(n, graph, src):
    distance = [float('inf')]*n
    visited = [False] * n

    distance[src] = 0

    for i in range(n):
        u = find_closest(n, graph, src,  distance, visited)
        visited[u] = True

        for v in range(n):
            if visited[v] == False and graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]
n = 9
src = 0

distance = dijk(n, graph, src)
print(distance)

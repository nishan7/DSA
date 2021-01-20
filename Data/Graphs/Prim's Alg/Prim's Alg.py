'''
#### Name:  Prim's Alg
Link: [link](http:\\geeksforgeeks.com)


Prim's Algorithm is used to find the minimum spanning tree from a graph


1) Create a set mstSet that keeps track of vertices already included in MST. 
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign key value as 0 for the first vertex so that it is picked first. 
3) While mstSet doesn't include all vertices // For all vertices    

A) Pick a vertex u which is not there in mstSet and has minimum key value.   
B) Include u to mstSet.    
C) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v


**TE: O(V^2)  Adjancency list O(ElogV)**
'''

def find_closest(n, graph, src, visited, distance):
    min_value = float('inf')
    min_index = src

    for i in range(n):
        if visited[i] == False and distance[i] < min_value:
            min_value = distance[i]
            min_index = i
    
    return min_index

def prims(n, graph, src):
    distance = [float('inf')]*n
    visited = [False] * n
    parent = [-1] * n

    distance[src] = 0

    for i in range(n):
        u = find_closest(n, graph, src, visited, distance)
        visited[u] = True

        for v in range(n):
            if visited[v] == False and graph[u][v] != 0 and distance[v] > graph[u][v]:
                distance[v] = graph[u][v]
                parent[v] = u
        
    
    return parent, distance
                
graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
n = 5
src = 0

parent, distance = prims(n, graph, src)


for i in range(1,n):   # For V vertices there will be V-1 edges in MST
    print("{} -> {} : {}".format(parent[i], i, distance[i]))


# 0 -> 1 : 2
# 1 -> 2 : 3
# 0 -> 3 : 6
# 1 -> 4 : 5
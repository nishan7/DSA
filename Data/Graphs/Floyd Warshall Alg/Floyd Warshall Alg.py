from pprint import pprint

'''
#### Name:  Floyd Warshall Alg
Link: [link]()

Main idea in floyd warshall alg is that it check whether the existing path is shorter or is there is shorter path via intermediate node k

**TE: O(V^3)**
'''


def floyd_warshall(adj, n):

    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj[i][j] = min(adj[i][k]+adj[k][j], adj[i][j])


INF = float('inf')
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

floyd_warshall(graph, 4)
print(graph)
# [[0, 5, 8, 9],
#  [inf, 0, 3, 4],
#  [inf, inf, 0, 1],
#  [inf, inf, inf, 0]
# ]

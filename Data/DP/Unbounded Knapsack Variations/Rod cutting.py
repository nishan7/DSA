'''
#### Name:  Unbounded Knapsack Variations
Link: [link]()

#### Sub_question_name: Rod cutting 
Link: [link](https://www.youtube.com/watch?v=SZqAQLjDsag&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14)

It is similar to knapsack problem   
length == wgt and price == value   and N == W   
Unbounded knapsack as we can use the same length more than once
'''
from pprint import pprint
def rod_cutting(value, length):
    N = len(length)
    n =len(value)
    T = [[0 for j in range(N+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, N+1):
            if length[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], value[i-1] + T[i][j - length[i-1]])

    return T[n][n]

value = [1, 5, 8, 9, 10, 17, 17, 20]
length = list(range(1, len(value)+1))  # Might be provided in the question

print(rod_cutting(value, length))
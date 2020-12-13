'''
#### Name:  Unbounded Knapsack CoinChange no of ways
Link: [link]()

#### Sub_question_name: Coin Change: number of ways 
Link: [link]()

Unbounded subset sum problem , 
**TC: O(mn) SC: O(n)**
'''
from pprint import pprint


def count_change(coins, n, req_sum):
    T = []
    n = len(coins)
    for i in range(n+1):
        row = []
        for j in range(req_sum+1):
            if j == 0:
                row.append(1)  # if req_sum is 0, 1 subset is possible
            elif i == 0:
                row.append(0)
            else:
                row.append(0)
        T.append(row)

    for i in range(1, n+1):
        for j in range(1, req_sum+1):
            if coins[i-1] > req_sum:
                T[i][j] = T[i-1][j]

            else:
                T[i][j] = T[i-1][j]+ T[i][j-coins[i-1]]

    return T[n][req_sum]


coins = [1, 2, 3]
n = len(coins)
print(count_change(coins, n, 4))

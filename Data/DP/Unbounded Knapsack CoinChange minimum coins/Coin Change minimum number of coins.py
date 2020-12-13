'''
#### Name:  Unbounded Knapsack CoinChange minimum coins
Link: [link]()

#### Sub_question_name: Coin Change: minimum number of coins 
Link: [link]()

**TC O(n*coin_sum)**
'''


def min_coins(coins, n, req_sum):
    T = []
    n = len(coins)
    for i in range(n+1):
        row = []
        for j in range(req_sum+1):
            if i == 0:
                row.append(float('inf'))  # 0/0 =inf, 1/0=inf, 2/0=inf ...
            elif j == 0:
                row.append(0)
            elif j % coins[0] == 0:   
                row.append(1)
            else:    # eg. 3 cannot be addeds such that it can have sum 4
                row.append(float('inf'))

        T.append(row)

    for i in range(1, n+1):
        for j in range(1, req_sum+1):
            if coins[i-1] > req_sum:
                T[i][j] = T[i-1][j]

            else:
                T[i][j] = min(T[i-1][j] ,1 + T[i][j-coins[i-1]])  # 1 denotes one answer
 
    return T[n][req_sum]


coins = [25,10,5]
n = len(coins)
coins_sum = 30
print(min_coins(coins, n, coins_sum))

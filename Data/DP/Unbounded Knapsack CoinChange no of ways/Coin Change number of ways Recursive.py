'''
#### Name:  Unbounded Knapsack CoinChange no of ways
Link: [link]()

#### Sub_question_name: Coin Change: number of ways Recursive 
Link: [link]()

'''
def coin_change(n, coins, amount):
    if amount == 0:
        return 1

    if n == 0 or amount < 0:
        return 0

    return coin_change(n-1, coins, amount) + coin_change(n, coins, amount-coins[n-1])

coins = [1, 2, 5]
amount = 5
n= len(coins)
print(coin_change(n, coins, amount))  # 4




# Memoization

def coin_change(n, coins, amount, T):
    if T[n][amount] != -1:
        return T[n][amount]
    if amount == 0:
        return 1

    if n == 0 or amount < 0:
        return 0

    T[n][amount] =  coin_change(n-1, coins, amount, T) + coin_change(n, coins, amount-coins[n-1], T)
    return T[n][amount]

coins = [1, 2, 5]
amount = 5
n= len(coins)
T = [[-1 for i in range(amount+1)] for j in range(n+1)]
print(coin_change(n, coins, amount, T))  # 4

'''
Works

dp = [0] * (amount + 1)
dp[0] = 1
for i in coins:
    for j in range(1, amount + 1):
        if j >= i:
            dp[j] += dp[j - i]
return dp[amount]

'''

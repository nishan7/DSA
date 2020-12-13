'''
#### Name:  Unbounded Knapsack CoinChange minimum coins
Link: [link]()

#### Sub_question_name: Coin Change: minimum number of coins arr Recursive 
Link: [link]()

'''
# Recurisve


def min_coin_change(coins, amount):
    n = len(coins)
    if amount == 0:    # !! The amount is zero, 0 coins are needed
        return 0

    # if n == 0:
    #     return float('inf')       # 1/0, 2/0

    min_count = float('inf')
    for i in range(n):
        if coins[i] <= amount:
            min_count = min(
                min_count, 1 + min_coin_change(coins, amount-coins[i]))

    return min_count


coins = [1, 2, 111, 5]
amount = 11

print(min_coin_change(coins, amount))


# Memozied Solution
def min_coin_change(coins, amount, T):
    n = len(coins)
    if T[amount] != -1:
        return T[amount]

    if amount == 0:    # !! The amount is zero, 0 coins are needed
        return 0

    # if n == 0:
    #     return float('inf')       # 1/0, 2/0

    min_count = float('inf')
    for i in range(n):   # Check for every coin
        if coins[i] <= amount:
            min_count = min(
                min_count, 1 + min_coin_change(coins, amount-coins[i], T))
            

    T[amount] = min_count
    return T[amount]


coins = [1, 2, 111, 5]
amount = 1


# Need to find the minimum so everything is float('inf')
T = [-1 for _ in range(amount+1)]

print(min_coin_change(coins, amount, T))
print(T)
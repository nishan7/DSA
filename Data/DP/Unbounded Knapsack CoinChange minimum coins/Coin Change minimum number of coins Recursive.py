'''
#### Name:  Unbounded Knapsack CoinChange minimum coins
Link: [link]()

#### Sub_question_name: Coin Change: minimum number of coins Recursive 
Link: [link]()

'''
# !!! NOT WORKING !!!!
# Recursive
from pprint import pprint

def min_coins(coins, amount):
    n = len(coins)
    if amount == 0:
        return 0

    if n == 0:                     #1/0, 2/0
        return float('inf')

    coin = coins.pop()
    if coin > amount:        # We couldn't not store
        # n is always reduced, to reduce input
        return min_coins(coins, amount)

    else:
        return min(1 + min_coins(coins, amount-coin,),  # We choose to store it # Choice Diagram
                   min_coins(coins, amount)    # W choose not to store it
                   )


coins = [1, 2, 5]
n = len(coins)
amount = 11
print(min_coins(coins, amount))


# Memoziation
def min_coins(coins, amount, T):
    n = len(coins)
    if T[n][amount] != -1:
        return T[n][amount]

    if amount == 0:
        return 0

    if n == 0:
        return float('inf')

    coin = coins.pop()
    if coin > amount:        # We couldn't not store
        # n is always reduced, to reduce input
        T[n][amount]= min_coins(coins, amount, T)
        return T[n][amount]

    else:
        
        T[n][amount]= min(1 + min_coins(coins, amount-coin,T),  # We choose to store it # Choice Diagram
                      min_coins(coins, amount, T)    # W choose not to store it
                   )
        return T[n][amount]


# Need to find the minimum so everything is float('inf')
coins = [1, 2, 5]
n = len(coins)
amount = 11

T = [[-1 for _ in range(amount+1)] for i in range(len(coins)+1)]


print(min_coins(coins, amount, T))
pprint(T)
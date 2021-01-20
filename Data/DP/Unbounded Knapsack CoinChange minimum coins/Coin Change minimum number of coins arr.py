'''
#### Name:  Unbounded Knapsack CoinChange minimum coins
Link: [link]()

#### Sub_question_name: Coin Change: minimum number of coins arr 
Link: [link]()

'''

def min_coin_change(coins, amount):
    # Need to find the minimum so everything is float('inf')
    T = [float('inf') for _ in range(amount+1)]
    T[0] = 0 # If amount required is 0, then we need 0 coins

    n = len(coins)
    for i in range(1, amount+1):
        for j in range(1, n+1):
            if coins[j-1] <= i:
                T[i] = min(T[i], 1 + T[i - coins[j-1]]) # if coins[j-1] == 3, amount(j)=5; Get count for amount '2'=> T[5-3]=T[2]
    
    print(T)
    return T[-1]



coins = [1, 2, 111, 5]
amount = 11



print(min_coin_change(coins, amount))

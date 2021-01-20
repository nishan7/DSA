'''
#### Name:  Coin Piles
Link: [link]()
# WRONG!!
'''

def solve(n, k, coins):
    coins.sort(reverse=True)
    smallest = coins[-1]
    
    count = 0
    for coin in coins:
        extra = coin - k - smallest
        if extra > 0:
            count += extra
        else:
            return count
    
    return count



t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split()))
    coins = list(map(int, input().strip().split()))
    
    print(solve(n, k, coins))



# 3
# 4 0
# 2 2 2 2
# 6 3
# 1 2 5 1 1 1
# 6 3
# 1 5 1 2 5 1
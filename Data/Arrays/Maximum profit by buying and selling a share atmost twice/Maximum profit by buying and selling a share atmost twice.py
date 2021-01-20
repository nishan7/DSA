'''
#### Name:  Maximum profit by buying and selling a share atmost twice
Link: [link]()

'''


def max_prof(price):
    n = len(price)
    profit = [0] * n


    max_so_far = price[-1]
    for i in range(n-2, -1, -1):
        profit[i] = max(profit[i+1], max_so_far - price[i])
        max_so_far = max(max_so_far, price[i])

    print(profit)
    min_so_far = price[0]
    for i in range(1, n):
        profit[i] = max(profit[i-1], profit[i] + (price[i] - min_so_far))
        min_so_far = min(min_so_far, price[i])

    print(profit)

price = [2, 4, 7, 5, 4, 3, 5]
max_prof(price)           # 7

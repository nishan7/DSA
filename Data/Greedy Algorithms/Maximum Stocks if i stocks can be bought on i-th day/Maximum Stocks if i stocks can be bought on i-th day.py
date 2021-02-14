'''
#### Name:  Maximum Stocks if i stocks can be bought on i-th day
Link: [link]()

1) Create list of tuples (day, price)
2) Sort by lowest price and keep track of stocks_count

'''


# 

def max_stocks(stocks, k):
    stocks_days = [(s, idx) for idx, s in enumerate(stocks, start=1)]
    stocks_days.sort(key=lambda x: x[0])

    stocks_count = 0
    for price, amount in stocks_days:
        can_buy = min(k // price, amount)
        k -= price * can_buy
        stocks_count += can_buy

        if k == 0:
            break
    
    print(stocks_count)


stocks = [10, 7, 19]  # 4
k = 45

# stocks = [7, 4, 10]  # 6
# k = 100

max_stocks(stocks, k)


# def max_stocks(stocks, k):
#     stocks_days = [(s, idx) for idx, s in enumerate(stocks, start=1)]
#     stocks_days.sort(key=lambda x: x[0])

#     stocks_count = 0
#     for price, amount in stocks_days:
#         if k - price*amount > 0:
#             k -= price*amount
#             stocks_count += amount

#         else:
#             buying_amount = k//price
#             stocks_count += buying_amount
#             break

#     print(stocks_count)

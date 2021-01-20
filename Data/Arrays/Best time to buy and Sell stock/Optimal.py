'''
#### Name:  Best time to buy and Sell stock
Link: [link]()

#### Sub_question_name: Optimal 
Link: [link]()

'''

def stock(arr):
    n = len(arr)
    max_profit = 0
    min_price = float('inf')
    for price in arr:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price- min_price)
    print(max_profit)

arr= [7,1,5,3,6,4]
stock(arr)
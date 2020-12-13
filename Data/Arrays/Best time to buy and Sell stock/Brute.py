'''
#### Name:  Best time to buy and Sell stock
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

'''


def stock(arr):
    n = len(arr)
    max_profit = 0
    for i in range(1, n):
        for j in range(i):
            max_profit = max(max_profit, arr[i]-arr[j])
    
    print(max_profit)  #5

arr= [7,1,5,3,6,4]
stock(arr)
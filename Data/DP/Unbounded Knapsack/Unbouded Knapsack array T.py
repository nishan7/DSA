'''
#### Name:  Unbounded Knapsack
Link: [link]()

#### Sub_question_name: Unbouded Knapsack array T 
Link: [link]()

'''


def knapsack(value, wgt, W):
    n = len(value)
    T = [0 for i in range(W+1)]  # need to initalize all to zero

    for i in range(1, W+1):
        for j in range(1, n+1):
            if wgt[j-1] <= i:
                T[i] = max(T[i], value[j-1] + T[i-wgt[j-1]])

    return T[-1]


W = 45
value = [40, 60, 50]
wgt = [12, 20, 15]
# # Output: 150


print(knapsack(value, wgt, W))

'''
#### Name:  Fractional Knapsack
Link: [link]()

'''

def knapsack(n, value, wgt, W):
    ratio = [v/w for v, w in zip(value, wgt)]
    index = list(range(n))  # As we need to sort the index
    fractions = [0] * n   
    index.sort(key=lambda x: ratio[x], reverse=True)
    max_value = 0

    for i in index:
        if wgt[i] <= W:
            fractions[i] = 1
            max_value += value[i]
            W -= wgt[i]
        
        else:
            fractions[i] = W/wgt[i]
            max_value += value[i] * W/wgt[i]
            break

    return max_value, fractions







n = 3
value = [60,100,120]
wgt = [10,20,30]
W = 50
print(knapsack(n, value, wgt, W))

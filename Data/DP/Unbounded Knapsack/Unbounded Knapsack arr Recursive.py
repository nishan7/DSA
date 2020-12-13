'''
#### Name:  Unbounded Knapsack
Link: [link]()

#### Sub_question_name: Unbounded Knapsack arr Recursive 
Link: [link]()

'''


def knapsack(wgt, values, W):
    n = len(values)
    if W <= 0:  # If capacity is 0, we can put no item so value 0
        return 0

    max_value = 0
    for i in range(n):
        if wgt[i] <= W:
            max_value = max(max_value,        # Use old value
                            values[i] + knapsack(wgt, values, W - wgt[i]))   # Use the value[i] and find value for capacity = W-value[i];  if value[i] = 3, W=5; find value for W=2

    return max_value


W = 100
value = [10, 30, 20]
wgt = [5, 10, 15]
# Output: 300


print(knapsack(wgt, value, W))



# Memoziation
def knapsack(wgt, values, W, T):
    n = len(values)

    if T[W] != -1:
        return T[W]

    if W <= 0:  # If capacity is 0, we can put no item so value 0
        return 0

    for i in range(n):
        if wgt[i] <= W:
            T[W] = max(T[W],        # Use old value
                       values[i] + knapsack(wgt, values, W - wgt[i], T))   # Use the value[i] and find value for capacity = W-value[i];  if value[i] = 3, W=5; find value for W=2

    return T[W]


W = 100
value = [10, 30, 20]
wgt = [5, 10, 15]
# Output: 300
T = [-1 for i in range(W+1)]

print(knapsack(wgt, value, W, T))

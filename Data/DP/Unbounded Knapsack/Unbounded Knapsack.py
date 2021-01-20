'''
#### Name:  Unbounded Knapsack
Link: [link](https://www.youtube.com/watch?v=aycn9KO8_Ls&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=13)

#### We dont change/reduce values
1) Mutliple items of same items are considered
2) Item once selected can be selected again

'''
# from pprint import pprint


def knapsack(value, wgt, W):
    n = len(value)

    T = []
    for i in range(n+1):
        row = []
        for j in range(W+1):
            if i == 0 or W == 0:
                row.append(0)
            row.append(0)
        T.append(row)

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wgt[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], value[i-1]+T[i][j-wgt[i-1]])
    
    # pprint(T)
    return T[n][W]


W = 100
value = [10, 30, 20]
wgt = [5, 10, 15]
 # Output: 300

# W = 45
# value =[40,60,50]
# wgt = [12,20,15]
# # Output: 150


print(knapsack(value, wgt, W))

'''
#### Name:  0 - 1 knapsack
Link: [link]()

#### Sub_question_name: Memoization 
Link: [link](https://www.youtube.com/watch?v=fJbIuhs24zQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=4)

Create a matrix for those variables that are changing

**TC: O(N*W) SC: O(N*W)**
'''

from pprint import pprint


def knapsack(wgt, value, W, n, T):
    # Base
    if W == 0 or n == 0:
        return 0

    # Memoziation part
    if T[n][W] != -1:
        print("used mes")
        return T[n][W]

    # Induction, acc to choice tree
    if wgt[n-1] > W:
        T[n][W] = knapsack(wgt, value, W, n-1, T)
        return T[n][W]

    else:
        T[n][W] = max(value[n-1] + knapsack(wgt, value, W-wgt[n-1], n-1, T),
                      knapsack(wgt, value, W, n-1, T))
        return T[n][W]


wgt = [1, 3, 4, 5]
value = [1, 4, 5, 7]
n = len(value)
W = 7


T = [[-1 for j in range(W+1)] for i in range(n+1)]   # n vs W

# pprint(T)

n = len(value)

print(knapsack(wgt, value, W, n, T))  # 9

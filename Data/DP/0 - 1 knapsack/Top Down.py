'''
#### Name:  0 - 1 knapsack
Link: [link]()

#### Sub_question_name: Top Down 
Link: [link](https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5)

The matrix is created from those values that changes ie n and W   
The max profit when n=n and W=W, is in matrix T[n][W]   
Answer is in T[n][W]   
Matix is filled as
- Initallization  (Base condition is intallization)
- By Functions  
 
**TC: O(N*W) SC: O(N*W)**
'''
from pprint import pprint


def knapsack(wgt, value, W, n, T):

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wgt[i-1] > j:  # if new item is greater than W, then continue, wgt[i-1] is the current item weight (as it starts from 1 to n+1)
                T[i][j] = T[i-1][j]
            else:             
                T[i][j] = max(value[i-1]+T[i-1][j-wgt[i-1]], T[i-1][j])

    return T[n][W]

wgt = [1, 3, 4, 5]
value = [1, 4, 5, 7]
n = len(value)
W = 7


T = [[0 if (i == 0 or j == 0) else None for j in range(W+1)]
     for i in range(n+1)]   # if(w==0 or n==0) return 0



print(knapsack(wgt, value, W, n, T))  # 9
pprint(T)
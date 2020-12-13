'''
#### Name:  0 - 1 knapsack
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link](https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3)

Choice Diagram: whethe a item is included or not based on weight:
a) if w1 > W: not
b) if w1 <= W: may or maynot  

Base condition is smallest valid input


**TC: O(2^n) SC: O(1)**
'''


def knapsack(wgt, value, W, n):
    if n == 0 or W == 0:
        return 0

    if wgt[n-1] > W:        # We couldn't not store
        return knapsack(wgt, value, W, n-1)  # n is always reduced, to reduce input

    else:
        return max(value[n-1] + knapsack(wgt, value, W-wgt[n-1], n-1),  # We choose to store it # Choice Diagram
                   knapsack(wgt, value, W, n-1)    # W choose not to store it
                   )


wgt = [1, 3, 4, 5]
value = [1, 4, 5, 7]
n = len(value)
W = 7

n = len(value)

print(knapsack(wgt, value, W, n))  # 9

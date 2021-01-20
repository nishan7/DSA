'''
#### Name:  Egg Dropping
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link](https://www.youtube.com/watch?v=S49zeUjeUL0&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=43)


You are given N floor and K eggs. You have to minimize the number of 
times you have to drop the eggs to find the critical floor where critical floor means 
the floor beyond which eggs start to break. Assumptions of the problem:


Start from bottom and go up
'''


def egg(e, f):

    if f == 0 or f == 1:
        return f

    if e == 1:
        return f

    count = float('inf')
    for k in range(1, f+1):
        down = egg(e-1, f-1)   # Egg broke need to look down
        up = egg(e, f-k)  # Egg didn't broke, can skip all the floors below k
        tries = max(down, up)

        count = min(count, tries)
    return count


e = 2
f = 4   # 3
print(egg(e, f))
print()

'''
#### Name:  Egg Dropping
Link: [link]()

#### Sub_question_name: Memoization 
Link: [link](https://www.youtube.com/watch?v=gr2NtY-2QUY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=44)

'''


def egg(e, f, T):

    if T[f][e] != -1:
        return T[f][e]

    if f == 0 or f == 1:
        return f

    if e == 1:
        return f

    count = float('inf')
    for k in range(1, f+1):

        down = egg(e-1, f-1, T)   # Egg broke need to look down
        T[f-1][e-1] =down

        up = egg(e, f-k, T)  # Egg didn't broke, can skip all the floors below k
        T[f-k][e]=up

        tries = max(down, up)

        count = min(count, tries)
    
    T[f][e] = count
    return count


e = 2
f = 4   # 3
T = [[-1]*(e+1) for _ in range(f+1)]
print(egg(e, f, T))
print()

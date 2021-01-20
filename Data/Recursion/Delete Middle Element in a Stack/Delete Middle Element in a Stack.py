'''
#### Name:  Delete Middle Element in a Stack
Link: [link](https://www.youtube.com/watch?v=oCcUNRMl7dA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=8)



'''
# stack = [1,2,7,1,9]


def del_mid(stack):
    if len(stack) == 0:
        return

    mid = len(stack)//2 + 0  # For even numbers, 0 for first and 1 for last middle elemtn

    solve(stack, mid)


def solve(stack, mid):
    if mid == 0:
        stack.pop()
        return

    tos = stack.pop()

    solve(stack, mid-1)
    stack.append(tos)


stack = [1, 2, 8,  7, 1, 9]
del_mid(stack)
print(stack)

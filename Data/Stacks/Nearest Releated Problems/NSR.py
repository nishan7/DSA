'''
#### Name:  Nearest Releated Problems
Link: [link]()

#### Sub_question_name: NSR 
Link: [link]()

'''

'''
val = 999
for i in range(0,n) 
    for j in range(i+1, n)
        val = min(val, arr[j])
'''


def nsr(arr):
    n = len(arr)

    output_rev = [-1]
    stack = [arr[-1]]

    for i in range(n-2, -1, -1):

        while stack:
            if stack[-1] < arr[i]:
                output_rev.append(stack[-1])
                stack.append(arr[i])
                break
            else:
                stack.pop()

        if len(stack) == 0:
            output_rev.append(-1)
            stack.append(arr[i])

    return output_rev[::-1]


arr = [1, 0, 0, 5, 2, 5, 1, 4]
print(nsr(arr))


# [1,3,2,4] => [-1, 2, -1, -1]
# [1, 0, 0, 5, 2, 5, 1, 4] => [0, -1, -1, 2, 1, 1, -1, -1]

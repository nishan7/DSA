'''
#### Name:  Nearest Releated Problems
Link: [link]()

#### Sub_question_name: NSL 
Link: [link]()

##  Nearst Smallest element to left

**TC: O(n)**
'''

'''
val = 999
for i in range(0,n) 
    for j in range(i-1, -1,-1)
        val = min(val, arr[j])
'''


def nsl(arr):
    n = len(arr)

    output = [-1]
    stack = [arr[0]]

    for i in range(1, n):

        while stack:
            if stack[-1] < arr[i]:
                output.append(stack[-1])
                stack.append(arr[i])
                break
            else:
                stack.pop()

        if len(stack) == 0:
            output.append(-1)
            stack.append(arr[i])

    return output


arr = [1, 0, 0, 5, 2, 5, 1, 4]
print(nsl(arr))


# [1,3,2,4] => [-1, 1, 1, 2]
# [1, 0, 0, 5, 2, 5, 1, 4] => [-1, -1, -1, 0, 0, 2, 0, 1]
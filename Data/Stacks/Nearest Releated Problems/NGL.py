'''
#### Name:  Nearest Releated Problems
Link: [link]()

#### Sub_question_name: NGL 
Link: [link]()

## Nearest Greater to Left(NGL)
'''

'''
val = -1
for i in range(0,n)
    for j in range(i-1,-1, -1)
        val = max(val, arr[j])
'''

def ngl(arr):
    n = len(arr)

    output = [-1]
    stack = [arr[0]]

    for i in range(1, n):

        while stack:
            if stack[-1] > arr[i]:
                output.append(stack[-1])
                stack.append(arr[i])
                break
            else:
                stack.pop()

        if len(stack) == 0:
            output.append(-1)
            stack.append(arr[i])
    
    return output


arr = [1,3, 2, 4]
print(ngl(arr))

## [1, 3, 2, 4] => [-1, -1, 3, -1]

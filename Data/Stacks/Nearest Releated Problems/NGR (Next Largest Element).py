'''
#### Name:  Nearest Releated Problems
Link: [link]()

#### Sub_question_name: NGR (Next Largest Element) 
Link: [youtube_link](https://www.youtube.com/watch?v=NXOOYYwpbg4)

'''

'''
val = -1
for i in range(0, n):
    for j in range(i+1, n):
        val = max(val, arr[j])

'''


def ngr(arr):
    n = len(arr)
    output_rev = []
    
    stack = []

    output_rev.append(-1)  # there is no right largest element for last index of array
    stack.append(arr[-1])   # We start with placing last element to arrat 

    for i in range(n-2, -1, -1):  # reversed(arr[:-1])
        while len(stack) != 0:
            if stack[-1] > arr[i]:
                output_rev.append(stack[-1])
                stack.append(arr[i])
                break
            else:
                stack.pop()
        
        if len(stack) == 0:
            output_rev.append(-1)
            stack.append(arr[i])

    return output_rev[::-1]



print(ngr([1,0,0,4,2,1]))

# [1,3,2,4] => [3, 4, 4, -1]
# [1,0,0,4,2,1] => [4, 4, 4, -1, -1, -1]


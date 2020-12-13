'''
#### Name:  Stock Span
Link: [link]()

# NGL is used with (value, idx) in stack, difference between NGL's index and current element's index

Given a list of prices with n number of days

Find the number of consecutive price in previous days that are smaller or equal to the price of the day

Just get NGL(Nearest Greater element on the left)'s index and subtract to get number of prices

**O(n)**
'''

def stock(arr):
    n = len(arr)
    
    stack = [(arr[0], 0)]
    output = [1]

    for i in range(1, n):


        while stack:
            if stack[-1][0] > arr[i]:
                output.append(i - stack[-1][1])
                stack.append((arr[i], i))
                break
            else:
                stack.pop()  
                

        if len(stack) == 0:
            output.append(i + 1)  # Everything on the right is small, so ctr is index + 1
            stack.append((arr[i], i))

    return output

print(stock([100,80,60,70,60,75,85]))

# [100,80,60,70,60,75,85] => [1, 1, 1, 2, 1, 4, 6]
# [1,2,4,5,3] => [1, 2, 3, 4, 1]
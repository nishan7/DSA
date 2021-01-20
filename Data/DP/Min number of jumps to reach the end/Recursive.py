'''
#### Name:  Min number of jumps to reach the end
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

'''
def jumps(arr, start):
    if len(arr) == start+1:  # If in last index,  we got the result
        return 0
    
    if arr[start] == 0:            # if zero no solution
        return float('inf')

    value = arr[start]
    min_jumps = float('inf')
    for i in range(1, value+1):
        if start+i >= len(arr):
            break
        count = 1 + jumps(arr, start+i)  # count no of jumps for a start
        min_jumps = min(min_jumps, count)
    
    return min_jumps



arr = [1, 3, 6, 1, 0, 9]
print(jumps(arr, 0))
'''
#### Name:  Min number of jumps to reach the end
Link: [link]()

#### Sub_question_name: Memoization 
Link: [link]()

'''


def jumps(arr, start, T):
    if T[start] != -1:
        return T[start]

    if len(arr) == start+1:  # If in last index,  we got the result
        return 0

    if arr[start] == 0:            # if zero no solution
        return float('inf')

    value = arr[start]
    min_jumps = float('inf')

    for i in range(1, value+1):  # e.g for 3; we can make 1, 2 or 3 jumps
        if start+i >= len(arr):
            break

        T[start+i] = jumps(arr, start+i, T) # count no of jumps for a start
        count = 1 + T[start+i]

        min_jumps = min(min_jumps, count)
    
    T[start] = min_jumps
    return min_jumps


arr = [1, 3, 6, 1, 0, 9]
T = [-1]*(len(arr)+1)
print(jumps(arr, 0, T))
print()

'''
#### Name:  Min number of jumps to reach the end
Link: [link]()

#### Sub_question_name: Top Down 
Link: [link]()

'''


def jumps(arr):
    n = len(arr)
    T = [float('inf')]*(n)
    T[n-1] = 0

    for i in range(n-2, -1, -1):
        val = arr[i]

        min_jumps = float('inf')
        for j in range(1, val+1):
            if i+j >= n:  # Out of Bounds
                break    
            
            min_jumps = min(min_jumps, 1 + T[i+j])
            
        T[i] = min_jumps 
    print(T[0])
        


arr = [1, 3, 6, 1, 0, 9]
arr = [3, 2, 4, 2, 0, 2, 3, 1, 2, 2]
print(jumps(arr))
# print()

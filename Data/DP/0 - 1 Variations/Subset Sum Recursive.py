'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Subset Sum Recursive 
Link: [link]()

'''

def subset(arr, req_sum):
    if req_sum == 0:
        return True

    if len(arr) == 0:
        return False

    element = arr[-1]
    arr = arr[:-1]

    if element > req_sum:
        return subset(arr, req_sum)

    else:
        return subset(arr, req_sum) or subset(arr, req_sum-element)

arr = [2, 3, 7, 8, 10]
n = len(arr)
req_sum = 11
print(subset(arr, req_sum))

## Memoization

def subset_memo(arr, req_sum, T):
    n = len(arr)
    if T[n][req_sum] != -1:
        return T[n][req_sum]

    if req_sum == 0:
        return True

    if len(arr) == 0:
        return False

    element = arr[-1]
    arr = arr[:-1]

    if element > req_sum:
        T[n][req_sum]= subset_memo(arr, req_sum, T)
        return T[n][req_sum]
    
    else:
        T[n][req_sum]= subset_memo(arr, req_sum, T) or subset_memo(arr, req_sum-element, T)
        return T[n][req_sum]

arr = [2, 3, 7, 8, 10]
n = len(arr)
req_sum = 11
T = [[-1 for j in range(req_sum+1)] for i in range(n+1)]

print(subset_memo(arr, req_sum, T))
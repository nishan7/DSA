'''
#### Name:  Subarray with zero-sum
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

2 loops
'''


def check_zero(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(i, n):
            subarray = arr[i:j+1]
            # print(subarray)
            if sum(subarray) == 0:
                return True
    
    return False




arr = [-3, 2, 3, 1, 6]    
arr = [-3, 2,-2, 3, 1, 6]    
print(check_zero(arr))
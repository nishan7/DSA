'''
#### Name:  nth Fibonacci
Link: [link]()

#### Sub_question_name: DP(memoization) 
Link: [link]()

'''

def fibo(n, arr):
    if arr[n] != -1:
        return arr[n]
    
    arr[n] = fibo(n-1, arr) + fibo(n-2, arr)
    return arr[n]


n = 5
arr = [-1] * (n+1)
arr[0] = 0
arr[1] = 1

print(fibo(n, arr))

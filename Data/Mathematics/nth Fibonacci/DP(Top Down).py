'''
#### Name:  nth Fibonacci
Link: [link]()

#### Sub_question_name: DP(Top Down) 
Link: [link]()

We create a T array and intiallize with n=0 and n=1  
We run linearly on it

'''


def fibo(n, T):
    
    for i in range(2, n+1):  # Value of 0 and 1 index is initalized, we have to find for index value 5
        T[i] = T[i-1] + T[i-2]
    
    return T[n]


n = 7
T = [-1 for _ in range(n+1)]
T[0] = 0     # initalize with base conditions 
T[1] = 1

print(fibo(n, T))

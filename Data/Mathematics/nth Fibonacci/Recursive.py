'''
#### Name:  nth Fibonacci
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

fibonacci number at nth index
**TE: O(2^n) SE:O(n)?**
'''

def fibo(n):
    if n == 0 or n == 1:
        return n
    
    return fibo(n-1) + fibo(n-2)

print(fibo(5))
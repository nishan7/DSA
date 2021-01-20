'''
#### Name:  nth Fibonacci
Link: [link]()

'''

def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b
        # print(a)  to print all the items in fibonacci series
    return a

print(fib_iter(5))
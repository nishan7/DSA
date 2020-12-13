'''
#### Name:  Kth Grammar

Link: [link](https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10)


n == row; k==column

Base Condition

start from 0 in row
In next row replace 0 by 01 and 1 by 10
e.g
0
01
0110  
0110|1001   # First half is equal to previous row; Second half is complement of first half

given n, k return kth element in nth row

**Brute**
Just get the numbers upto n; and choose the kth value

**IBH**
'''

def kth_Grammar(N, K, complement=False):

    if N==1 and K==1:  # Base Condition
        if complement:
            return 1
        else:
            return 0

    # Induction
    no_of_items = 2 **(N-1)  # as n==1 has 2**0=1; n==3 has 2**2 = 4 and so on
    
    if K > no_of_items//2: # eg k=5 > no.of_items=8//2=4
        # Row above it but complimented
        return kth_Grammar(N-1, K-no_of_items//2, ~complement)
    else:
        return kth_Grammar(N-1, K, complement)
    



print(kth_Grammar(1,1))
print(kth_Grammar(2,1))
print(kth_Grammar(2,2))
print(kth_Grammar(4,5))


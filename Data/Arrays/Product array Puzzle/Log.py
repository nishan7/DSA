'''
#### Name:  Product array Puzzle
Link: [link]()

#### Sub_question_name: Log 
Link: [link]()

'''
from math import log10

def prefix_suffix(nums):
    prod = 0
    for number in nums:
        prod += log10(number)
    
    res = []
    for number in nums:
        res.append(int(pow(10, prod- log10(number))))
    
    print(res)

arr = [10, 3, 5, 6, 2]
prefix_suffix(arr) 
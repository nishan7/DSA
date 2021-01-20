'''
#### Name:  Square root of a Number
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

**O(n^(1/2))**
'''

# Floor sqrt
def sqrt(number):
    if number == 0 or number == 1:
        return number

    i = 1
    while i*i <= number:
        i = i + 1

    
    return i-1


print(sqrt(4))
print(sqrt(11))
print(sqrt(49))
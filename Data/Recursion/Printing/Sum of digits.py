'''
#### Name:  Printing
Link: [link]()

#### Sub_question_name: Sum of digits 
Link: [link]()

# Sum of all the digits in a number
'''

def sum_of_digits(num):
    if num == 0:
        return 0
    
    return num%10 + sum_of_digits(num//10)

print(sum_of_digits(123))
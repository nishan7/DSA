'''
#### Name:  Printing
Link: [link]()

#### Sub_question_name: Cumulative sum upto n 
Link: [link]()

# Similar to factorial but simiply have to print the sum
#  n(n+1)/2
'''
def sum_to_n(n):
    if n == 1:
        return 1
    return n+sum_to_n(n-1)


print(sum_to_n(3))

'''
#### Name:  Printing
Link: [link]()

#### Sub_question_name: 1 to n 
Link: [link]()


### Way of recursion
1) Design a solution: Hypothesis
2) Design a solution for smaller input: Induction

'''

def print_1ton(arr, i):
    if i == -1:
        return
    print_1ton(arr, i-1)
    print(arr[i])

print_1ton([1,2,3,4,5],5-1)

'''
#### Name:  Printing
Link: [link]()

#### Sub_question_name: n to 1 
Link: [link]()



'''

def print_nto1(arr, i):
    if i == -1:
        return
    print(arr[i])
    
    return print_nto1(arr, i-1)


print_nto1([1,2,3,4,5], 5-1)
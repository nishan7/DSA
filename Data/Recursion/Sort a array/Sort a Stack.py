'''
#### Name:  Sort a array
Link: [link]()

#### Sub_question_name: Sort a Stack 
Link: [link](https://www.youtube.com/watch?v=MOGBRkkOhkY&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=7)

Similar to array


'''
# [5, 4, 0 , 1]

def sort(stack):
    if len(stack) <= 1:  # One or zero elements
        return 

    tos = stack.pop() 
    sort(stack)
    insert(stack, tos)

def insert(stack, elem):
    if len(stack) == 0 or elem < stack[-1]:  # Check the len as it could be 0 when insert is called recurisively
        stack.append(elem)
        return

    tos = stack.pop()
    insert(stack, elem)
    stack.append(tos)

stack = [5,4, 0,1]
sort(stack)
print(stack)
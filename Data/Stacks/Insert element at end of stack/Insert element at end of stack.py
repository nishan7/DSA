'''
#### Name:  Insert element at end of stack
Link: [link]()

'''

def add_element(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return
    
    tos = stack.pop()
    add_element(stack, element)
    stack.append(tos)


stack = [4, 6, 8]
add_element(stack, 11)
print(stack)     # 11, 4, 6, 8
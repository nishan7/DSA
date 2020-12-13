'''
#### Name:  Parentheses Check
Link: [link]()

'''

def paran_check(expr):
    stack  = []

    for char in expr:
        if char in ['(','{','[']:  
            stack.append(char)
        elif char in ['+','-','*','/'] or char.isalnum():
            continue
        else:
            if len(stack) == 0:
                return False
            
            tos = stack.pop()
            if tos == '(':
                if char != ')':
                    return False
            if tos == '{':
                if char != '}':
                    return False
            if tos == '[':
                if char != ']':
                    return False
            # Anything else conintue
    
    if len(stack) == 0:  # If stack is empty parenthesis are balanced
        return True
    
    return False


print(paran_check('{(5-1)[]}'))
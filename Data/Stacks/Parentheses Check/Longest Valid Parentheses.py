'''
#### Name:  Parentheses Check
Link: [link]()

#### Sub_question_name: Longest Valid Parentheses 
Link: [link]()


'''


def paran_check(expr):
    opening = 0
    closing = 0


    valid_ctr = 0

    for char in expr:
        if char == '(':
            opening += 1
        elif char == ')':
            closing += 1
        
        if closing > opening:
            closing = opening = 0 # Reset everything

        if closing == opening: # Valid
            valid_ctr= max(valid_ctr, 2 * closing)

    return valid_ctr 
        


print(paran_check('))()()(()'))  #4

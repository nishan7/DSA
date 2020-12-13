'''
#### Name:  Evaluate Expression to True/Boolean Parenthesization
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link](https://www.youtube.com/watch?v=pGVguAcWX4g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=39)

For a expression find the number of way we can parenthesize set so that expression is true   
Note: question may be asked to find false expression
'''


def boolean_paran(string, i, j, is_true):
    # print(string[i:j+1])
    if i > j:   # Empty function
        return False
    if i == j:
        if is_true:  # We want True value
            return string[i] == 'T'
        else:
            return string[i] == 'F'

    count = 0
    for k in range(i+1, j, 2):  # As i+1 -> j-1 as j is exclusive
        # k-1 as we dont need to consider for operator
        left_T = boolean_paran(string, i, k-1, True)
        right_T = boolean_paran(string, k+1, j, True)
        left_F = boolean_paran(string, i, k-1, False)
        right_F = boolean_paran(string, k+1, j, False)

        operator = string[k]
        if operator == '&':
            if is_true:   # If we need True value
                count += left_T * right_T
            else:
                count += left_F * right_F + left_T * right_F + left_F * right_F
        elif operator == '|':
            if is_true:   # If we need True value
                count += left_F * right_F + left_T * right_F + left_F * right_F
            else:
                count += left_T * right_T
        elif operator == '^':
            if is_true:
                count += left_T * right_F + left_F * right_T
            else:
                count += left_T * right_T + left_F*right_F
        
        

    return count


expr = 'T^F&T'
print(boolean_paran(expr, 0, len(expr)-1, True))

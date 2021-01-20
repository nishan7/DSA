'''
#### Name:  Generate all balanced Paranthesis
Link: [link](https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17)

Create a Decision Tree
1) We can put a opening bracket anywhere if possilbe
2) To put a closing bracket we need a matching opening bracket

n =3; will have 6 parenthesis; e.g ()()(), ((())), (()()) .. etc


'''
# open: keeps track of opening brackets remaining to place
# open: keeps track of closing brackets remaining to place


def param(open, close, output, result):
    if open == 0 and close == 0:
        result.append(output)
        return

    # if open == 0: # opening paranthesis are depleted
    #     return param(open, close-1, output+')', result)

    # if close == 0:  # Closing paranthesis are depleted
    #     return param(open-1, close, output+'(', result)

    # # it is balance then we can place only '(';   e.g '()', '()()', '(())', ''
    # if open == close:
    #     return param(open-1, close, output+'(', result)

    # To place a close paranthesis; aleast a opening bracket must exists
    if close > open:
        param(open, close-1, output+')', result)

    # If no open brackets exists, just exit
    if open != 0:    
        param(open-1, close, output+'(', result)
    


result = []
n = 3
param(n, n, '', result)
print(result)

'''
#### Name:  Expression contains redundant bracket or Not
Link: [link]()


1) Insert only bracket and operators(+,-, *, /)
2) If while poping we see a ( in TOS, there is duplicate bracket


**O(n) O(n)**

((a+b)) -> True
(a+b) -> False
'''


def redundant_bracket(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)

        elif char.isalnum():
            continue

        elif char == ')':
            tos = stack.pop()  # Trying to remove operator
            if tos == '(':
                return True

            stack.pop()   # Poping the opening bracket

        elif char in ['+', '-', '*', '/']:
            stack.append(char)

    return False


print(redundant_bracket("(a+b*(c-d))"))
print(redundant_bracket("(a+(b)/c)"))
print(redundant_bracket("((a+b))"))

'''
#### Name:  Minimum number of bracket reversals needed to make an expression balanced.
Link: [link]()

'''


def reversals(s):
    stack = []
    closing = 0
    for bracket in s:
        if bracket == '{':
            stack.append('{')
        elif bracket == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                # stack.append('}')
                closing += 1
    # diff = len(stack)//2 + closing//2
    diff = max(len(stack), closing)
    print(diff)


print(reversals('}{{}}{{{'))
print(reversals('{{}}}}'))
print(reversals('{{}{{{}{{}}{{'))
print(reversals('{{{{}}}}'))

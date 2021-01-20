'''
#### Name:  Subsets/Powerset (IP-OP)
Link: [link](https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12)


##### In all IP-OP questions base condition is when len(inp) ==0
'''
# String


def subset(inp, out, result):
    if len(inp) == 0:
        result.append(out)
        return

    first_char = inp[0]
    inp = inp[1:]

    subset(inp, out, result)
    subset(inp, out+first_char, result)


result = []
subset('abc', '', result)
print(result)


# Arrays
def subset(inp, out, result):
    if len(inp) == 0:
        result.append(out) # append as it will be used later
        return

    first_elem = inp[0]
    inp = inp[1:]
    # first_elem = inp.pop(0) #!! DONOT DO THIS

    subset(inp, out, result)
    # out.append(first_elem)  !!! DONOT DO THIS
    subset(inp, out + [first_elem], result)


result = []
input = [1,2,3]
input = [11, 12, 13, 14]
subset(input, [], result)
print(result)

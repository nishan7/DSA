'''
#### Name:  Print N-bit binary numbers having more **or equal** 1's than 0's for any Prefix
Link: [link](https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19)

We use an extra_one variable to keep track of ones
If extra one is availbe then only it is possible to place a 0
'''


def binary(extra_ones, N, output, result):

    # Base condition, if we get N bits we can return
    if N == 0:
        result.append(output)
        return

    # If there is extra '1', we can add a 0
    if extra_ones > 0:
        binary(extra_ones-1, N-1, output+'0', result)

    binary(extra_ones+1,  N-1, output+'1', result)


N = 4


result = []
binary(0, N, '', result)
print(result)

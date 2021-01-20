'''
#### Name:  Permutations (IP-OP)
Link: [link]()

#### Sub_question_name: Permutations with spaces 
Link: [link](https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14)

'''

def permutation(inp, out,result):
    if len(inp) == 0:
        result.append(out)
        return
    
    first_elem = inp[0]
    inp = inp[1:]
 
    # Choice is: we can insert a item with a space or without a space
    permutation(inp, out+first_elem, result)
    permutation(inp, out+'_'+first_elem, result)


result = []
string = 'ABC'
inp = string[1:]
out = string[0]
permutation(inp, out, result)
print(result)              #['ABC', 'AB_C', 'A_BC', 'A_B_C']
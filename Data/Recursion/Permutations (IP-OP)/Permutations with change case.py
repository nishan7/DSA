'''
#### Name:  Permutations (IP-OP)
Link: [link]()

#### Sub_question_name: Permutations with change case and digit
Link: [link](https://www.youtube.com/watch?v=J2Er5XceU_I&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15)

Choice is to wheather include the letter as it is or do after changin the case
'''


def perm_case(inp, out, result):
    if len(inp) == 0:
        result.append(out)
        return

    first_letter = inp[0]
    inp = inp[1:]

    if first_letter.isdigit():
        perm_case(inp, out+first_letter, result)
    else:
        perm_case(inp, out+first_letter.lower(), result)  # Adding letter as small case
        perm_case(inp, out+first_letter.upper(), result)  # Adding letter as upper case


# inp = 'Ab1C'
inp = '1234'
out = ''
result = []
perm_case(inp, out, result)  #['ab1c', 'ab1C', 'aB1c', 'aB1C', 'Ab1c', 'Ab1C', 'AB1c', 'AB1C']
print(result)

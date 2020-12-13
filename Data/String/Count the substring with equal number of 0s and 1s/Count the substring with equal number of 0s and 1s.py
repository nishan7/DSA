'''
#### Name:  Count the substring with equal number of 0s and 1s
Link: [link]()

Linearly iterate and count the occasions where 0 ctr and 1_ctr where equal
'''


def count(string):
    n = len(string)

    zero_ctr = 0
    one_ctr = 0

    ctr = 0

    for digit in string:
        if digit == '0':
            zero_ctr += 1
        else:
            one_ctr += 1

        if one_ctr == zero_ctr:
            ctr += 1

    print(ctr)


string = "0100110101"
count(string)

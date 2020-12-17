'''
#### Name:  Number of flips to make binary string alternate
Link: [link]()

Try both alternative numbers(ie starting from 0 or 1) 
'''

def alternate_count(binary, start_with):
    # Even index will have to be start_with

    alt_ctr = 0

    for i in range(len(binary)):
        if i % 2 == 0 and binary[i] != start_with:
            alt_ctr += 1
        elif i % 2 == 1 and binary[i] == start_with:
            alt_ctr += 1
    
    return alt_ctr


binary = "0001010111"
print(min(alternate_count(binary, '0'), alternate_count(binary, '1')))  # 2


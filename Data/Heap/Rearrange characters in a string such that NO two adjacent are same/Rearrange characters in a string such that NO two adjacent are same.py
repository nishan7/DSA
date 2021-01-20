'''
#### Name:  Rearrange characters in a string such that NO two adjacent are same
Link: [link]()

1) Simply use max heapq (based on freq) to put the most common char at the time
2) Once popped value can be pushed in another iteration only (so they can be no ajacent characters)

**O(NlogN) O(N^2)**
'''

from heapq import heappush, heappop, heapify

h = []


def h_push(freq, item): 
    return heappush(h, (-1 * freq, item))


def h_pop():
    freq, item = heappop(h)
    return -1*freq, item


def h_max():
    freq, item = h[0]
    return -1*freq, item


def rearrage(s):
    freq_table = {}
    for char in s:
        if char in freq_table.keys():
            freq_table[char] += 1
        else:
            freq_table[char] = 1

    for char, freq in freq_table.items():
        h_push(freq, char)

    res = ''
    prev = 0, '#'
    while h:
        freq, char = h_pop()
        res += char
        
        old_freq, old_char= prev
        if old_freq  > 1: # Still more than 1 freq
            h_push(old_freq-1, old_char)
        
        prev = freq, char
    
    print(res)
    print(len(s) == len(res))




s = 'geeksforgeeks'  # True
s ='bbbabaaacd'      # True
s = 'bbb'            # False
rearrage(s)
